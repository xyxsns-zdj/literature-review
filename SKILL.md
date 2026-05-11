---
name: literature-review
description: "Complete 7-step literature review writing + citation verification workflow based on Galván & Galván (2017). Strict step-by-step execution. Features multi-source API literature search (arXiv, PubMed, Web of Science via sci_lib/sci_search.py) and real Zotero Web API v3 integration (sci_lib/zotero.py). Includes automated peer review (academic-paper-reviewer) and citation verification (LitSense/NCBI, Zotero import, .docx export, HTML verification report). Interactive editing boxes at 8 key touch points."
metadata:
  version: "2.1.0"
  last_updated: "2026-05-11"
  status: active
  based_on: "Galván, J. L., & Galván, M. C. (2017). Writing Literature Reviews (7th ed.). Routledge."
  writing_reference: "University of Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/)"
  task_type: guided
  execution_mode: strict_sequential
  ai_capabilities: "WebSearch, WebFetch, AskUserQuestion, edit_content.py, Agent, Skill (academic-paper-reviewer), sci_lib/sci_search.py, sci_lib/zotero.py, python-docx"
  integrates_with: "academic-paper-reviewer (v3.7.0) — multi-perspective peer review; LitSense/NCBI — sentence-level literature search; Zotero — reference collection management; sci_lib/sci_search.py — multi-source API search (arXiv, PubMed, WoS); sci_lib/zotero.py — Zotero Web API v3 CLI"
---

# Literature Review Writing — Complete 7-Step Workflow (v2.0.0)

Based on **José L. Galván & Melisa C. Galván, *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th Edition, Routledge, 2017)**.

---

## 🔴 最高准则 — SUPREME RULE（必须遵守，不可逾越）

> **所有内容必须基于 PubMed 或 Web of Science 收录的真实文献，严禁杜撰。**

这是不可协商的底线。每一次写作或审校都必须遵守：

1. **所有引用的研究、数据、作者、期刊、年份** — 必须来自 PubMed 或 Web of Science 可检索到的真实论文
2. **禁止编造** — 禁止凭空生成论文标题、作者名、DOI、期刊卷期页码、或研究结果
3. **每引用必验证** — 引用的每条文献都须通过 WebSearch/WebFetch 在 PubMed 或 Web of Science 上核实其真实性
4. **存疑即标注** — 若某条文献无法在 PubMed/WoS 找到明确记录，须标记为"⚠️ 待核实"并告知用户，不得直接使用
5. **用户提供的信息优先** — 若用户提供了具体文献，以用户提供的为准，但仍需在 PubMed/WoS 上验证

> 违反本准则意味着生成不可靠的学术内容，这是不可接受的。

---

## 🔧 Environment Variables

The following environment variables enable API-based literature search and Zotero integration. Set them in `~/.claude/settings.local.json` or your shell profile.

### Literature Search (sci_lib/sci_search.py)
- `WOS_API_KEY` — Web of Science Starter API key.
  - **Required for**: Web of Science search (optional; arXiv and PubMed work without it)
  - **Get one**: https://developer.clarivate.com/apis/wos-starter (free tier available)
  - **Usage**: `python3 sci_lib/sci_search.py "<query>" --source wos`

### Zotero Integration (sci_lib/zotero.py)
- `ZOTERO_API_KEY` — Zotero API key.
  - **Required for**: All `sci_lib/zotero.py` commands
  - **Get one**: https://www.zotero.org/settings/keys/new
- `ZOTERO_USER_ID` — Your Zotero numeric user ID.
  - **Required for**: Personal library access
  - **Find it**: https://www.zotero.org/settings/keys (displayed at the top)
- `ZOTERO_GROUP_ID` — Zotero group ID (alternative to USER_ID for group libraries).
  - **Optional**: Use instead of `ZOTERO_USER_ID` for shared group libraries

### Verification
To test configuration:
```bash
# Test sci_search.py (PubMed search, no API key needed)
python3 sci_lib/sci_search.py "test query" --source pubmed --limit 2

# Test zotero.py (requires API key + user ID)
python3 sci_lib/zotero.py items --limit 5
```

