---
name: literature_review
description: "Complete 6-step literature review writing workflow based on Galván & Galván (2017). Strict step-by-step execution. AI performs literature searches via WebSearch/WebFetch, presents results with real URLs. Every user interaction uses AskUserQuestion. Interactive editing boxes at 8 key touch points (outline, topic, draft sections, title). Triggers on: /literature_review, write literature review, lit review, literature review writing, systematic review."
metadata:
  version: "1.4.1"
  last_updated: "2026-05-08"
  status: active
  based_on: "Galván, J. L., & Galván, M. C. (2017). Writing Literature Reviews (7th ed.). Routledge."
  writing_reference: "University of Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/)"
  task_type: guided
  execution_mode: strict_sequential
  ai_capabilities: "WebSearch, WebFetch, AskUserQuestion, edit_content.py"
---

# Literature Review Writing — Complete 6-Step Workflow

Based on **José L. Galván & Melisa C. Galván, *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th Edition, Routledge, 2017)**.

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

**Protocol**: Confirm parameters (AskUserQuestion) → Execute WebSearch → Present 5-10 results with real URLs (AskUserQuestion) → WebFetch details → Record selections.

---

## Trigger Conditions

**Triggers**: `/literature_review`, write literature review, lit review, literature review writing, systematic review

---

## Workflow Overview

```
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6
```

| Step | Name | Key Output | Editing |
|------|------|------------|---------|
| 1 | Determine Review Type | Review type selected | — |
| 2 | Select & Refine Topic | Topic statement + literature pool | TP-1 |
| 3 | Screen & Import to Zotero | Screening table + Zotero library | — |
| 4 | Deep Analysis | Analysis tables + summaries | — |
| 5 | Synthesize & Write Draft | Complete first draft | TP-2~7 |
| 6 | Edit & Finalize | Final manuscript | TP-8 |

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
**Step 3** — AskUserQuestion for keywords. AI runs WebSearch. Present 8 papers with real URLs via AskUserQuestion.

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

**Steps 5-6** — Collection structure, import, consistency. AskUserQuestion.

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

## Quick Reference: 12 Key Principles

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

---

> 🎉 v1.4.1: 8 interactive editing touch points (outline added). AI writes → user edits → AI adapts.
> 🔍 AI performs all literature searches via WebSearch/WebFetch with real URLs.
> 🖱️ All decisions use AskUserQuestion visual interface.
