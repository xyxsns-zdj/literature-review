#!/usr/bin/env python3
"""
Literature Review — Editable Content Box
========================================
Called by the literature_review skill at key editing touch points.
Opens content in an editor for the user to revise, then outputs the result.

Usage:
  python3 edit_content.py --title "Topic Statement" --content "..." [--out result.md]

Or pipe content in:
  echo "content" | python3 edit_content.py --title "Section Title"

Touch points (skill auto-triggers at these moments):
  Step 2.12 — Topic Statement draft
  Step 5.3  — Each thematic category section of first draft
  Step 5.4  — Cross-theme synthesis section
  Step 5.5  — Conclusion section
  Step 5.6  — Introduction section
  Step 6.C  — Title refinement candidates
"""

import argparse
import os
import subprocess
import sys
import tempfile

MARKER_START = "<!-- ===== EDIT BELOW THIS LINE ====="
MARKER_END = "===== EDIT ABOVE THIS LINE -->"


def detect_editor():
    """Find the best available text editor on the system."""
    # Priority: GUI editors first, then terminal editors
    candidates = [
        # Windows (via WSL interop)
        "notepad.exe",
        "code",         # VS Code
        "subl",         # Sublime Text
        # Linux GUI
        "gedit",
        "mousepad",
        "kate",
        # Terminal editors
        "nano",
        "vim",
        "vi",
    ]
    for editor in candidates:
        try:
            subprocess.run(
                ["which", editor],
                capture_output=True, text=True, timeout=3
            )
            return editor
        except (subprocess.TimeoutExpired, FileNotFoundError):
            continue
    return "nano"  # ultimate fallback


def main():
    parser = argparse.ArgumentParser(
        description="Open content in an editable text box for revision."
    )
    parser.add_argument(
        "--title", required=True,
        help="Display title for this editing session (e.g., 'Topic Statement')"
    )
    parser.add_argument(
        "--content",
        help="Initial content text (if not provided, reads from stdin)"
    )
    parser.add_argument(
        "--out",
        help="Output file path (default: prints to stdout)"
    )
    parser.add_argument(
        "--editor",
        help="Editor command override (e.g., 'code', 'nano')"
    )
    args = parser.parse_args()

    # Get content
    content = args.content
    if content is None:
        content = sys.stdin.read().strip()

    if not content:
        print("Error: No content provided.", file=sys.stderr)
        sys.exit(1)

    # Build the editable file
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    )
    tmp.write(f"# {args.title}\n\n")
    tmp.write(f"{MARKER_START}\n")
    tmp.write("<!-- Edit the content below. Save the file and close the editor. -->\n")
    tmp.write("<!-- The skill will read your revised content and continue. -->\n\n")
    tmp.write(content)
    tmp.write(f"\n\n{MARKER_END}\n")
    tmp_path = tmp.name
    tmp.close()

    editor = args.editor or detect_editor()

    print(f"[edit_content] Opening '{args.title}' in {editor}...", file=sys.stderr)
    print(f"[edit_content] File: {tmp_path}", file=sys.stderr)
    print(f"[edit_content] Edit the content, save, and close the editor.", file=sys.stderr)

    # Open editor and wait for it to close
    try:
        subprocess.run([editor, tmp_path], check=True)
    except subprocess.CalledProcessError:
        # Editor returned non-zero — user might have closed without saving
        print("[edit_content] Editor closed. Reading file...", file=sys.stderr)
    except FileNotFoundError:
        print(f"[edit_content] Editor '{editor}' not found.", file=sys.stderr)
        print("[edit_content] Manually edit and save:", tmp_path, file=sys.stderr)
        input("[edit_content] Press Enter after you've edited and saved the file...")

    # Read back modified content
    try:
        with open(tmp_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: Edited file not found. Was it deleted?", file=sys.stderr)
        sys.exit(1)

    # Extract content between markers
    start_idx = text.find(MARKER_START)
    end_idx = text.find(MARKER_END)

    if start_idx != -1 and end_idx != -1:
        # Get content between markers
        start_line_end = text.index("\n", start_idx) + 1
        modified = text[start_line_end:end_idx].strip()
        # Remove the HTML comment lines
        lines = modified.split("\n")
        cleaned = []
        for line in lines:
            if line.strip().startswith("<!--") and line.strip().endswith("-->"):
                continue
            cleaned.append(line)
        modified = "\n".join(cleaned).strip()
    else:
        # Markers removed — take everything after the title
        modified = text.split("\n\n", 1)[1] if "\n\n" in text else text

    # Clean up temp file
    try:
        os.unlink(tmp_path)
    except OSError:
        pass

    # Output
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(modified)
        print(f"[edit_content] Saved to {args.out}", file=sys.stderr)
    else:
        print(modified)

    print("[edit_content] Done — content captured.", file=sys.stderr)


if __name__ == "__main__":
    main()