---

## ⛔ STRICT EXECUTION PROTOCOL — READ THIS FIRST

This skill MUST be executed **step by step, one step at a time**. The AI model is FORBIDDEN from:

- ❌ Skipping any step
- ❌ Combining multiple steps into a single response
- ❌ Proceeding to the next step without the user's explicit confirmation
- ❌ Assuming the user has completed a step without asking for evidence/output
- ❌ Jumping ahead to later steps
- ❌ Shortcutting the process
- ❌ Asking questions in plain text instead of using AskUserQuestion
- ❌ Telling the user to "go search for X yourself"
- ❌ Skipping the edit_content.py editing cycle at any marked touch point

**Required behavior for EVERY step:**

1. **ANNOUNCE** the step number and name clearly
2. **EXPLAIN** what this step accomplishes and why it matters (cite the book chapter)
3. **USE AskUserQuestion** for EVERY question to the user
4. **WAIT** for the user's response before continuing
5. **VERIFY** the user's output meets the step's completion criteria
6. **CONFIRM** with the user before moving to the next step

---

## 🖱️ MANDATORY: AskUserQuestion Usage Rules

1. **Decision questions**: `multiSelect: false`, 2–4 clear options
2. **Preference questions**: `multiSelect: true`
3. **Open-ended responses**: Include "I'll type my answer" option
4. **Confirmation gates**: "Yes, proceed" + "Not yet"

Group up to 4 related questions per call.

---

## 📝 MANDATORY: Interactive Content Editing Protocol (v1.4.1)

**CRITICAL**: At 8 key writing touch points, the user must edit content directly before the skill proceeds.

### Editing cycle:

```
1. AI writes/assembles content
2. AI saves content to editing/[step]_[title].md in the workspace
3. AI prompts: "✏️ Interactive Edit — [section name] — File: editing/[name].md"
4. User opens, edits, saves (directly or via: python3 edit_content.py)
5. AI Reads the modified file
6. AI continues with user's revised content
```

### ⛔ Eight Editing Touch Points:

| TP | Step | Content | File |
|----|------|---------|------|
| TP-1 | 2.12 | Topic statement draft | `editing/topic_statement.md` |
| TP-2 | 5.B5 | **Detailed outline** | `editing/outline.md` |
| TP-3 | 5.C | Thematic section 1 | `editing/section_1.md` |
| TP-4 | 5.C | Thematic section 2 | `editing/section_2.md` |
| TP-5 | 5.C | Cross-theme synthesis | `editing/cross_theme.md` |
| TP-6 | 5.C | Conclusion | `editing/conclusion.md` |
| TP-7 | 5.C | Introduction | `editing/introduction.md` |
| TP-8 | 6.C | Title candidates (3 versions) | `editing/title_candidates.md` |

After each edit, the AI MUST Read the file back and adapt all subsequent content.

### Standard editing prompt:

> ✏️ **Interactive Edit — [Section Name]**
>
> I've saved the draft to `editing/[file].md`. Edit as needed:
> - **Direct**: Open the file on your computer, edit, save, tell me when done.
> - **GUI**: `python3 edit_content.py --title "[Title]" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/[file].md"`
>
> I'll read your revised version and continue.

---

## 🔍 MANDATORY: AI-Led Literature Search Protocol

The AI performs ALL literature searches (Steps 2.3, 2.7, 2.8, 2.9, 2.10, 5.A2).

Two search methods are available:

### Option A: WebSearch (default)
Standard web search via the WebSearch/WebFetch tools. Works for any topic without configuration.

### Option B: Multi-Source API Search (recommended)
Uses `sci_lib/sci_search.py` to search arXiv, PubMed, and Web of Science (if WOS_API_KEY is set) simultaneously. Results include journal impact factors, JCR partitioning, and times-cited counts — providing richer context for literature selection.

