---
name: "literature_review"
description: "Complete 6-step literature review workflow with STRICT step-by-step execution enforced. Based on Galván & Galván (2017). Command: /literature_review"
---

---
name: literature_review
description: "Complete 6-step literature review writing workflow based on Galván & Galván (2017). Strict step-by-step execution enforced. Each step must be completed and confirmed before proceeding. Triggers on: /literature_review, write literature review, lit review, literature review writing, systematic review."
metadata:
  version: "1.1.0"
  last_updated: "2026-05-08"
  status: active
  based_on: "Galván, J. L., & Galván, M. C. (2017). Writing Literature Reviews (7th ed.). Routledge."
  writing_reference: "University of Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/)"
  task_type: guided
  execution_mode: strict_sequential
---

# Literature Review Writing — Complete 6-Step Workflow

Based on **José L. Galván & Melisa C. Galván, *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th Edition, Routledge, 2017)**.

---

## TRIGGER CONDITIONS

**Triggers**: `/literature_review`, write literature review, literature review writing, lit review, systematic review, write a review, help with literature review

---

## ⛔ STRICT EXECUTION PROTOCOL — READ THIS FIRST

This skill MUST be executed **step by step, one step at a time**. The AI model is FORBIDDEN from:

- ❌ Skipping any step
- ❌ Combining multiple steps into a single response
- ❌ Proceeding to the next step without the user's explicit confirmation
- ❌ Assuming the user has completed a step without asking for evidence/output
- ❌ Jumping ahead to later steps (e.g., discussing writing before topic is confirmed)
- ❌ Shortcutting the process because "the user seems experienced"

**Required behavior for EVERY step:**

1. **ANNOUNCE** the step number and name clearly (e.g., "## Step 1: Determine the Review Type")
2. **EXPLAIN** what this step accomplishes and why it matters (cite the book chapter)
3. **ASK** the user the required questions for this step (one question at a time if multiple)
4. **WAIT** for the user's response before continuing within the step
5. **VERIFY** the user's output meets the step's completion criteria
6. **CONFIRM** with the user before moving to the next step: "Step X is complete. Shall we proceed to Step X+1?"

**Completion gate before each transition:**
> ✅ Step X is now complete. You should have: [list of concrete outputs].
> ➡️ Ready to proceed to Step X+1: [step name]?

**If the user says "skip this" or "I already did this":**
- Politely insist on reviewing their existing work: "I understand you've already done this. Could you share what you have so I can verify it meets the step's requirements before we move on?"

---

## WORKFLOW OVERVIEW

```
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6
  Type    Topic  Screen   Deep     Draft    Edit &
  Select  Refine &Zotero  Analyze  Write    Output
```

| Step | Name | Book Chapters | Key Output |
|------|------|---------------|------------|
| 1 | Determine Review Type | Ch. 1 | Review type selected |
| 2 | Select & Refine Topic | Ch. 3 | Refined topic statement (14 sub-steps) |
| 3 | Screen Literature & Import to Zotero | Ch. 4, 8 | Screening table + Zotero library |
| 4 | Deep Analysis of Literature | Ch. 5–8 | Analysis tables + Summaries per category |
| 5 | Synthesize & Write First Draft | Ch. 9–11 | Complete first draft + Coherence revision |
| 6 | Edit, Finalize & Output | Ch. 12–13, App. A | Final manuscript (Word + LaTeX) + References |

---

## STEP 1: DETERMINE THE REVIEW TYPE

> **Book Reference**: Chapter 1 — Writing Reviews of Academic Literature: An Overview

### Type 1: Term Paper / Course-Assigned Review
- Length: 10–20 pages | Literature: 10–30 articles | Audience: Instructor
- Purpose: Demonstrate ability to search, read, understand, and synthesize literature

### Type 2: Thesis / Dissertation Literature Review
- Length: Full chapter(s) | Literature: 50–100+ articles | Audience: Committee & examiners
- Purpose: Lay theoretical foundation; identify gaps justifying your study

### Type 3: Journal Article Literature Review
- Length: 25–50 pages | Literature: 60–200 articles | Audience: Academic peers
- Purpose: Provide original, critical synthesis; must have clear argument

### Step 1 Completion Gate:
> ✅ Step 1 is complete. You have selected: [Type A/B/C].
> ➡️ Ready to proceed to Step 2: Select and Refine Your Topic?

---

## STEP 2: SELECT AND REFINE YOUR TOPIC

> **Book Reference**: Chapter 3 — 14 sub-steps in 4 phases

