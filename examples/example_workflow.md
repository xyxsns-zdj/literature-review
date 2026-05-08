# Example: Full Literature Review Workflow

## Dogfooding Case Study: Oncolytic Viruses and Cancer Immunotherapy Review

This document demonstrates the complete 6-step workflow as applied to a real journal article review targeting the *Journal of Translational Medicine*. All outputs shown are actual deliverables from the dogfooding process.

---

### Step 1: Determine Review Type

**User**: "写一篇关于溶瘤病毒和肿瘤免疫治疗的综述"

**Selection**: **Type 3 — Journal Article Review**
- Target: *Journal of Translational Medicine* (Springer Nature / BMC)
- Language: English
- Audience: Translational oncology researchers

**Implications**: Requires original critical synthesis, clear thesis statement, Vancouver reference style, Declarations section mandatory.

---

### Step 2: Select & Refine Topic (14 Sub-steps)

**Phase A — General Direction:**
- Databases: PubMed + Web of Science + Scopus
- Keywords split into 4 sub-topic blocks:
  1. Molecular mechanisms: oncolytic virus + immunogenic cell death + cGAS-STING + innate immunity
  2. Engineering: oncolytic virus + genetic engineering + targeted delivery + transgene arming
  3. Combination: oncolytic virus + immune checkpoint inhibitor + CAR-T + combination therapy
  4. Clinical: oncolytic virus + clinical trial + T-VEC + phase III

**Phase B — Scope Adjustment:**
- ~200–300 relevant articles across all 4 sub-topics
- Timeframe: 2015–2025, emphasis on 2020–2025
- Grey literature: Conference abstracts (ASCO, AACR) included for recent Phase III data

**Phase C — Key Resources:**
- Landmark studies: Andtbacka et al. (2015, T-VEC OPTiM), Ribas et al. (2017, T-VEC + pembrolizumab), Bommareddy et al. (2019, STING paradox)
- Core theorists: Kaufman HL, Bell JC, Harrington K, Gujar S, Kroemer G
- Existing reviews gap: Most recent J Transl Med reviews cover only single-organ (liver cancer, leptomeningeal metastasis); no comprehensive 4-domain review exists

**Phase D — Topic Statement:**
> "This review critically synthesizes recent advances in oncolytic virus-based cancer immunotherapy spanning molecular mechanisms (ICD, cGAS-STING, TME reprogramming), genetic engineering strategies, combination approaches (ICI, CAR-T), and clinical translation. By integrating mechanistic rationale with emerging clinical evidence including the recent Phase III successes of CG0070 and CAN-2409, this review aims to inform the rational design of next-generation OV immunotherapies for J Transl Med's translational oncology readership."

---

### Step 3: Screen Literature & Build Tables

**Screening Table**: [View CSV](computer://C:\Users\zdj\Desktop\research\溶瘤病毒综述\Literature_Screening_Table.csv)
- 42 core + supporting articles
- 5 thematic categories: Molecular Mechanisms, Engineering & Delivery, Combination Therapy, Clinical Translation, Cross-cutting
- 7 identified gaps ranked by priority

**Zotero Structure:**
```
📁 OV_Immunotherapy_Review
   ├── 01_Core_Articles
   ├── 02_Supporting_Articles
   ├── 03_Peripheral_Articles
   ├── 04_Excluded
   ├── 05_Reviews_and_Meta
   ├── 06_Theoretical
   └── 07_Grey_Literature
```

See [Step 3 Gap Analysis](computer://C:\Users\zdj\Desktop\research\溶瘤病毒综述\Step3_Gap_Analysis_and_Zotero_Structure.md).

---

### Step 4: Deep Analysis

**Three Analytical Tables**: [View](computer://C:\Users\zdj\Desktop\research\溶瘤病毒综述\Step4_Deep_Analysis_Tables.md)

**Key findings from analysis:**
- ICD definition consistency: High across literature (Galluzzi/Kroemer criteria universally adopted)
- STING role controversy: Beneficial (DePeaux 2024) vs. detrimental to replication (Bommareddy 2019) — context-dependent
- Methodological gap: 6/15 key studies are clinical trials, 9/15 preclinical; OV+CAR-T entirely preclinical
- Cross-category pattern: Recurring tension between antiviral and antitumor immunity across all domains

**Four thematic integration summaries** written (300–500 words each).

---

### Step 5: Synthesize & Write

**Journal Style Analysis (14 dimensions)**: [View](computer://C:\Users\zdj\Desktop\research\溶瘤病毒综述\Step5_Journal_Style_Analysis.md)

**Outline**: Hybrid thematic + translational arc
1. Introduction (funnel: known → unknown → objective + thesis)
2. Molecular Mechanisms (ICD, cGAS-STING, innate→adaptive, TME)
3. Engineering Strategies (platforms, targeting, arming, delivery)
4. Combination Immunotherapy (ICI, CAR-T, chemo/radio, triple)
5. Clinical Translation (approved, pipeline, biomarkers, challenges)
6. Conclusions (inverted funnel)

**Thesis**: "OVs function as multimodal immunotherapeutics — direct oncolytics, in situ vaccines, and TME conditioners — and their full potential will be realized through mechanistic understanding driving rational engineering and biomarker-guided combination strategies."

**Writing rule enforced**: Every paragraph organized by theme, cites multiple sources, starts with topic sentence — NOT author names.

---

### Step 6: Edit & Output

**48-item self-edit**: 42/48 passed; 4 items flagged for word processing stage (spell check, DOIs, formatting, declarations).

**3-round editing**: Macro (structure) → Meso (paragraphs) → Micro (sentences).

**Peer review**: Manuscript underwent 5-reviewer simulated peer review (EIC + methodology + domain + perspective + Devil's Advocate). Decision: Major Revision. All P0–P3 revisions implemented.

**Final manuscript**: ~8,000 words, 97 references, Vancouver format.

Review reports: [Peer_Review_Report.md](computer://C:\Users\zdj\Desktop\research\溶瘤病毒综述\Peer_Review_Report.md)

---

### Key Lessons from This Dogfooding Run

1. **Strict execution matters.** The initial attempt to skip/combine steps led to the v1.1.0 protocol enforcement.
2. **The 14-step topic refinement** (Step 2) paid off — identifying the 4-sub-domain structure early prevented scope creep.
3. **The screening table** (Step 3) was essential for tracking which articles had been analyzed when writing Section 5 (Clinical).
4. **The STING paradox** — identified in the cross-category pattern analysis (Step 4) — became one of the review's most distinctive contributions.
5. **Peer review before submission** (via academic-paper-reviewer skill) caught critical omissions (missing negative trials, absent search methodology, overstatements) that would have led to journal rejection.