AI should offer the user both options via AskUserQuestion at the first search opportunity (Step 2.3). If the user has no preference, select Option B (API Search) for academic rigor.

**Protocol**: Confirm parameters (AskUserQuestion) → Execute search (WebSearch or sci_search.py) → Present 5-10 results with real URLs via AskUserQuestion → WebFetch/API details → Record selections.

---

## Trigger Conditions

**Triggers**: `/literature-review`, write literature review, lit review, literature review writing, systematic review

---

## Workflow Overview

```
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6 → Step 7 → Step 8
```

| Step | Name | Key Output | Editing |
|------|------|------------|---------|
| 1 | Determine Review Type | Review type selected | — |
| 2 | Select & Refine Topic | Topic statement + literature pool | TP-1 |
| 3 | Screen & Import to Zotero | Screening table + Zotero library | — |
| 4 | Deep Analysis | Analysis tables + summaries | — |
| 5 | Synthesize & Write Draft | Complete first draft | TP-2~7 |
| 6 | Edit & Finalize | Final manuscript | TP-8 |
| 7 | Peer Review & Selective Revision | Multi-perspective review + collectively revised manuscript | — |
| 8 | Citation Verification & Reference Mgmt | Verified references + Zotero collection + .docx + HTML report | — |

---

## Step 1: Determine the Review Type

> **Book Reference**: Chapter 1

### Type 1: Term Paper / Course-Assigned Review
- Length: 10–20 pages | Literature: 10–30 articles | Audience: Instructor

### Type 2: Thesis / Dissertation Literature Review
- Length: Full chapter(s) | Literature: 50–100+ articles | Audience: Committee & examiners

### Type 3: Journal Article Literature Review
- Length: 25–50 pages | Audience: Academic peers

| Dimension | Term Paper | Thesis | Journal |
|-----------|-----------|--------|---------|
| Purpose | Demonstrate mastery | Justify research | Provide synthesis |
| Depth | Moderate | Deep | Very deep |
| Originality | Low | Moderate | High |
| Audience | Instructor | Advisors & examiners | Academic peers |

**1.2** — Use AskUserQuestion:
```
AskUserQuestion({ questions: [{ question: "Which type of literature review are you writing?", header: "Review Type", options: [
  {label: "Term Paper / Course Review", description: "10-20 pages, 10-30 articles."},
  {label: "Thesis / Dissertation Review", description: "Full chapter(s), 50-100+ articles."},
  {label: "Journal Article Review", description: "25-50 pages. Original, critical synthesis."}
], multiSelect: false }] })
```

### Step 1 Completion Gate — AskUserQuestion Yes/No.

---

## Step 2: Select and Refine Your Topic

> **Book Reference**: Chapter 3 (14 steps)

⛔ AI performs all literature searches.

### Phase A: General Direction (Steps 1–3)

**Step 1** — AskUserQuestion for general topic + motivation.
**Step 2** — AskUserQuestion for database access (multiSelect: institutional, Google Scholar, PubMed, no preference).
**Step 3** — AskUserQuestion for keywords. Offer the user two search options:
   - **Option A: WebSearch** — AI performs web-based search
   - **Option B: Multi-Source API Search (recommended)** — Uses `sci_lib/sci_search.py` to search arXiv + PubMed + Web of Science simultaneously with journal metrics

   If Option B is chosen, execute via Bash:
   ```bash
   python3 sci_lib/sci_search.py "<keywords>" --source all --limit 10
   ```
   If WOS_API_KEY is not set, the tool skips Web of Science gracefully.

   Present 8-10 papers with real URLs, impact factors, and JCR rankings via AskUserQuestion.

### Phase B: Adjust Scope (Steps 4–6)

Narrow (>500 results): AskUserQuestion multiSelect (population, time frame, method, context, variable). Expand (<20): AI broadens search. AskUserQuestion for unpublished literature.

### Phase C: Key Resources (Steps 7–10)