### Phase A: Establish General Direction (Steps 1–3)
**Step 1** — Ask: "In 1–2 sentences, describe your general area of interest." Follow up on familiarity and motivation.
**Step 2** — Ask: "What databases does your institution provide?" (WoS, Scopus, PubMed, etc.)
**Step 3** — Ask: "What 3–5 keywords for an initial search?" Run one; report count and recurring themes. >500 = too broad; <20 = too narrow.

### Phase B: Adjust Scope (Steps 4–6)
**Step 4** — Narrow by population, timeframe, method, context, or variable if >200 results.
**Step 5** — Expand via broader synonyms, interdisciplinary search if <20–30 results.
**Step 6** — Consider unpublished studies; weigh publication bias reduction vs. no peer review.

### Phase C: Locate Key Resources (Steps 7–10)
**Step 7** — Start with current research, work backward. Browse 10–20 recent abstracts.
**Step 8** — Search for theoretical articles (add "theory," "framework," "model").
**Step 9** — Find existing reviews; differentiate your approach (<2–3yr = new angle; 5+yr = fill gap).
**Step 10** — Identify landmark studies (sort by citations) and core theorists (3–5 authors).

### Phase D: Formulate Topic Statement (Steps 11–14)
**Step 11** — Summarize: count, time span, 3–5 categories, over/under-represented areas.
**Step 12** — Write 2–4 sentence topic statement: focus, scope, purpose/significance.
**Step 13** — Refine: focused? feasible? enough literature? valuable beyond existing reviews?
**Step 14** — Seek advisor feedback before proceeding.

### Step 2 Completion Gate:
> ✅ Step 2 is complete. You should have: refined topic statement, preliminary literature list, understanding of core researchers/existing reviews/theoretical frameworks.
> ➡️ Ready to proceed to Step 3?

---

## STEP 3: SCREEN LITERATURE, BUILD TABLES & IMPORT TO ZOTERO

> **Book Reference**: Chapters 4 & 8

### Phase A: Skim and Preliminary Screening
**Step 1** — Quick-skim each article in order: Title → Abstract → Keywords → Intro end → Methods → Discussion → References. Classify as: Definitely Include / Possibly Include / Exclude. Report counts.
**Step 2** — Group retained articles by category (6 dimensions available). Report counts per category.

### Phase B: Check for Gaps
**Step 3** — Identify sparse categories, missing perspectives, population/context gaps, methodological monotony. Conduct targeted supplementary searches.

### Phase C: Build the Literature Screening Summary Table
**Step 4** — Create in Excel/Google Sheets with 11 columns: #, Author(s) (Year), Title, Study Type, Design/Method, Sample/Data, Key Variables, Main Findings, Theoretical Framework, Thematic Category, Relevance, Priority.

### Phase D: Import into Zotero
**Step 5** — Create Collection structure (7 folders), import via Browser Connector/DOI/RIS, add tags.
**Step 6** — Verify consistency: Zotero count = table count, categories map, PDFs linked.

### Phase E: Final Organization Check
**Step 7** — Verify: Zotero complete, table filled, PDFs linked, priorities set, categories clear, gaps flagged, excluded documented.

### Step 3 Completion Gate:
> ✅ Step 3 is complete. You should have: screened literature set, complete screening table, structured Zotero library with tags and priorities.
> ➡️ Ready to proceed to Step 4?

---

## STEP 4: DEEP ANALYSIS OF LITERATURE

> **Book Reference**: Chapters 5–8

### Phase A: Build Three Analytical Tables (Chapter 5)
**Table 1 — Definition Table**: Track how each study defines 3–5 core constructs (Author, Construct 1–3, Operationalization, Measurement).
**Table 2 — Methods Table**: Compare designs (Author, Design, Sample Size, Characteristics, Sampling, Data Collection, Analysis, Rigor).
**Table 3 — Results Summary**: Standardize findings (Author, Research Question, Main Findings [own words], Effect Size, Consistent with Hypothesis?, Author Limitations, Additional Limitations).

### Phase B: Analyze Quantitative Research (Chapter 6)
Evaluate: Design & Causality, Measurement (reliability, validity), Analysis (methods, assumptions, effect sizes + CIs, missing data, power). Cross-study summary: overall quality, effect size range, instrument patterns, population patterns, causal evidence.

### Phase C: Analyze Qualitative Research (Chapter 7)
Evaluate: Paradigm, Data Collection (sampling, saturation, triangulation), Analysis Rigor (coding, member checking, reflexivity), Findings Quality. **NEVER apply quantitative criteria to qualitative studies.**

