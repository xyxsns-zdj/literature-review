# Changelog

All notable changes to the `literature_review` skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] — 2026-05-11

### Added

- **sci_lib/ subdirectory** with two powerful Python scripts:
  - `sci_lib/sci_search.py` — multi-source academic paper search tool (arXiv API, PubMed E-utilities, Web of Science Starter API). Returns results with journal impact factors, JCR partitioning, and times-cited counts. Pure stdlib Python, no pip dependencies required.
  - `sci_lib/zotero.py` — full Zotero Web API v3 CLI with 14 commands: items, search, get, collections, collection-create, collection-add, tags, children, add-doi (with `--collection` flag), add-isbn, add-pmid, check-pdfs, crossref, find-dois, fetch-pdfs. Requires ZOTERO_API_KEY and ZOTERO_USER_ID.
  - `sci_lib/journal_db.json` — journal metrics database with IF, JCR, and CAS partitioning for 17 journals.
  - `sci_lib/__init__.py` — package marker.

- **Environment Variables section** in SKILL.md documenting WOS_API_KEY, ZOTERO_API_KEY, ZOTERO_USER_ID, and ZOTERO_GROUP_ID.

### Changed

- **SKILL.md frontmatter**: Updated `ai_capabilities` and `integrates_with` to include sci_lib scripts. Bumped version to 2.1.0.
- **AI-Led Literature Search Protocol**: Now offers two search methods — WebSearch (default) and Multi-Source API Search via sci_search.py.
- **Step 2 Phase A Step 3**: Added option to use `sci_lib/sci_search.py` for multi-source API search with Bash command template.
- **Step 3 Phase D (Zotero Import)**: Replaced abstract placeholder with concrete `sci_lib/zotero.py` CLI commands.
- **Step 8 Phase D (Zotero Import)**: Replaced abstract `zot` commands with real `sci_lib/zotero.py` commands including `--collection` flag.
- **_meta.json**: Version bumped to 2.1.0. Added capabilities list and scripts references.
- **upload_to_github.bat**: Added `sci_lib/` to git add path.

### Fixed

- **journal_db.json path**: sci_search.py now correctly resolves JOURNAL_DB_PATH to sibling journal_db.json inside sci_lib/.

### Technical Notes
- Both scripts are pure Python 3 stdlib — no pip install needed.
- Cross-platform (Windows, macOS, Linux).
- arXiv and PubMed work without any API key; Web of Science requires WOS_API_KEY.

---

## [1.1.0] — 2026-05-08

### ⛔ Major Change — Strict Sequential Execution Protocol

**Rationale**: During dogfooding of v1.0.0 on a full journal article review (oncolytic viruses + cancer immunotherapy for *Journal of Translational Medicine*), the AI model was observed to skip steps, combine multiple steps into single responses, and proceed without user confirmation. The user explicitly requested: "要严格按照skills的步骤执行" (must strictly follow the skill's step-by-step execution). This feedback revealed that the original skill's permissive structure — which presented all steps as a reference guide rather than an enforced workflow — allowed the model to bypass the sequential design.

### Added

- **STRICT EXECUTION PROTOCOL section** at the top of SKILL.md (before Trigger Conditions), with explicit forbidden behaviors:
  - ❌ Skipping any step
  - ❌ Combining multiple steps into a single response  
  - ❌ Proceeding without user confirmation
  - ❌ Assuming the user has completed a step without evidence
  - ❌ Jumping ahead to later steps
  - ❌ Shortcutting because "the user seems experienced"
- **Per-step required behavior checklist**: ANNOUNCE → EXPLAIN → ASK → WAIT → VERIFY → CONFIRM
- **Step-by-step completion gates** at every transition point (6 gates total), each containing:
  - ✅ Checklist of concrete outputs expected from that step
  - ➡️ Explicit prompt asking user to confirm readiness for next step
- **Anti-bypass protocol**: If user says "skip this" or "already did this," the model must politely insist on reviewing existing work before proceeding
- `execution_mode: strict_sequential` metadata field

### Changed

- Reorganized the skill preamble to place execution protocol BEFORE trigger conditions, ensuring it's read first
- Enhanced trigger conditions to include the `/literature_review` slash command as primary trigger
- Step 5 Phase A now explicitly gated: only executes for Journal reviews, skips for other types
- All writing instruction sections now reference specific Manchester Phrasebank URLs (instead of general mention)

### Fixed

- Model tendency to jump directly to writing (Steps 5-6) without completing analysis (Steps 3-4)
- Missing per-step verification that prevents proceeding with incomplete work

---

## [1.0.0] — 2026-05-07

### Added

- Initial release of the `literature_review` skill
- Complete 6-step literature review workflow based on Galván & Galván (2017), *Writing Literature Reviews* (7th ed.)
- Coverage of all 13 chapters + Appendix A
- Three review types: Term Paper, Thesis, Journal Article
- **Step 1**: Review Type Determination (Chapter 1)
- **Step 2**: Topic Selection and Refinement — 14 sub-steps in 4 phases (Chapter 3)
- **Step 3**: Literature Screening — skimming protocol, grouping, gap analysis, screening table, Zotero import with 7-collection structure (Chapters 4, 8)
- **Step 4**: Deep Analysis — three analytical tables (Definition, Methods, Results), quantitative/qualitative specialized analysis, integration by group (Chapters 5-8)
- **Step 5**: Synthesis and Writing — journal style analysis (14 dimensions), trend/pattern/gap identification, 5 organizational schemes, Manchester Phrasebank integration, 9 coherence guidelines (Chapters 9-11)
- **Step 6**: Editing and Output — 48-item self-editing checklist (Appendix A), 3-round editing, 4 title structures, Zotero reference formatting, Word + LaTeX output (Chapters 12-13)
- 12 Key Principles quick reference
- Support for Chinese-language academic users (triggers: 文献综述, 综述写作)
- Output targets: Word (.docx), LaTeX (.tex + .bib), and PDF

### References

- **Primary**: Galván, J. L., & Galván, M. C. (2017). *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th ed.). Routledge.
- **Writing Aid**: University of Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/)

---

## Versioning Policy

- **MAJOR** (X.0.0): Structural changes to the workflow (steps added/removed/reordered), new execution protocols
- **MINOR** (0.X.0): New features, enhanced guidance, new reference material, improved prompts within existing steps
- **PATCH** (0.0.X): Typo fixes, link updates, minor clarifications, formatting improvements

---

## Planned for Future Versions

| Version | Planned Changes |
|---------|----------------|
| 1.2.0 | Add systematic review mode (PRISMA integration); add scoping review mode; add AI-assisted literature search helpers |
| 1.3.0 | Add bilingual (Chinese/English) workflow support; CNKI/Wanfang database integration guidance |
| 2.0.0 | Integration with `academic-paper-reviewer` skill for pre-submission self-review; integration with `academic-paper` skill for full paper pipeline |