**Step 7** — AI searches recent papers → AskUserQuestion for focus areas.
**Step 8** — AI searches theoretical frameworks → AskUserQuestion.
**Step 9** — AI finds existing reviews → AskUserQuestion for differentiation.
**Step 10** — AI identifies landmark studies → AskUserQuestion.

### Phase D: Topic Statement (Steps 11–14)

**Step 11** — AI summarizes literature pool → AskUserQuestion.

**Step 12** — ⛔ **TP-1: Interactive Edit — Topic Statement**

Template: *"This review examines [topic/focus], focusing on [scope]. It aims to [purpose], which is significant because [reason]."*

After the draft is assembled, AI writes to `editing/topic_statement.md` and MUST prompt:

> ✏️ **Interactive Edit — Topic Statement**
> File: `editing/topic_statement.md`
> WSL: `python3 edit_content.py --title "Topic Statement" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/topic_statement.md"`
> Edit wording, scope, or emphasis. I'll read your revised version and continue.

After user confirms, Read the file back and use revised statement.

**Step 13** — AskUserQuestion for refinement (multiSelect: focus, feasibility, adequacy, value).
**Step 14** — AskUserQuestion for advisor feedback.

### Step 2 Completion Gate — AskUserQuestion Yes/No.

---

## Step 3: Screen Literature, Build Tables & Import to Zotero

> **Book Reference**: Chapters 4 + 8

### Phase A: Skim and Screen

**Step 1** — 7-step skim protocol. AI offers WebFetch summaries. AskUserQuestion for counts.
**Step 2** — AskUserQuestion for categorization dimension.

### Phase B: Check for Gaps

**Step 3** — AskUserQuestion for gap types. AI runs supplementary searches if needed.

### Phase C: Screening Summary Table

**Step 4** — 11-column template. AskUserQuestion for status.

### Phase D: Import into Zotero

**Steps 5-6** — Collection structure, import, consistency.

When importing articles into Zotero (requires ZOTERO_API_KEY and ZOTERO_USER_ID environment variables):

1. **For each article**, add it by DOI or PMID using `sci_lib/zotero.py`:
   ```bash
   # Add by DOI (most common)
   python3 sci_lib/zotero.py add-doi "10.xxxx/xxxxx"

   # Add by PubMed ID (if DOI is unavailable)
   python3 sci_lib/zotero.py add-pmid "12345678"
   ```

2. **Organize into collections**:
   ```bash
   python3 sci_lib/zotero.py collection-create "[Collection Name]"
   ```

3. **Verify the import**:
   ```bash
   python3 sci_lib/zotero.py items --limit 50
   ```

4. **Check for PDF attachments** (optional):
   ```bash
   python3 sci_lib/zotero.py check-pdfs
   python3 sci_lib/zotero.py fetch-pdfs
   ```

5. **AskUserQuestion** to confirm completeness before proceeding.

### Phase E: Organization Check

**Step 7** — 7-item readiness. AskUserQuestion.

### Step 3 Completion Gate — AskUserQuestion Yes/No.

---

## Step 4: Deep Analysis of Literature

> **Book Reference**: Chapters 5–8

### Phase A: Three Analytical Tables
Definition Table → Methods Table → Results Summary Table. AskUserQuestion at each.

### Phase B: Quantitative Analysis
Design/Causality/Measurement/Analysis checklist. Cross-study AskUserQuestion.

### Phase C: Qualitative Analysis
Paradigm/Data/Rigor/Findings. ⛔ No quantitative criteria for qualitative studies.

### Phase D: Integrate by Group
Integration Tables + 300-500 word summaries. AskUserQuestion.

### Step 4 Completion Gate — AskUserQuestion Yes/No.

---

## Step 5: Synthesize Trends, Write Draft & Develop Coherent Essay

> **Book Reference**: Chapters 9–11
> **Writing Reference**: [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/)

### Phase A: Journal-Specific (Journal Reviews Only)

**A1** — AskUserQuestion for target journal.
**A2** — AI searches journal for reviews → AskUserQuestion.
**A3** — 14-dimension style analysis.

### Phase B: Build Outline (Chapter 9)