### Phase D: Integrate by Group (Chapter 8)
Create Analysis Integration Tables per category. Identify cross-category patterns. Write 300–500 word Analysis Summary per category.

### Step 4 Completion Gate:
> ✅ Step 4 is complete. You should have: 3 analysis tables, quant/qual specialized analysis, integration tables, cross-category patterns, analysis summaries per category.
> ➡️ Ready to proceed to Step 5?

---

## STEP 5: SYNTHESIZE TRENDS, WRITE DRAFT & DEVELOP COHERENT ESSAY

> **Book Reference**: Chapters 9–11
> **Writing Reference**: Manchester Academic Phrasebank

### Phase A: Journal-Specific Preparation (Journal Reviews Only)
**A1** — Ask: "Which journal? (1–3 candidates)." **A2** — Find 3–5 recent review articles in target journal. **A3** — Analyze style across 14 dimensions; write 200–300 word style summary.

### Phase B: Build an Outline (Chapter 9)
**B1** — Identify trends (temporal, methodological, theoretical, population, publication, geographic). **B2** — Identify patterns (consistent, contradictory, method-finding, theory-finding, inter-category tensions). **B3** — Rank gaps by priority. **B4** — Choose organizational scheme (Thematic/Chronological/Methodological/Theoretical/Hybrid). **B5** — Build detailed outline.

### Phase C: Write the First Draft (Chapter 10)

> ⛔ **FORBIDDEN**: "Smith (2020) found... Jones (2019) reported..."
> ✅ **CORRECT**: "Regarding [Theme], research consistently indicates [finding]. Both Smith (2020) and Chen (2021) found... However, Jones (2019), using a different methodology, reached the opposite conclusion..."

Writing order: Most familiar category first → Other categories → Cross-theme synthesis → Conclusion → Introduction LAST.

### Phase D: Develop a Coherent Essay (Chapter 11 — 9 Guidelines)
1. Provide overview near beginning. 2. State what IS and IS NOT covered. 3. **State your thesis early** (MOST IMPORTANT). 4. Integrate into cohesive essay. 5. Use consistent subheadings. 6. Use transitions. 7. Consider discipline-by-discipline for interdisciplinary topics. 8. Write proper conclusion. 9. Check argument flow by reading aloud.

### Step 5 Completion Gate:
> ✅ Step 5 is complete. You should have: journal style analysis (if journal), trends/patterns/gaps, outline with thesis, complete first draft, coherence check results, process record.
> ➡️ Ready to proceed to Step 6?

---

## STEP 6: EDIT, FINALIZE & OUTPUT

> **Book Reference**: Chapters 12–13 + Appendix A (48-item checklist)

### Phase A: Comprehensive Self-Editing (48 items, 5 dimensions)
1. **Content & Synthesis** (10 items) 2. **Organization & Coherence** (10 items) 3. **Style & Language** (10 items) 4. **Citations & References** (8 items) 5. **Presentation** (7 items)

### Phase B: Three-Round Editing
Round 1 (Macro): Structure, logic, proportions. Round 2 (Meso): Paragraph topic sentences, evidence, transitions. Round 3 (Micro): Sentences, grammar, spelling.

### Phase C: Refine Final Title
4 title structures; rate on 6 criteria; generate 3 candidates; final checklist.

### Phase D: Format References via Zotero
Create Final_References Collection → verify 7 fields → set citation style → generate list → cross-check.

### Phase E: Output in Word and LaTeX
Word: heading styles, auto ToC, margins/spacing/font, Zotero references, spell check. LaTeX: Better BibTeX export, APA template, pdflatex→biber→pdflatex×2.

### Step 6 Completion Gate:
> ✅ Step 6 is complete. Your literature review is finished.
> 🎉 The full 6-step workflow is complete. All 13 chapters + Appendix A applied.

---

## QUICK REFERENCE: 12 KEY PRINCIPLES

1. **Broad to narrow** — start wide, iteratively focus (Ch. 3)
2. **Skim before you read** — structural preview (Ch. 4)
3. **Use structured tables** — analysis tools (Ch. 5)
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

> 🎉 This skill enforces the complete Galván & Galván (2017) workflow. All 13 chapters + Appendix A. Step-by-step execution is mandatory.

---

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-05-08 | ⛔ Strict sequential execution protocol added; completion gates at every step transition |
| 1.0.0 | 2026-05-07 | Initial release — complete 6-step Galván & Galván (2017) workflow |
