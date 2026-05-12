#!/usr/bin/env python3
"""
Literature Review — Web-Based Rich Editor
===========================================
Opens a browser-based WYSIWYG editor for reviewing, annotating, and revising
literature review content at key editing touch points.

Features:
  - Inline editing (click to edit any paragraph)
  - Text annotations (select text, add comment)
  - Block-level deletion with undo
  - Visual annotation indicators
  - Save changes back to the original markdown file

Usage:
  python3 review_editor.py --file "editing/topic_statement.md" --title "Topic Statement"

Touch points (called by the literature_review skill):
  TP-1  Step 2.12 — Topic Statement draft
  TP-2  Step 5.B5 — Detailed outline
  TP-3  Step 5.C  — Thematic section 1
  TP-4  Step 5.C  — Thematic section 2 (and 3+)
  TP-5  Step 5.C  — Cross-theme synthesis
  TP-6  Step 5.C  — Conclusion
  TP-7  Step 5.C  — Introduction
  TP-8  Step 6.C  — Title candidates
"""

import argparse
import json
import os
import re
import sys
import threading
import time
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse


# ── HTML / CSS / JS template ────────────────────────────────────────────────

EDITOR_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Review Editor</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #f0f2f5; color: #1a1a2e; line-height: 1.8; font-size: 15px;
  }}

  /* ── Toolbar ── */
  #toolbar {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    background: #fff; border-bottom: 1px solid #e0e0e0;
    padding: 12px 24px; display: flex; align-items: center; gap: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }}
  #toolbar h1 {{
    font-size: 18px; font-weight: 600; flex: 1; white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis;
  }}
  #toolbar .hint {{
    font-size: 13px; color: #888; white-space: nowrap;
  }}
  #saveBtn {{
    padding: 8px 24px; background: #2563eb; color: #fff; border: none;
    border-radius: 6px; font-size: 14px; font-weight: 500; cursor: pointer;
    transition: background 0.15s; white-space: nowrap;
  }}
  #saveBtn:hover {{ background: #1d4ed8; }}
  #saveBtn:disabled {{ background: #93c5fd; cursor: not-allowed; }}
  #saveBtn .shortcut {{ opacity: 0.7; font-size: 12px; margin-left: 6px; }}
  #statusBar {{
    position: fixed; top: 56px; left: 0; right: 0; z-index: 999;
    text-align: center; padding: 6px; font-size: 13px; display: none;
  }}
  #statusBar.saving {{ background: #fef3c7; color: #92400e; display: block; }}
  #statusBar.saved {{ background: #d1fae5; color: #065f46; display: block; }}
  #statusBar.error {{ background: #fee2e2; color: #991b1b; display: block; }}

  /* ── Content area ── */
  #content {{
    max-width: 860px; margin: 80px auto 40px; padding: 0 20px;
  }}

  /* ── Block cards ── */
  .block {{
    background: #fff; border-radius: 8px; padding: 16px 20px;
    margin-bottom: 12px; border: 1px solid #e8e8e8;
    transition: border-color 0.2s, opacity 0.3s, background 0.3s;
    position: relative;
  }}
  .block:hover {{ border-color: #c0c0c0; }}
  .block.deleted {{
    opacity: 0.35; background: #fafafa; border-color: #ffcccc;
  }}
  .block.deleted .block-text {{
    text-decoration: line-through; color: #999;
  }}
  .block.has-annotation {{
    border-left: 3px solid #f59e0b;
  }}
  .block.dragover {{
    border-color: #2563eb; border-style: dashed;
    background: #eff6ff;
  }}

  /* block handle for drag */
  .block-handle {{
    position: absolute; left: -6px; top: 50%; transform: translateY(-50%);
    width: 12px; height: 32px; cursor: grab; opacity: 0;
    transition: opacity 0.2s; display: flex; align-items: center; justify-content: center;
    color: #bbb; font-size: 16px; user-select: none;
  }}
  .block:hover .block-handle {{ opacity: 1; }}
  .block-handle:hover {{ color: #666; }}

  /* Block header (type badge + action buttons) */
  .block-header {{
    display: flex; align-items: center; gap: 8px; margin-bottom: 8px;
    font-size: 12px; color: #999;
  }}
  .block-type {{
    background: #f0f0f0; padding: 1px 8px; border-radius: 3px;
    font-size: 11px; text-transform: uppercase; letter-spacing: 0.3px;
  }}
  .block-type.heading {{ background: #dbeafe; color: #1e40af; }}
  .block-actions {{
    margin-left: auto; display: flex; gap: 4px; align-items: center;
  }}
  .block-actions button {{
    background: none; border: 1px solid transparent; cursor: pointer;
    padding: 2px 8px; border-radius: 4px; font-size: 13px; color: #888;
    transition: all 0.15s; line-height: 1.6;
  }}
  .block-actions .btn-annotate:hover {{ background: #fef3c7; color: #b45309; border-color: #fde68a; }}
  .block-actions .btn-annotate.active {{ background: #fef3c7; color: #b45309; }}
  .block-actions .btn-delete:hover {{ background: #fee2e2; color: #dc2626; border-color: #fecaca; }}
  .block-actions .btn-delete.active {{ background: #fee2e2; color: #dc2626; }}
  .block-actions .annotation-count {{
    font-size: 12px; color: #b45309; cursor: pointer;
    padding: 1px 6px; border-radius: 10px; background: #fef3c7;
  }}

  /* Block text content */
  .block-text {{
    min-height: 1.5em; outline: none; white-space: pre-wrap; word-wrap: break-word;
    padding: 4px 0;
  }}
  .block-text:focus {{
    background: #fafeff; border-radius: 2px;
  }}
  .block-text.ann-hl {{
    background: #fef9c3; border-radius: 2px; cursor: help;
  }}
  .block-text[h5-el] {{
    font-size: 1.2em; font-weight: 600; color: #1e293b;
  }}
  .block-text[h4-el] {{
    font-size: 1.1em; font-weight: 600; color: #1e293b;
  }}
  .block-text[h3-el] {{
    font-size: 1.0em; font-weight: 600; color: #1e293b;
  }}

  /* ── Annotation popup ── */
  #annOverlay {{
    display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.3);
    z-index: 2000; justify-content: center; align-items: center;
  }}
  #annOverlay.active {{ display: flex; }}
  #annPopup {{
    background: #fff; border-radius: 12px; padding: 24px; width: 480px;
    max-width: 90vw; box-shadow: 0 20px 60px rgba(0,0,0,0.2);
  }}
  #annPopup h3 {{ font-size: 16px; margin-bottom: 4px; }}
  #annPopup .ann-preview {{
    background: #f8f9fa; padding: 12px; border-radius: 6px;
    font-size: 14px; margin: 8px 0 12px; border-left: 3px solid #f59e0b;
    max-height: 80px; overflow-y: auto;
  }}
  #annPopup textarea {{
    width: 100%; min-height: 80px; padding: 10px; border: 1px solid #d0d0d0;
    border-radius: 6px; font-size: 14px; font-family: inherit; resize: vertical;
  }}
  #annPopup textarea:focus {{ outline: none; border-color: #2563eb; }}
  .ann-actions {{ display: flex; gap: 8px; justify-content: flex-end; margin-top: 12px; }}
  .ann-actions button {{
    padding: 6px 20px; border-radius: 6px; font-size: 14px; cursor: pointer;
    border: 1px solid #d0d0d0; background: #fff;
  }}
  .ann-actions .ann-save {{ background: #2563eb; color: #fff; border-color: #2563eb; }}
  .ann-actions .ann-save:hover {{ background: #1d4ed8; }}
  .ann-actions .ann-cancel:hover {{ background: #f5f5f5; }}

  /* ── Annotation markers in text ── */
  .ann-marker {{
    background: #fef3c7; border-bottom: 2px solid #f59e0b; cursor: help;
    border-radius: 2px; padding: 0 1px;
    transition: background 0.15s;
  }}
  .ann-marker:hover {{ background: #fde68a; }}

  /* ── Annotation list sidebar ── */
  #annSidebar {{
    position: fixed; right: -360px; top: 56px; width: 340px; bottom: 0;
    background: #fff; border-left: 1px solid #e0e0e0;
    transition: right 0.25s ease; z-index: 900;
    overflow-y: auto; padding: 16px; box-shadow: -2px 0 8px rgba(0,0,0,0.05);
  }}
  #annSidebar.open {{ right: 0; }}
  #annSidebar h3 {{ font-size: 15px; margin-bottom: 12px; color: #333; }}
  .ann-item {{
    padding: 10px; border-radius: 6px; background: #fffbeb;
    margin-bottom: 8px; border-left: 3px solid #f59e0b; font-size: 13px;
  }}
  .ann-item .ann-item-text {{ color: #92400e; margin-bottom: 4px; }}
  .ann-item .ann-item-ref {{ font-size: 12px; color: #999; }}
  .ann-item .ann-del {{
    float: right; cursor: pointer; color: #ccc; background: none; border: none;
    font-size: 14px;
  }}
  .ann-item .ann-del:hover {{ color: #dc2626; }}

  /* ── Save notification overlay ── */
  #saveOverlay {{
    display: none; position: fixed; inset: 0; z-index: 3000;
    background: rgba(255,255,255,0.95);
    justify-content: center; align-items: center; flex-direction: column;
    text-align: center;
  }}
  #saveOverlay.active {{ display: flex; }}
  #saveOverlay .check {{
    font-size: 64px; color: #16a34a; margin-bottom: 16px;
  }}
  #saveOverlay h2 {{ font-size: 24px; color: #1a1a2e; margin-bottom: 8px; }}
  #saveOverlay p {{ font-size: 15px; color: #666; }}

  /* ── Responsive ── */
  @media (max-width: 768px) {{
    #toolbar {{ padding: 10px 16px; flex-wrap: wrap; }}
    #toolbar h1 {{ font-size: 16px; width: 100%; order: -1; margin-bottom: 4px; }}
    #content {{ margin-top: 100px; padding: 0 12px; }}
    .block {{ padding: 12px 14px; }}
    #annSidebar {{ width: 100%; right: -100%; }}
  }}
</style>
</head>
<body>

<div id="toolbar">
  <h1>📝 {title}</h1>
  <span class="hint">💡 Click text to edit · Select text to annotate · <kbd>Ctrl+S</kbd> save</span>
  <button id="saveBtn">💾 Save &amp; Close<span class="shortcut">Ctrl+S</span></button>
</div>
<div id="statusBar"></div>

<div id="content"></div>

<!-- Annotation Overlay -->
<div id="annOverlay">
  <div id="annPopup">
    <h3>💬 Add Annotation</h3>
    <div class="ann-preview" id="annPreview"></div>
    <textarea id="annText" placeholder="Enter your annotation, comment, or suggestion..."></textarea>
    <div class="ann-actions">
      <button class="ann-cancel" onclick="closeAnnotation()">Cancel</button>
      <button class="ann-save" onclick="saveAnnotation()">Save Annotation</button>
    </div>
  </div>
</div>

<!-- Annotation Sidebar -->
<div id="annSidebar">
  <h3>📋 All Annotations
    <span id="annCount" style="font-weight:normal;color:#999;"></span>
  </h3>
  <div id="annList"></div>
</div>

<!-- Save Overlay -->
<div id="saveOverlay">
  <div class="check">✓</div>
  <h2>Saved Successfully</h2>
  <p id="saveMsg">Your changes have been written back to the file.</p>
</div>

<script>
// ── Data ──────────────────────────────────────────────────────────────
let blocks = {json_blocks};
let annotations = {{}};
let nextAnnId = 0;
let currentAnnBlockId = null;
let currentAnnSelection = null;

// ── Render ────────────────────────────────────────────────────────────
function render() {{
  const container = document.getElementById('content');
  container.innerHTML = '';
  blocks.forEach((block, idx) => {{
    const div = document.createElement('div');
    div.className = 'block' + (block.deleted ? ' deleted' : '') + (block.hasAnnotation ? ' has-annotation' : '');
    div.dataset.id = block.id;
    div.dataset.type = block.type;

    const handle = document.createElement('div');
    handle.className = 'block-handle';
    handle.textContent = '⠿';

    const header = document.createElement('div');
    header.className = 'block-header';

    const typeLabel = document.createElement('span');
    typeLabel.className = 'block-type' + (block.type === 'heading' ? ' heading' : '');
    typeLabel.textContent = block.type === 'heading' ? 'Heading' : block.type === 'heading2' ? 'H2' : block.type === 'heading3' ? 'H3' : 'Paragraph';
    header.appendChild(typeLabel);

    const actions = document.createElement('div');
    actions.className = 'block-actions';

    // Annotation button
    const annBtn = document.createElement('button');
    annBtn.className = 'btn-annotate' + (block.hasAnnotation ? ' active' : '');
    annBtn.textContent = '💬';
    annBtn.title = 'Add annotation to this block';
    annBtn.onclick = () => openAnnotation(block.id);
    actions.appendChild(annBtn);

    // Annotation count
    if (block.hasAnnotation) {{
      const count = document.createElement('span');
      count.className = 'annotation-count';
      const anns = Object.values(annotations).filter(a => a.blockId === block.id);
      count.textContent = anns.length + ' ann';
      count.title = anns.map(a => a.text).join('\n');
      count.onclick = () => toggleSidebar();
      actions.appendChild(count);
    }}

    // Delete/restore button
    const delBtn = document.createElement('button');
    delBtn.className = 'btn-delete' + (block.deleted ? ' active' : '');
    delBtn.textContent = block.deleted ? '↩' : '✕';
    delBtn.title = block.deleted ? 'Restore block' : 'Delete block';
    delBtn.onclick = () => toggleDelete(block.id);
    actions.appendChild(delBtn);

    header.appendChild(actions);

    // Text content
    const textDiv = document.createElement('div');
    textDiv.className = 'block-text';
    textDiv.contentEditable = true;
    textDiv.dataset.blockId = block.id;
    // Render annotations markers in the text
    textDiv.innerHTML = renderTextWithAnnotations(block);

    textDiv.addEventListener('blur', function() {{
      block.text = this.innerText;
    }});
    textDiv.addEventListener('keydown', function(e) {{
      if (e.key === 'Enter' && !e.shiftKey) {{
        e.preventDefault();
        this.blur();
      }}
    }});
    textDiv.addEventListener('mouseup', function(e) {{
      const sel = window.getSelection();
      if (sel && !sel.isCollapsed && this.contains(sel.anchorNode)) {{
        // User selected text within this block
        handleTextSelection(e, block.id);
      }}
    }});
    textDiv.addEventListener('touchend', function(e) {{
      // On mobile, defer to mouseup
    }});

    div.appendChild(handle);
    div.appendChild(header);
    div.appendChild(textDiv);
    container.appendChild(div);
  }});
  updateAnnotationCounts();
}}

function renderTextWithAnnotations(block) {{
  let text = escapeHtml(block.text);
  const anns = Object.values(annotations).filter(a => a.blockId === block.id);
  if (anns.length === 0) return text.replace(/\n/g, '<br>');
  // Build sorted annotation markers
  // We store start/end as character offsets in the plain text
  // Simple approach: wrap annotated ranges with spans
  const markers = [];
  anns.forEach(a => {{
    if (a.startIdx !== undefined && a.endIdx !== undefined) {{
      markers.push({{ start: a.startIdx, end: a.endIdx, id: a.id, text: a.text }});
    }}
  }});
  if (markers.length === 0) return text.replace(/\n/g, '<br>');
  markers.sort((a, b) => a.start - b.start);
  // Check for overlap, don't double-wrap
  let result = '';
  let pos = 0;
  // Remove overlapping markers — keep only non-overlapping ones
  const filtered = [];
  markers.forEach(m => {{
    if (filtered.length === 0 || m.start >= filtered[filtered.length - 1].end) {{
      filtered.push(m);
    }}
    // If overlapping, skip (could merge, but for simplicity skip)
  }});
  filtered.forEach(m => {{
    result += text.substring(pos, m.start);
    result += '<span class="ann-marker" title="' + escapeHtml(m.text) + '">' + escapeHtml(text.substring(m.start, m.end)) + '</span>';
    pos = m.end;
  }});
  result += text.substring(pos);
  return result.replace(/\\n/g, '<br>');
}}

function escapeHtml(str) {{
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}}

// ── Annotations ───────────────────────────────────────────────────────
function openAnnotation(blockId) {{
  const sel = window.getSelection();
  let selectedText = '';
  let startIdx = -1;
  let endIdx = -1;
  if (sel && !sel.isCollapsed) {{
    selectedText = sel.toString().trim();
    if (selectedText) {{
      // Find offset in the block's plain text
      const block = blocks.find(b => b.id === blockId);
      if (block && sel.anchorNode) {{
        // Use a simple approach: find the selected text in the block text
        const idx = block.text.indexOf(selectedText);
        if (idx >= 0) {{
          startIdx = idx;
          endIdx = idx + selectedText.length;
        }}
      }}
    }}
  }}
  currentAnnBlockId = blockId;
  currentAnnSelection = {{ text: selectedText, startIdx, endIdx }};
  document.getElementById('annPreview').textContent = selectedText || '(full block)';
  document.getElementById('annText').value = '';
  document.getElementById('annText').focus();
  document.getElementById('annOverlay').classList.add('active');
}}

function closeAnnotation() {{
  document.getElementById('annOverlay').classList.remove('active');
  currentAnnBlockId = null;
  currentAnnSelection = null;
}}

function saveAnnotation() {{
  const text = document.getElementById('annText').value.trim();
  if (!text) return;
  const id = 'ann-' + (nextAnnId++);
  annotations[id] = {{
    id: id,
    blockId: currentAnnBlockId,
    text: text,
    startIdx: currentAnnSelection ? currentAnnSelection.startIdx : undefined,
    endIdx: currentAnnSelection ? currentAnnSelection.endIdx : undefined
  }};
  const block = blocks.find(b => b.id === currentAnnBlockId);
  if (block) block.hasAnnotation = true;
  closeAnnotation();
  render();
}}

function deleteAnnotation(annId) {{
  const ann = annotations[annId];
  if (!ann) return;
  delete annotations[annId];
  // Check if block still has annotations
  const block = blocks.find(b => b.id === ann.blockId);
  if (block) {{
    const remaining = Object.values(annotations).filter(a => a.blockId === block.id);
    if (remaining.length === 0) block.hasAnnotation = false;
  }}
  render();
}}

function toggleSidebar() {{
  const sidebar = document.getElementById('annSidebar');
  sidebar.classList.toggle('open');
  if (sidebar.classList.contains('open')) {{
    updateSidebarContent();
  }}
}}

function updateSidebarContent() {{
  const list = document.getElementById('annList');
  const count = document.getElementById('annCount');
  const vals = Object.values(annotations);
  count.textContent = '(' + vals.length + ' total)';
  list.innerHTML = '';
  if (vals.length === 0) {{
    list.innerHTML = '<p style="color:#999;font-size:13px;">No annotations yet.</p>';
    return;
  }}
  vals.forEach(a => {{
    const div = document.createElement('div');
    div.className = 'ann-item';
    const del = document.createElement('button');
    del.className = 'ann-del';
    del.textContent = '✕';
    del.onclick = () => deleteAnnotation(a.id);
    div.appendChild(del);
    const ref = document.createElement('div');
    ref.className = 'ann-item-ref';
    const blockIdx = blocks.findIndex(b => b.id === a.blockId);
    ref.textContent = 'Block #' + (blockIdx + 1);
    div.appendChild(ref);
    const txt = document.createElement('div');
    txt.className = 'ann-item-text';
    txt.textContent = a.text;
    div.appendChild(txt);
    list.appendChild(div);
  }});
}}

function updateAnnotationCounts() {{
  const total = Object.keys(annotations).length;
  if (total > 0) {{
    // Update toolbar with annotation count
    let badge = document.getElementById('annBadge');
    if (!badge) {{
      badge = document.createElement('span');
      badge.id = 'annBadge';
      badge.style.cssText = 'font-size:13px;color:#b45309;cursor:pointer;';
      badge.onclick = toggleSidebar;
      const hint = document.querySelector('.hint');
      if (hint) hint.after(badge);
    }}
    badge.textContent = '📌 ' + total + ' annotation' + (total > 1 ? 's' : '');
  }}
}}

// ── Block actions ─────────────────────────────────────────────────────
function toggleDelete(blockId) {{
  const block = blocks.find(b => b.id === blockId);
  if (block) {{
    block.deleted = !block.deleted;
    render();
  }}
}}

// ── Text selection context toolbar ────────────────────────────────────
function handleTextSelection(event, blockId) {{
  // Show a small floating annotate button near the selection
  const sel = window.getSelection();
  if (!sel || sel.isCollapsed) return;
  const text = sel.toString().trim();
  if (!text || text.length < 2) return;
  // Could show inline popup — for simplicity, just auto-open annotation
  // We'll let the user click the 💬 button manually
}}

// ── Keyboard shortcuts ────────────────────────────────────────────────
document.addEventListener('keydown', function(e) {{
  if ((e.ctrlKey || e.metaKey) && e.key === 's') {{
    e.preventDefault();
    saveContent();
  }}
}});

// ── Save ──────────────────────────────────────────────────────────────
async function saveContent() {{
  const btn = document.getElementById('saveBtn');
  const statusBar = document.getElementById('statusBar');
  btn.disabled = true;
  statusBar.className = 'saving';
  statusBar.textContent = '⏳ Saving...';

  // Collect current text from contenteditable divs
  document.querySelectorAll('.block-text').forEach(el => {{
    const id = el.dataset.blockId;
    const block = blocks.find(b => b.id === id);
    if (block) block.text = el.innerText;
  }});

  // Build output: non-deleted blocks in order
  const outputBlocks = blocks.filter(b => !b.deleted);
  const outputText = outputBlocks.map(b => b.text).join('\n\n');

  try {{
    const resp = await fetch('/api/save', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ content: outputText, annotations: Object.values(annotations) }})
    }});
    const result = await resp.json();
    if (result.status === 'ok') {{
      statusBar.className = 'saved';
      statusBar.textContent = '✅ Saved successfully!';
      setTimeout(() => {{
        document.getElementById('saveOverlay').classList.add('active');
        document.getElementById('saveMsg').textContent = 'Saved ' + outputBlocks.length + ' blocks to ' + result.file;
        // Notify server to shutdown after 2 seconds
        setTimeout(() => {{
          fetch('/api/shutdown', {{ method: 'POST' }}).catch(() => {{}});
        }}, 2000);
      }}, 500);
    }} else {{
      throw new Error(result.message || 'Save failed');
    }}
  }} catch (err) {{
    statusBar.className = 'error';
    statusBar.textContent = '❌ Error: ' + err.message;
    btn.disabled = false;
  }}
}}

// Re-save on button click
document.getElementById('saveBtn').addEventListener('click', saveContent);

// Init
render();
</script>
</body>
</html>
"""


# ── HTTP Handler ────────────────────────────────────────────────────────────

class ReviewEditorHandler(BaseHTTPRequestHandler):
    """HTTP handler that serves the editor and processes save requests."""

    content = ""
    output_path = ""
    title = "Review Content"
    saved = threading.Event()

    # Silence default logging
    def log_message(self, format, *args):
        pass

    @classmethod
    def _parse_content(cls):
        """Parse markdown content into structured blocks."""
        blocks = []
        text = cls.content
        paragraphs = re.split(r'\n\s*\n', text)
        idx = 0
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            block_id = f"b{idx}"
            block_type = "paragraph"
            if para.startswith("# ") or para.startswith("#\t"):
                block_type = "heading"
            elif para.startswith("## "):
                block_type = "heading2"
            elif para.startswith("### "):
                block_type = "heading3"
            blocks.append({
                "id": block_id,
                "type": block_type,
                "text": para,
                "deleted": False,
                "hasAnnotation": False,
            })
            idx += 1
        return blocks

    @classmethod
    def _render_html(cls):
        """Render the editor HTML with content embedded."""
        blocks_json = json.dumps(cls._parse_content(), ensure_ascii=False)
        return EDITOR_HTML.format(
            title=cls.title,
            json_blocks=blocks_json,
        )

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/", "", "/index.html"):
            html = self._render_html()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        elif parsed.path == "/api/health":
            self._send_json({"status": "ok"})
        else:
            self.send_error(404)

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length else "{}"

        if parsed.path == "/api/save":
            try:
                data = json.loads(body)
                content = data.get("content", "")
                annotations = data.get("annotations", [])
                output_path = self.__class__.output_path

                # Write content back to file
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(content)
                    f.write("\n")

                # If there are annotations, also save them alongside
                if annotations:
                    ann_path = os.path.splitext(output_path)[0] + "_annotations.json"
                    with open(ann_path, "w", encoding="utf-8") as f:
                        json.dump(annotations, f, ensure_ascii=False, indent=2)

                self.__class__.saved.set()
                self._send_json({
                    "status": "ok",
                    "file": os.path.basename(output_path),
                    "blocks": len(content.strip().split("\n\n")) if content.strip() else 0,
                })
            except Exception as e:
                self._send_json({"status": "error", "message": str(e)}, 500)

        elif parsed.path == "/api/shutdown":
            self._send_json({"status": "shutting_down"})
            # Schedule shutdown in a separate thread
            def shutdown():
                time.sleep(0.5)
                self.server.shutdown()
            threading.Thread(target=shutdown, daemon=True).start()

        else:
            self.send_error(404)

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    # Suppress noisy stderr from server
    def log_error(self, format, *args):
        pass


# ── CLI Entry Point ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Browser-based rich editor for literature review content."
    )
    parser.add_argument(
        "--file", required=True,
        help="Path to the markdown file to edit"
    )
    parser.add_argument(
        "--title", default="Review Content",
        help="Display title for the editor page"
    )
    parser.add_argument(
        "--port", type=int, default=0,
        help="Port number (0 = auto-select)"
    )
    args = parser.parse_args()

    # Resolve file path
    file_path = os.path.abspath(args.file)
    if not os.path.exists(file_path):
        print(f"[review_editor] Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Read file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"[review_editor] Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    if not content.strip():
        print(f"[review_editor] Warning: File is empty: {file_path}", file=sys.stderr)

    # Configure handler
    ReviewEditorHandler.content = content
    ReviewEditorHandler.output_path = file_path
    ReviewEditorHandler.title = args.title
    ReviewEditorHandler.saved.clear()

    # Start server
    server = HTTPServer(("127.0.0.1", args.port), ReviewEditorHandler)
    port = server.server_address[1]

    # Open browser
    url = f"http://127.0.0.1:{port}/"
    try:
        webbrowser.open(url)
    except Exception:
        pass  # Non-blocking; may fail on headless systems

    print(f"┌──────────────────────────────────────────────────────────────┐", file=sys.stderr)
    print(f"│  📝 Review Editor — {args.title}", file=sys.stderr)
    print(f"│", file=sys.stderr)
    print(f"│  Open in browser: {url}", file=sys.stderr)
    print(f"│", file=sys.stderr)
    print(f"│  Features:", file=sys.stderr)
    print(f"│    • Click text to edit inline", file=sys.stderr)
    print(f"│    • Click 💬 to annotate a block", file=sys.stderr)
    print(f"│    • Click ✕ to delete / ↩ to restore", file=sys.stderr)
    print(f"│    • Ctrl+S or click Save & Close when done", file=sys.stderr)
    print(f"│", file=sys.stderr)
    print(f"│  File: {os.path.basename(file_path)}", file=sys.stderr)
    print(f"└──────────────────────────────────────────────────────────────┘", file=sys.stderr)

    # Serve until saved
    try:
        ReviewEditorHandler.saved.wait()  # Block until save
    except KeyboardInterrupt:
        print(f"\n[review_editor] Interrupted.", file=sys.stderr)
    finally:
        server.shutdown()
        server.server_close()

    # Re-read the saved file to confirm
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            saved_content = f.read()
        lines = saved_content.strip().count("\n") + 1 if saved_content.strip() else 0
        print(f"[review_editor] ✅ Saved — {lines} lines written to {file_path}", file=sys.stderr)
    except Exception as e:
        print(f"[review_editor] ⚠️  File saved but could not verify: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