**B1** — AskUserQuestion for trends (multiSelect: temporal, methodological, theoretical, population).
**B2** — AskUserQuestion for patterns (multiSelect: consistent, contradictory, method-finding, theory-finding, cross-category).
**B3** — Gap ranking.
**B4** — AskUserQuestion for organizational scheme (thematic/chronological/methodological/theoretical/hybrid).
**B5** — Build detailed outline — ⛔ **TP-2: Interactive Edit — Outline**

After assembling the outline (section titles, sub-themes, key points per section, thesis statement position), the AI writes it to `editing/outline.md` and MUST prompt:

> ✏️ **Interactive Edit — Outline**
>
> I've drafted the review outline based on your chosen organizational scheme and identified themes. This is the blueprint for the entire review — getting it right now saves massive rewriting later.
>
> **File**: `editing/outline.md`
> **WSL**: `python3 edit_content.py --title "Review Outline" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/outline.md"`
>
> Check: section order, sub-theme groupings, whether any important themes are missing, thesis statement placement. Rearrange, add, or remove sections as needed.

After user confirms, Read the file back. The revised outline becomes the mandatory structure for all subsequent writing.

**⛔ CRITICAL**: Do NOT start writing any draft section until the outline has been edited and approved.

### Phase C: Write First Draft (Chapter 10) — ⛔ 5 EDITING TOUCH POINTS

**CRITICAL RULE:**
> ⛔ FORBIDDEN: "Smith (2020) found..."
> ✅ CORRECT: "Regarding [Theme X], research consistently indicates [finding]..."

Writing follows the approved outline. Order: Thematic sections → Cross-theme → Conclusion → Introduction last.

After EACH section, AI writes to file, prompts user to edit, reads back revised version:

---

**TP-3 — Thematic Section 1**:
> ✏️ File: `editing/section_1.md` | WSL: `python3 edit_content.py --title "Section 1" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/section_1.md"`

**TP-4 — Thematic Section 2** (and 3+):
> ✏️ File: `editing/section_2.md` | Same pattern.

**TP-5 — Cross-Theme Synthesis**:
> ✏️ File: `editing/cross_theme.md` | WSL: `python3 edit_content.py --title "Cross-Theme" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/cross_theme.md"`

**TP-6 — Conclusion**:
> ✏️ File: `editing/conclusion.md` | WSL: `python3 edit_content.py --title "Conclusion" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/conclusion.md"`

**TP-7 — Introduction** (written last):
> ✏️ File: `editing/introduction.md` | WSL: `python3 edit_content.py --title "Introduction" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/introduction.md"`

---

After all sections edited, AskUserQuestion for synthesis check.

### Phase D: Coherent Essay (Chapter 11 — 9 Guidelines)

Walk through each guideline. Guideline 3 (Thesis) is most critical.

### Phase E: Process Recording

AskUserQuestion.

### Step 5 Completion Gate — AskUserQuestion Yes/No.

---

## Step 6: Edit, Finalize & Output

> **Book Reference**: Chapters 12–13 + Appendix A

### Phase A: Self-Editing Checklist

Read entire manuscript without marking. Walk through 48 items (5 dimensions) via AskUserQuestion.

### Phase B: Edit and Revise

Three rounds: Macro → Meso → Micro. AskUserQuestion.

### Phase C: Refine Final Title — ⛔ TP-8

> ✏️ **Interactive Edit — Title Candidates**
> File: `editing/title_candidates.md`
> WSL: `python3 edit_content.py --title "Title Candidates" --file "/mnt/c/Users/zdj/Desktop/research/溶瘤病毒综述/editing/title_candidates.md"`
> 3 candidates drafted. Edit, merge, or rewrite. I'll use your final choice.

Run 7-item title checklist after.

### Phase D: Format References

5-step Zotero reference formatting. AskUserQuestion.

### Phase E: Output

AskUserQuestion for format (Word/LaTeX/Both).

### Step 6 Completion Gate — AskUserQuestion Yes/No.

