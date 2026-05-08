# Literature Review Writing Skill

A complete 6-step literature review writing workflow skill for Claude Code / Cowork mode, based on **José L. Galván & Melisa C. Galván, *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th Edition, Routledge, 2017)**.

## Overview

This skill enforces a strict, step-by-step execution of all 13 chapters + Appendix A from Galván & Galván (2017). It guides you from initial topic selection through final formatted output in Word and LaTeX, with Zotero integration for reference management.

### What It Covers

| Step | Name | Key Output |
|------|------|------------|
| 1 | Determine Review Type | Term paper / Thesis / Journal article selected |
| 2 | Select & Refine Topic | Refined topic statement (14 sub-steps) |
| 3 | Screen Literature | Screening summary table + Zotero library |
| 4 | Deep Analysis | Definition/Methods/Results tables + Analysis summaries |
| 5 | Synthesize & Write | Complete first draft + Coherence self-check |
| 6 | Edit & Output | Final manuscript (Word + LaTeX) + References |

### Key Features

- **Strict sequential execution** — each step must be confirmed before proceeding
- **Broad-to-narrow topic refinement** — 14 sub-steps in Step 2
- **Structured analytical tables** — Definition, Methods, and Results tables for deep analysis
- **Quantitative and qualitative analysis checklists** — differentiated by research paradigm
- **Writing synthesis enforcement** — prevents annotated-bibliography style
- **Manchester Academic Phrasebank integration** — functional sentence patterns for every section
- **48-item self-editing checklist** — from Appendix A of Galván & Galván (2017)
- **Zotero integration** — collection structure, tagging system, batch import guidance
- **Word and LaTeX output** — with Vancouver/APA/MLA referencing

## Installation

### For Cowork Mode

```bash
# Save the skill to your Cowork account
# In Cowork, use: /save-skill literature_review
# Or place the SKILL.md in:
# ~/Claude/skills/literature_review/SKILL.md
```

### Manual Installation

1. Copy `SKILL.md` to your Claude skills directory:
   - **Cowork**: `C:\Users\<username>\AppData\Local\Claude-3p\local-agent-mode-sessions\skills-plugin\...\skills\literature_review\`
   - **Claude Code CLI**: `~/.claude/skills/literature_review/`

2. The skill will automatically trigger on: `/literature_review`, "write literature review", "lit review", "literature review writing", "systematic review"

## Usage

```
/literature_review Write a review on [your topic]
```

Or simply say:
- "Write a literature review about..."
- "Help me with my literature review"
- "I need to write a lit review on..."

The skill will then guide you through all 6 steps sequentially.

### Review Types Supported

| Type | Length | Articles | Audience | Purpose |
|------|--------|----------|----------|---------|
| Term Paper | 10-20 pages | 10-30 | Instructor | Demonstrate mastery |
| Thesis | Full chapter(s) | 50-100+ | Committee | Justify research |
| Journal Article | 25-50 pages | 60-200 | Academic peers | Original synthesis |

### Writing Style Enforcement

The skill enforces thematic synthesis over annotated bibliography:

```
❌ FORBIDDEN: "Smith (2020) found... Jones (2019) reported..."
✅ CORRECT:   "Regarding [theme], research consistently indicates [finding].
              Both Smith (2020) and Chen (2021) found... However, Jones (2019),
              using different methodology, reached the opposite conclusion..."
```

## Requirements

- Claude Code or Cowork mode with skill support
- Zotero (recommended, for reference management)
- Microsoft Word or LaTeX (for final output)
- Access to academic databases (WoS, Scopus, PubMed, etc.)

## Academic References

- **Primary source**: Galván, J. L., & Galván, M. C. (2017). *Writing Literature Reviews: A Guide for Students of the Social and Behavioral Sciences* (7th ed.). Routledge.
- **Writing reference**: [University of Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/)

## File Structure

```
literature_review/
├── README.md                              ← Project overview & usage guide
├── SKILL.md                               ← Core skill definition (Claude Cowork)
├── CHANGELOG.md                           ← Full version history
├── LICENSE                                ← MIT License
├── .gitignore
├── examples/
│   ├── example_workflow.md                ← Full end-to-end workflow demonstration
│   └── output_templates.md                ← All output templates (tables, summaries)
└── references/
    └── phrasebank_guide.md                ← Manchester Phrasebank quick reference
```

## Dogfooding Case Study

This skill was developed and battle-tested through a real-world application: writing a comprehensive journal article review on **"Oncolytic Viruses and Cancer Immunotherapy"** (~8,000 words, 97 references) targeting the *Journal of Translational Medicine*. The full workflow produced:

- **Step 1-2**: Topic refinement across 4 sub-domains (molecular mechanisms, engineering, combination therapy, clinical translation)
- **Step 3**: Literature screening table (42 core articles) + gap analysis + Zotero structure template
- **Step 4**: Three deep-analysis tables (Definition/Methods/Results) + 4 thematic integration summaries
- **Step 5**: Journal style analysis (14 dimensions) + trend/pattern/gap identification + complete first draft
- **Step 6**: 48-item self-editing checklist → 5-reviewer simulated peer review → revision & final output

The dogfooding process directly led to the v1.1.0 strict execution protocol, after the AI model was observed skipping steps during initial use.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-05-08 | ⛔ Strict sequential execution protocol; completion gates at every step |
| 1.0.0 | 2026-05-07 | Initial release — complete Galván & Galván (2017) workflow |

## License

MIT License — see [LICENSE](LICENSE) file.

## Contributing

This skill follows the skill packaging conventions for Claude Code / Cowork mode. Contributions are welcome via GitHub issues and pull requests.
"# literature-review" 
"# literature-review" 