---

## Step 7: Peer Review & Selective Revision

> **New in v1.5.0**: After completing the final manuscript, this step automatically invokes the `academic-paper-reviewer` skill to conduct a multi-perspective peer review, lists every reviewer comment one by one for your selection, and applies all accepted changes collectively.

**Rationale** (Galván & Galván, Ch. 12): "Seek feedback before finalizing" — automated peer review provides systematic, multi-perspective feedback that catches weaknesses you may have overlooked.

### Phase A: Assemble Complete Manuscript

1. **Read the final edited versions** of all manuscript sections:
   - Title candidates file → extract your final chosen title
   - `editing/introduction.md`
   - `editing/section_1.md`
   - `editing/section_2.md` (and `section_3.md`, etc. if they exist)
   - `editing/cross_theme.md`
   - `editing/conclusion.md`
   - Reference list (from Step 6 Phase D)

2. **Compile** the complete manuscript into a single file: `editing/manuscript_draft.md`
   - Full title at top
   - All sections in order
   - References at the end

3. **AskUserQuestion** to confirm the assembled manuscript:
   ```json
   {
     question: "I've assembled the complete manuscript from your edited sections. The full draft is saved at `editing/manuscript_draft.md`. Shall we proceed to automated peer review?",
     header: "Manuscript Ready",
     options: [
       { label: "Yes, proceed to peer review", description: "Launch multi-perspective peer review via Academic Research Skills." },
       { label: "Let me check first", description: "I'll review the assembled draft before continuing." },
       { label: "Skip peer review", description: "Proceed directly to final output without review." }
     ],
     multiSelect: false
   }
   ```
   - If "Let me check first": prompt user to edit `editing/manuscript_draft.md`, then Read the file back.
   - If "Skip peer review": jump to Phase E (Final Output).

### Phase B: Launch Multi-Perspective Peer Review

1. **Invoke the Academic Paper Reviewer** by spawning an Agent with the manuscript:
   ```
   Agent({
     subagent_type: "general-purpose",
     description: "Academic peer review on manuscript",
     prompt: "You MUST load the academic-paper-reviewer skill via the Skill tool. Review the manuscript at [workspace_path]/editing/manuscript_draft.md using the 'full' mode. Simulate all 5 reviewer personas (Editor-in-Chief, 3 Peer Reviewers, Devil's Advocate). For EACH reviewer, produce individual atomic comments (one discrete issue per item) with severity labels (major/minor/typographical). Return ALL comments as a structured JSON array with fields: reviewer_name, comment_number, comment_text, severity. Do NOT skip or summarize any reviewer."
   })
   ```

2. **Wait** for the Agent to complete and return the structured review data.

3. **Verify** that all 5 reviewer perspectives were generated. If a reviewer is missing, re-invoke with an explicit instruction to include them.

### Phase C: Present Comments One by One

⛔ **CRITICAL**: Process comments strictly in order — one reviewer at a time, one comment at a time. Do NOT batch, skip, or summarize.

1. For EACH reviewer (in fixed order: Editor-in-Chief → Peer Reviewer 1 → Peer Reviewer 2 → Peer Reviewer 3 → Devil's Advocate):

2. **Announce** the reviewer header clearly:
   > `--- Reviewer [N]: [Name] ---`

3. For EACH individual comment from that reviewer:

   **Present** the full comment text and use AskUserQuestion:
   ```json
   {
     question: "**Reviewer [Name] — Comment #[N]**\nSeverity: [major/minor/typo]\n\n\"[Full comment text]\"\n\nDo you accept this suggestion?",
     header: "Accept Comment?",
     options: [
       { label: "✅ Accept", description: "Include this change in the collective revision batch." },
       { label: "❌ Reject", description: "Do not apply this suggestion." },
       { label: "✏️ Modify", description: "Accept with adjustments (I'll describe the modification)." }
     ],
     multiSelect: false
   }
   ```

4. **If "✏️ Modify"**: Ask the user to describe their modification. Record the modified version alongside the original.

5. **Record** every decision in a running decision log table with columns: Reviewer | # | Comment Summary | Decision | Modified Version (if applicable).

⛔ **STRICT RULES:**
- Process ONE comment per AskUserQuestion call. Never bundle multiple comments.
- Preserve the exact reviewer order listed above.
- Do NOT reorder, merge, or split comments.
- Do NOT let the Devil's Advocate's comments be presented differently — same format, same decision options.

### Phase D: Apply Accepted Changes Collectively

After ALL comments across ALL reviewers have been processed:

1. **Compile** the decision log into three lists:
   - **Accepted** (including Modified versions)
   - **Rejected**
   - **Total**

2. **Present a summary table** to the user:
   ```
   📋 Review Summary
   ─────────────────────────────────────────
   Total comments received:     [N]
   ✅ Accepted:                 [N]
   ❌ Rejected:                 [N]
   ✏️ Accepted (modified):      [N]
   ─────────────────────────────────────────
   ```

3. **Apply all accepted and modified changes** to the manuscript at once. Save the result to `editing/manuscript_revised.md`.

4. **AskUserQuestion** to confirm satisfaction:
   ```json
   {
     question: "All accepted changes have been applied collectively. The revised manuscript is at `editing/manuscript_revised.md`. Are you satisfied with the result?",
     header: "Revision Complete",
     options: [
       { label: "Yes, proceed to final output", description: "Move to final formatting and export." },
       { label: "Let me make additional manual edits", description: "I'll edit the revised draft further." },
       { label: "Request re-review", description: "Send the revised manuscript for a second round of peer review." }
     ],
     multiSelect: false
   }
   ```
   - If "Let me make additional manual edits": prompt user to edit `editing/manuscript_revised.md`, Read back, then proceed.
   - If "Request re-review": loop back to Phase B with the revised manuscript.

### Phase E: Final Output

AskUserQuestion for output format (Word/LaTeX/Both/PDF). After output, provide the final file path.

### Step 7 Completion Gate — AskUserQuestion Yes/No.

---

## Step 8: Citation Verification & Reference Management

> **New in v2.0.0**: After peer review and revision, this step analyzes citation integrity, searches LitSense (NCBI) for missing references, verifies existing citations, imports to Zotero, formats the article per journal style as a Word (.docx) document, and generates an HTML verification report with DOI links for human review.

**⛔ SUPREME RULE**: All citations MUST be from real PubMed or Web of Science indexed literature. Fabrication of any reference is strictly forbidden.

### Phase A: Load Manuscript & Classify Statements

1. **Read the revised manuscript** from `editing/manuscript_revised.md`.
2. **Classify every sentence** into three categories:
   - **Cited** — contains a citation marker (e.g., `(1-3)`, `(Author, Year)`)
   - **Needs Citation** — makes a factual/scientific claim without any citation
   - **Structural** — transitions, framework, author's own synthesis
3. **Present** two working lists to the user:
   - **List A (Uncited Claims)**: factual statements needing references
   - **List B (Existing Citations)**: all detected citation instances to verify
4. **AskUserQuestion** to confirm both lists. Allow user to add/remove items.

### Phase B: Search LitSense for Uncited Statements

For EACH statement in List A:

1. **Extract** 8–15 key terms from the claim.
2. **Search PubMed/LitSense** via WebSearch/WebFetch to find real supporting references.
3. **Present** up to 5 candidate references (with title, authors, year, journal, PMID, DOI).
4. **AskUserQuestion** for selection (Accept / Reject / Modify / Search again).
5. **Record** the decision. If none found, mark as "⚠️ unchecked — no PubMed match."

### Phase C: Verify Existing Citations

For a representative sample of List B (or all, if user chooses):

1. **Extract claim + cited reference** for each citation instance.
2. **Search PubMed/LitSense** to confirm the cited paper supports the claim.
3. **Classify**: ✅ Confirmed / ⚠️ Questionable / ❌ Not Found.
4. **AskUserQuestion** for action (Keep / Flag / Replace / Remove).
5. **Record** all results. Flag any citation that cannot be verified on PubMed/WoS.

### Phase D: Import to Zotero

1. **Create a Zotero collection** named after the article title:
   ```bash
   python3 sci_lib/zotero.py collection-create "[Article Title]"
   ```
   Note the returned collection key (e.g., `ABC123`).

2. **Compile master reference list** (existing + newly added refs, deduplicated by DOI/PMID).

3. **Import each reference** via DOI or PMID:
   ```bash
   # Add each reference to the specified collection
   python3 sci_lib/zotero.py add-doi "10.xxxx/xxxxx" --collection "ABC123"

   # Or add by PubMed ID
   python3 sci_lib/zotero.py add-pmid "12345678"
   ```

   For books or book chapters, use ISBN:
   ```bash
   python3 sci_lib/zotero.py add-isbn "978-xxxx"
   ```

4. **Verify import**:
   ```bash
   python3 sci_lib/zotero.py items --limit 50
   ```

5. **AskUserQuestion** to confirm the import is complete.

6. **Optional**: Search for missing DOIs or fetch open-access PDFs:
   ```bash
   python3 sci_lib/zotero.py find-dois
   python3 sci_lib/zotero.py fetch-pdfs
   ```

### Phase E: Format & Export as Word (.docx)

1. **Detect target journal style** from the manuscript (APA, Vancouver, GB/T 7714, IEEE, etc.).
2. **Insert all in-text citations** — both newly added (Phase B) and existing verified ones.
3. **Format reference list** per the detected style, sorted correctly.
4. **AskUserQuestion** to confirm the formatting.
5. **Generate .docx** using python-docx:
   ```
   python3 -c "from docx import Document; doc=Document(); ..."
   ```
   Include: centered title, section headings, body text (Times New Roman 12pt), page break before references.
6. Save to `editing/formatted_article.docx`.

### Phase F: Generate HTML Verification Report

1. **Build** a structured dataset with fields: Statement | Section | Status | Citation | Reference | DOI.
2. **Generate** a standalone HTML file saved to `editing/citation_verification_report.html` with:
   - Summary statistics cards (Verified/Newly Added/Corrected/Total)
   - Color-coded statement-to-reference mapping table (🟢 Verified / 🟡 Newly Added / 🔴 Corrected)
   - Clickable DOI links opening in new tabs
   - Deliverables listing
3. **AskUserQuestion** for final confirmation and output preferences.

### Step 8 Completion Gate — AskUserQuestion Yes/No.

## Quick Reference: 14 Key Principles

1. **Broad to narrow** — start wide, iteratively focus (Ch. 3)
2. **Skim before you read** — structural preview (Ch. 4)
3. **Use structured tables** (Ch. 5)
4. **Different criteria for quant vs. qual** (Ch. 6–7)
5. **Integrate by group before writing** (Ch. 8)
6. **Build an outline first** (Ch. 9)
7. **Synthesize, don't annotate** (Ch. 10–11)
8. **Have a thesis statement** (Ch. 11)
9. **Multi-round editing** (Ch. 12)
10. **Zotero throughout** (Ch. 4, 13)
11. **Use the Manchester Phrasebank**
12. **Seek feedback before finalizing** (Ch. 12)
13. **Use automated peer review** — multi-perspective review with selective revision (v1.5.0)
14. **Verify every citation** — LitSense search, Zotero import, .docx export, HTML report (v2.0.0)

---

> 🎉 v2.0.0: Step 7 — Peer Review & Selective Revision + Step 8 — Citation Verification & Reference Management. After peer review, analyzes citation integrity via LitSense, imports to Zotero, exports formatted .docx, and generates HTML verification report with DOI links.
> 🔍 AI performs all literature searches via WebSearch/WebFetch with real URLs.
> 🖱️ All decisions use AskUserQuestion visual interface.
> 🔴 SUPREME RULE: All citations must be from real PubMed/Web of Science literature — fabrication strictly forbidden.
