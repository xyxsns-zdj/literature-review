---
name: literature_review
description: "Complete 6-step literature review writing workflow based on Galván & Galván (2017). Strict step-by-step execution enforced. AI performs literature searches via WebSearch/WebFetch and presents results with real URLs. Every user interaction uses AskUserQuestion. Triggers on: /literature_review, write literature review, lit review, literature review writing, systematic review."
metadata:
  version: "1.3.0"
  last_updated: "2026-05-08"
  status: active
  based_on: "Galván, J. L., & Galván, M. C. (2017). Writing Literature Reviews (7th ed.). Routledge."
  writing_reference: "University of Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/)"
  task_type: guided
  execution_mode: strict_sequential
  ai_capabilities: "WebSearch, WebFetch, AskUserQuestion"
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
- ❌ Jumping ahead to later steps (e.g., discussing writing before topic is confirmed)
- ❌ Shortcutting the process because "the user seems experienced"
- ❌ Asking questions in plain text instead of using the AskUserQuestion tool
- ❌ Telling the user to "go search for X yourself" — the AI MUST perform searches

**Required behavior for EVERY step:**

1. **ANNOUNCE** the step number and name clearly (e.g., "## Step 1: Determine the Review Type")
2. **EXPLAIN** what this step accomplishes and why it matters (cite the book chapter)
3. **USE AskUserQuestion** for EVERY question to the user — never type questions in plain text.
4. **WAIT** for the user's response before continuing within the step
5. **VERIFY** the user's output meets the step's completion criteria
6. **CONFIRM** with the user before moving to the next step, using AskUserQuestion

**Completion gate before each transition:**
> ✅ Step X is now complete. You should have: [list of concrete outputs].
> ➡️ Ready to proceed to Step X+1: [step name]?

Every completion gate MUST use AskUserQuestion with Yes/No options to confirm progression.

**If the user says "skip this" or "I already did this":**
- Politely insist on reviewing their existing work: "I understand you've already done this. Could you share what you have so I can verify it meets the step's requirements before we move on?"

---

## 🖱️ MANDATORY: AskUserQuestion Usage Rules

**CRITICAL**: Every time the skill says "Ask the user..." or "Ask:" — you MUST use the `AskUserQuestion` tool. Never type the question as plain text.

### How to structure each AskUserQuestion call:

1. **For decision questions** (single choice among options): Set `multiSelect: false`. Provide 2–4 clear options as `{label, description}` pairs.

2. **For preference questions** (multiple selections allowed): Set `multiSelect: true`. Provide options the user can pick several from.

3. **For open-ended responses**: Include an option labeled "I'll type my answer" so the user can write freely. The other options serve as scaffolding/suggestions.

4. **For confirmation gates**: Always use 2 options: "Yes, proceed" and "Not yet, I need to finish something"

### AskUserQuestion parameter format:
```
AskUserQuestion({
  questions: [{
    question: "Clear, complete question ending with ?",
    header: "Short label (max 12 chars)",
    options: [
      {label: "Option 1", description: "What this means or what will happen"},
      {label: "Option 2", description: "What this means or what will happen"}
    ],
    multiSelect: false
  }]
})
```

### Grouping questions:
- If a phase has 2–3 related questions that don't depend on each other, you MAY batch them into a single `AskUserQuestion` call with multiple questions (up to 4).
- If questions are sequential (answer to Q1 determines Q2), ask them one at a time.

---

## 🔍 MANDATORY: AI-Led Literature Search Protocol

**CRITICAL PRINCIPLE**: The user should NOT have to leave this conversation to search for literature. Whenever the skill requires finding articles, the AI performs the search using WebSearch and WebFetch, summarizes the findings with real URLs, and presents results via AskUserQuestion for the user to select from.

### When the AI must search (not the user):

The AI takes over ALL of the following search tasks that the original skill assigned to the user:

| Step | Original "user does" | v1.3.0 "AI does" |
|------|---------------------|-----------------|
| 2.3 | User runs keyword search, reports results | AI runs WebSearch, presents findings |
| 2.7 | User browses recent abstracts | AI searches for recent papers, summarizes |
| 2.8 | User searches for theoretical articles | AI runs theory-focused search |
| 2.9 | User finds existing review articles | AI searches for reviews, reports gaps |
| 2.10 | User identifies landmark studies | AI searches + analyzes citation patterns |
| 5.A2 | User finds 3-5 recent reviews in target journal | AI searches target journal for reviews |

### Search protocol:

**Step A — Confirm search parameters with user via AskUserQuestion**
Before searching, confirm: the topic/keywords, any constraints (year range, methodology, etc.), and what the user wants to find. Use AskUserQuestion to let the user adjust parameters before the search runs.

**Step B — Execute the search using WebSearch**
Construct queries that target academic literature:
- Use site-specific searches when helpful: `site:scholar.google.com`, `site:pubmed.ncbi.nlm.nih.gov`, `site:eric.ed.gov`
- Always include the topic keyword + "review" or "research" or "study"
- For recent papers, add year constraints in the query
- For theoretical papers, add "theory" or "framework" or "model"
- Query format: `"[topic]" [optional: review|study|research] [optional: year]`

**Step C — Summarize and present findings via AskUserQuestion**
For each search, present:
- A brief summary of what was found (2-3 sentences)
- 5-10 specific paper results formatted as: **Title** (Author, Year) — *Journal* — [Real URL]
- AskUserQuestion options letting the user select which papers to pursue
- Always include the "I'll type my own" option for user-provided papers

**Step D — Deep-dive on selected papers via WebFetch**
When the user selects papers, use WebFetch to retrieve more detail (abstract, key findings) and present back to the user.

**Step E — Record results**
Save all user-selected papers with their real URLs. These become the user's literature pool.

### Example search flow:

```
1. AI asks via AskUserQuestion: "I'll search for [topic]. Any constraints?"
2. User selects: "Focus on last 5 years"
3. AI runs WebSearch: "oncolytic virus therapy review 2021 2022 2023 2024 2025 2026"
4. AI summarizes: "Found 120k results. Key themes: immunotherapy combinations, delivery methods, clinical trials..."
5. AI presents top 8 papers via AskUserQuestion with real URLs
6. User selects 4 papers
7. AI WebFetches details for those 4
8. Selected papers are added to user's literature pool
```

---

## Trigger Conditions

**Triggers**: `/literature_review`, write literature review, literature review writing, lit review, systematic review, write a review, help with literature review

---

## Workflow Overview

This skill guides you through the complete 6-step literature review writing process. Each step builds on the previous one:

```
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6
```

| Step | Name | Book Chapters | Key Output |
|------|------|---------------|------------|
| 1 | Determine Review Type | Ch. 1 | Review type selected |
| 2 | Select & Refine Topic | Ch. 3 | Refined topic statement + AI-searched literature pool |
| 3 | Screen Literature & Import to Zotero | Ch. 4, 8 | Screening table + Zotero library |
| 4 | Deep Analysis of Literature | Ch. 5–8 | Analysis tables + Summaries per category |
| 5 | Synthesize & Write First Draft | Ch. 9–11 | Complete first draft + Coherence revision |
| 6 | Edit, Finalize & Output | Ch. 12–13, App. A | Final manuscript (Word + LaTeX) + References |

---

## Step 1: Determine the Review Type

> **Book Reference**: Chapter 1 — Writing Reviews of Academic Literature: An Overview

**Why this step matters**: The review type determines the depth, breadth, audience, and format of your entire review. Making the wrong assumption here causes misalignment throughout the process.

### What to do in this step:

**1.1** — Present the three types to the user and explain the key differences:

### Type 1: Term Paper / Course-Assigned Review
- **Length**: 10–20 pages | **Literature**: 10–30 articles | **Audience**: Instructor
- **Purpose**: Demonstrate ability to search, read, understand, and synthesize literature
- **Process**: Select topic → Search → Read & analyze → Organize notes → Draft → Revise

### Type 2: Thesis / Dissertation Literature Review
- **Length**: Full chapter(s) | **Literature**: 50–100+ articles | **Audience**: Committee & examiners
- **Purpose**: Lay theoretical foundation for empirical research; identify gaps justifying your study
- **Process**: Define research question → Systematic search → Deep analysis → Organize by theme → Synthesize → Write → Multiple revisions

### Type 3: Journal Article Literature Review
- **Length**: 25–50 pages (journal-dependent) | **Audience**: Academic peers
- **Purpose**: Provide original, critical synthesis for the field; must have clear argument
- **Process**: Define review question & scope → Systematic search strategy → Screen & assess → Deep analysis → Build framework → Write → Peer review → Revise

| Dimension | Term Paper | Thesis | Journal |
|-----------|-----------|--------|---------|
| Purpose | Demonstrate mastery | Justify research | Provide synthesis |
| Depth | Moderate | Deep | Very deep |
| Originality | Low | Moderate | High |
| Audience | Instructor | Advisors & examiners | Academic peers |

**1.2** — Use **AskUserQuestion** to ask the review type:

```
AskUserQuestion({
  questions: [{
    question: "Which type of literature review are you writing?",
    header: "Review Type",
    options: [
      {label: "Term Paper / Course Review", description: "10-20 pages, 10-30 articles. Demonstrate ability to search, read, and synthesize literature for an instructor."},
      {label: "Thesis / Dissertation Review", description: "Full chapter(s), 50-100+ articles. Lay theoretical foundation and identify gaps justifying your empirical research."},
      {label: "Journal Article Review", description: "25-50 pages. Provide original, critical synthesis for academic peers. Must have a clear, novel argument."}
    ],
    multiSelect: false
  }]
})
```

**1.3** — After the user selects, confirm their choice and explain the implications for their workflow.

### Step 1 Completion Gate:
Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Step 1 is complete. Ready to proceed to Step 2: Select and Refine Your Topic? I'll help search for literature on your topic.",
    header: "Proceed?",
    options: [
      {label: "Yes, proceed", description: "Move to Step 2: defining your topic. I'll do the searching for you."},
      {label: "Not yet", description: "I want to reconsider my review type or ask a question first."}
    ],
    multiSelect: false
  }]
})
```

---

## Step 2: Select and Refine Your Topic

> **Book Reference**: Chapter 3 — Selecting a Topic for Your Review (14 steps)

**Why this step matters**: A well-defined topic is the foundation of an effective review. The 14-step process follows the **broad-to-narrow** principle.

**⛔ NEW in v1.3.0**: The AI performs all literature searches. You provide the topic and preferences; the AI finds real papers with real URLs and presents them for your selection.

### Phase A: Establish General Direction (Steps 1–3)

**Step 1 — Define your general topic**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "In 1-2 sentences, describe the general area you want to review. Precision is not required — just state your broad interest.",
    header: "General Topic",
    options: [
      {label: "I'll type my answer", description: "I'll describe my general research area in my own words."},
      {label: "I need help brainstorming", description: "I have a rough idea but want help narrowing it down."}
    ],
    multiSelect: false
  }]
})
```

After the user describes their topic, follow up with **AskUserQuestion** to probe motivation:
```
AskUserQuestion({
  questions: [{
    question: "Why does this topic interest you, and how familiar are you with the existing literature?",
    header: "Motivation",
    options: [
      {label: "I'll type my answer", description: "I'll explain my motivation and familiarity level."},
      {label: "Course requirement", description: "This is for a class assignment. I'm still getting familiar with the literature."},
      {label: "Research project", description: "This relates to my ongoing research. I have moderate familiarity."},
      {label: "Deep expertise", description: "I've worked in this area and know the literature well."}
    ],
    multiSelect: false
  }]
})
```

**Step 2 — Familiarize with database resources**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Which academic databases do you have access to? Even if you don't have direct access, I can search broadly via Google Scholar and the web. Select all that apply.",
    header: "Databases",
    options: [
      {label: "I have institutional access", description: "I can access Web of Science, Scopus, PubMed, etc. through my university."},
      {label: "Google Scholar only", description: "I primarily use free resources. The AI will focus on openly accessible papers."},
      {label: "PubMed (free)", description: "I work in biomedical/life sciences. PubMed is my primary database."},
      {label: "No preference", description: "Just find the best papers — I'll worry about access later."}
    ],
    multiSelect: true
  }]
})
```

**Step 3 — AI performs initial keyword search**

⛔ **AI ACTION REQUIRED**: Do NOT ask the user to search. The AI performs the search.

First, use **AskUserQuestion** to confirm keywords:
```
AskUserQuestion({
  questions: [{
    question: "Based on your topic, I'll search using relevant keywords. What keywords do you suggest? Or should I generate optimal search terms based on your topic?",
    header: "Keywords",
    options: [
      {label: "I'll provide keywords", description: "I have specific keywords in mind for the search."},
      {label: "Generate keywords for me", description: "Based on my topic description, create the best search terms."},
      {label: "Use my topic as-is", description: "Just search using my topic description directly."}
    ],
    multiSelect: false
  }]
})
```

**Then the AI MUST execute the search** using WebSearch. Construct queries targeting academic literature:

```
Search query structure:
- General: "[keyword1] [keyword2] research review"
- With year: "[keyword1] [keyword2] study [current year or recent range]"
- For breadth assessment: "[keyword1] [keyword2]" (to see total volume)
```

**After searching, present results via AskUserQuestion**:

```
AskUserQuestion({
  questions: [{
    question: "I searched for '[keywords]'. Found approximately [N] results. Here are the most relevant papers I identified. Which ones look interesting for your review? (Select all that apply.)",
    header: "Search Results",
    options: [
      {label: "[Paper 1 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 2 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 3 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 4 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 5 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 6 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 7 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "[Paper 8 Title] ([Year])", description: "[Journal]. [One-line finding]. [Real URL]"},
      {label: "None of these — search differently", description: "Let me refine the search with different keywords or constraints."},
      {label: "I'll add my own papers", description: "I already have specific papers I want to include."}
    ],
    multiSelect: true
  }]
})
```

**CRITICAL**: Every paper option MUST include a real, verifiable URL. If you cannot find a real URL for a paper, do NOT include it as an option.

**Summarize what you found**: After the user selects, provide a 2-3 sentence summary of: (1) total search volume, (2) main themes/sub-themes visible, (3) whether the topic seems too broad (>500 papers) or too narrow (<20 papers).

### Phase B: Adjust Scope (Steps 4–6)

**Step 4 — Narrow if needed**

If the AI's search returned many results (>500), use **AskUserQuestion** to guide narrowing:
```
AskUserQuestion({
  questions: [{
    question: "This is a large field with many results. Which dimension would you like to use to focus your review?",
    header: "Narrow By",
    options: [
      {label: "Population", description: "Focus on a specific group (e.g., adolescents, elderly, specific profession)."},
      {label: "Time frame", description: "Limit to recent publications (e.g., last 5-10 years)."},
      {label: "Method type", description: "Focus on specific research methods (e.g., only clinical trials, only qualitative)."},
      {label: "Context/Setting", description: "Limit to a specific context (e.g., specific country, clinical vs. community)."},
      {label: "Specific variable", description: "Focus on a particular aspect or variable within the broader topic."}
    ],
    multiSelect: true
  }]
})
```

After user selects narrowing dimensions, the AI runs a refined search and presents new results.

**Step 5 — Expand if needed**

If the AI's search returned <20–30 results, suggest and try broader synonyms, interdisciplinary search, or relaxing constraints. The AI runs the expanded search.

**Step 6 — Consider unpublished studies**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Will you include unpublished literature such as dissertations, conference papers, or preprints? This affects what I search for.",
    header: "Unpublished Lit",
    options: [
      {label: "Yes, include grey literature", description: "Include dissertations and conference papers to reduce publication bias."},
      {label: "Peer-reviewed only", description: "Limit to peer-reviewed journal articles for higher quality assurance."},
      {label: "Undecided", description: "I'd like to hear the pros and cons for my review type first."}
    ],
    multiSelect: false
  }]
})
```

### Phase C: Locate Key Resources (Steps 7–10)

**Step 7 — AI searches for recent papers and identifies patterns**

⛔ **AI ACTION REQUIRED**: The AI runs a targeted search for the most recent papers on the topic.

The AI MUST:
1. Run WebSearch with year constraints for recent papers (e.g., last 2-3 years)
2. Identify: (a) current focus areas, (b) recurring journals, (c) frequently cited older works in these papers
3. Present findings via AskUserQuestion:
```
AskUserQuestion({
  questions: [{
    question: "I searched for the most recent papers on your topic. Here's what I found about current research patterns. Which focus areas interest you most?",
    header: "Recent Patterns",
    options: [
      {label: "Focus Area 1: [name]", description: "[Brief description]. Key journals: [names]. Frequently cites: [older works]."},
      {label: "Focus Area 2: [name]", description: "[Brief description]. Key journals: [names]. Frequently cites: [older works]."},
      {label: "Focus Area 3: [name]", description: "[Brief description]. Key journals: [names]. Frequently cites: [older works]."},
      {label: "All of the above", description: "I want to cover all identified focus areas."}
    ],
    multiSelect: true
  }]
})
```

**Step 8 — AI searches for theoretical articles**

⛔ **AI ACTION REQUIRED**: The AI runs a theory-focused search.

The AI MUST:
1. Run WebSearch with: `"[topic]" theory OR framework OR model research`
2. Identify main theoretical frameworks used in the field
3. Present findings via AskUserQuestion:
```
AskUserQuestion({
  questions: [{
    question: "I searched for theoretical frameworks in your field. Here are the main theories I found. Which are relevant to your review?",
    header: "Theories",
    options: [
      {label: "[Theory/Framework 1]", description: "[Brief explanation]. Key authors: [names]. Found in [N] papers."},
      {label: "[Theory/Framework 2]", description: "[Brief explanation]. Key authors: [names]. Found in [N] papers."},
      {label: "[Theory/Framework 3]", description: "[Brief explanation]. Key authors: [names]. Found in [N] papers."},
      {label: "No clear theories found", description: "The literature seems largely atheoretical or uses implicit frameworks."},
      {label: "I'll specify my own", description: "I know the theoretical frameworks relevant to my work."}
    ],
    multiSelect: true
  }]
})
```

**Step 9 — AI finds existing review articles**

⛔ **AI ACTION REQUIRED**: The AI searches for existing review articles.

The AI MUST:
1. Run WebSearch with: `"[topic]" "literature review" OR "systematic review" OR "meta-analysis" OR "review"`
2. Identify the most recent reviews and their publication dates
3. Present findings via AskUserQuestion:
```
AskUserQuestion({
  questions: [{
    question: "I searched for existing reviews on your topic. The most recent review appears to be from [Year]. Here are the existing reviews I found. How do you want to differentiate yours?",
    header: "Existing Reviews",
    options: [
      {label: "Differentiate by focus", description: "Existing reviews cover X, I'll focus on Y (a sub-topic or different angle)."},
      {label: "Update an old review", description: "The last comprehensive review was [5+ years ago]. My review updates the field."},
      {label: "Different methodology", description: "Existing reviews are narrative; I'll do a systematic review or meta-analysis."},
      {label: "Different population/context", description: "I'll focus on a different population or context than existing reviews."},
      {label: "No existing reviews found", description: "This may be a genuine gap — my review would be the first."}
    ],
    multiSelect: false
  }]
})
```

After the user selects, present the specific existing review papers with URLs.

**Step 10 — AI identifies landmark studies**

⛔ **AI ACTION REQUIRED**: The AI searches for highly cited, foundational works.

The AI MUST:
1. Run WebSearch with: `"[topic]" seminal OR landmark OR foundational OR "highly cited"`
2. Also search: `"[topic]" [names of frequently cited older works from Step 7]`
3. Present findings via AskUserQuestion:
```
AskUserQuestion({
  questions: [{
    question: "I identified these landmark studies and core authors in your field. Which should form the foundation of your review?",
    header: "Landmark Studies",
    options: [
      {label: "[Author] ([Year]) — [Title]", description: "Cited by most papers in the field. [Brief significance]. [URL]"},
      {label: "[Author] ([Year]) — [Title]", description: "Cited by most papers in the field. [Brief significance]. [URL]"},
      {label: "[Author] ([Year]) — [Title]", description: "Cited by most papers in the field. [Brief significance]. [URL]"},
      {label: "[Author] ([Year]) — [Title]", description: "Cited by most papers in the field. [Brief significance]. [URL]"},
      {label: "[Author] ([Year]) — [Title]", description: "Cited by most papers in the field. [Brief significance]. [URL]"},
      {label: "I'll add my own", description: "I know specific foundational works not listed here."}
    ],
    multiSelect: true
  }]
})
```

### Phase D: Formulate Topic Statement (Steps 11–14)

**Step 11 — Assemble source collection**

The AI now has a pool of user-selected papers from Steps 3, 7, 8, 9, and 10. Use **AskUserQuestion** to summarize:
```
AskUserQuestion({
  questions: [{
    question: "Let's review what we've assembled. Based on our searches and your selections, we have approximately [N] articles spanning [earliest]–[latest]. They fall into [3-5] thematic categories. Shall I now help you draft your topic statement based on this collection?",
    header: "Source Summary",
    options: [
      {label: "Yes, draft topic statement", description: "Help me write a focused 2-4 sentence topic statement using what we've found."},
      {label: "Need more papers first", description: "Let me add more specific papers to the collection before drafting."},
      {label: "I'll write my own", description: "I have enough to draft the topic statement myself."}
    ],
    multiSelect: false
  }]
})
```

**Step 12 — Write topic statement draft**

Provide the user with the template:
```
"This review examines [topic/focus], focusing on [scope: timeframe, study types, population]. 
It aims to [purpose: synthesize, critique, identify gaps, etc.], which is significant because [reason]."
```

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Using the template provided, write your 2-4 sentence topic statement draft. What did you come up with?",
    header: "Topic Statement",
    options: [
      {label: "I'll share my draft", description: "I've written my topic statement and will paste it here."},
      {label: "Need help drafting", description: "I'd like you to propose a draft based on our searches and selections."}
    ],
    multiSelect: false
  }]
})
```

If the user selects "Need help drafting," the AI proposes a topic statement based on the collected literature and the review type.

**Step 13 — Refine the topic**

Use **AskUserQuestion** with multiSelect:
```
AskUserQuestion({
  questions: [{
    question: "Review your topic statement against these criteria. Which areas need refinement? (Select all that apply.)",
    header: "Refinement",
    options: [
      {label: "Focus: too broad or vague", description: "The topic needs further narrowing to be manageable."},
      {label: "Feasibility concerns", description: "I'm unsure if I can access enough data or complete this in my timeframe."},
      {label: "Literature adequacy", description: "I'm not sure there's enough (or too much) literature to review."},
      {label: "Value over existing reviews", description: "I'm not confident my review adds something new beyond what's already published."}
    ],
    multiSelect: true
  }]
})
```

For thesis reviews, also ask: "Is the topic clearly tied to your specific research question?"

**Step 14 — Seek advisor feedback**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Have you shared your topic statement with your advisor/instructor for feedback? This is strongly recommended before investing time in the full review.",
    header: "Advisor Check",
    options: [
      {label: "Already got feedback", description: "My advisor/instructor approved the topic. Ready to proceed."},
      {label: "Will get feedback first", description: "I'll send it now and continue after receiving feedback."},
      {label: "Proceeding without feedback", description: "I understand the risk but want to continue now (e.g., tight deadline)."}
    ],
    multiSelect: false
  }]
})
```

### Step 2 Completion Gate:
Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Step 2 is complete. You should have: a refined topic statement, an AI-curated literature pool with real URLs, knowledge of core researchers and theories, and understanding of existing reviews. Ready to proceed to Step 3: Screen Literature & Import to Zotero?",
    header: "Proceed?",
    options: [
      {label: "Yes, proceed to Step 3", description: "I have all the Step 2 outputs ready. Let's screen and organize my literature."},
      {label: "Not yet", description: "I need to finish something in Step 2 first."}
    ],
    multiSelect: false
  }]
})
```

---

## Step 3: Screen Literature, Build Tables & Import to Zotero

> **Book Reference**: Chapter 4 (Organizing Yourself to Begin Selection) + Chapter 8 (Organizing Notes by Grouping Results)

**Why this step matters**: You now have a pool of articles (AI-searched + any you provided). Before deep reading, you must systematically screen, classify, and organize everything.

### Phase A: Skim and Preliminary Screening

**Step 1 — Quick-skim each article (~5–10 min each)**

Guide the user to skim in this specific order: 1) Title, 2) Abstract, 3) Keywords, 4) Last paragraphs of Introduction, 5) Method headings, 6) First/last paragraph of Discussion, 7) References.

⛔ **AI ASSIST**: For papers selected through AI searches, the AI can WebFetch the abstract page and summarize key details to speed up screening. Offer this:

```
AskUserQuestion({
  questions: [{
    question: "I can help speed up screening by fetching and summarizing abstract details for the papers we found. Would you like me to do this before you skim?",
    header: "AI Assist",
    options: [
      {label: "Yes, fetch summaries", description: "Fetch abstracts for all AI-found papers and summarize key details to help me screen faster."},
      {label: "I'll skim manually", description: "I prefer to access and skim the papers myself."}
    ],
    multiSelect: false
  }]
})
```

After skimming, classify each article as: **Definitely Include** / **Possibly Include** / **Exclude**.

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "After screening, report your results. How many articles did you classify as Definitely Include, Possibly Include, and Exclude?",
    header: "Screening Results",
    options: [
      {label: "I'll report my numbers", description: "I have my inclusion/exclusion counts ready."},
      {label: "Still screening", description: "I'm still working through my articles and will report back."},
      {label: "Need help with criteria", description: "I'm unsure how to classify some borderline articles."}
    ],
    multiSelect: false
  }]
})
```

**Step 2 — Group retained articles by category**

Present the 6 categorization dimensions. Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Which primary dimension will you use to categorize your retained articles?",
    header: "Categorization",
    options: [
      {label: "Theme / Sub-theme", description: "Group by the main topics or sub-topics the articles address."},
      {label: "Research Method", description: "Group by methodology (qualitative, quantitative, mixed methods, etc.)."},
      {label: "Theoretical Framework", description: "Group by the theoretical lens each article employs."},
      {label: "Population / Sample", description: "Group by who or what was studied."},
      {label: "Time Period", description: "Group chronologically by publication date or studied period."},
      {label: "Finding Direction", description: "Group by whether findings support, contradict, or are mixed."}
    ],
    multiSelect: false
  }]
})
```

### Phase B: Check for Gaps

**Step 3 — Identify and fill gaps**

Walk through 4 gap types. Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Review your categorized articles for gaps. Did you identify any: sparse categories, missing theoretical perspectives, population/context gaps, or methodological monotony?",
    header: "Gap Check",
    options: [
      {label: "Yes, I found gaps", description: "I identified specific gaps and can describe them."},
      {label: "No obvious gaps", description: "My categories seem well-covered across all dimensions."},
      {label: "Unsure", description: "I need help identifying what constitutes a meaningful gap."}
    ],
    multiSelect: false
  }]
})
```

⛔ **AI ACTION**: If gaps exist, the AI runs targeted supplementary searches to fill them (same protocol as Step 2: search → present → user selects).

### Phase C: Build the Literature Screening Summary Table

**Step 4 — Create the screening table**

Provide the 11-column template: Author/Year, Title, Study Type, Design/Method, Sample/Data, Key Variables, Main Findings, Theoretical Framework, Thematic Category, Relevance (1-5), Priority (High/Med/Low).

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Have you created your Literature Screening Summary Table in Excel or Google Sheets with all 11 columns?",
    header: "Table Status",
    options: [
      {label: "Table created & populated", description: "I've built the table and filled in at least 5-10 articles. Ready to move on."},
      {label: "Table created, filling in", description: "I've set up the columns but am still populating entries."},
      {label: "Need the template", description: "Please provide me with the exact column headers and a blank template."}
    ],
    multiSelect: false
  }]
})
```

### Phase D: Import into Zotero

**Step 5 — Import all literature into Zotero**

Guide through Collection structure and import methods. Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Have you imported all your retained articles into Zotero with the recommended Collection structure?",
    header: "Zotero Import",
    options: [
      {label: "Fully imported & organized", description: "All articles are in Zotero with collections, tags, and PDFs attached."},
      {label: "Partially imported", description: "I've started importing but haven't finished all articles or collections."},
      {label: "Don't use Zotero", description: "I use a different reference manager or no reference manager."},
      {label: "Need setup help", description: "I need step-by-step guidance on setting up Zotero."}
    ],
    multiSelect: false
  }]
})
```

**Step 6 — Verify consistency**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Does your Zotero count match your screening table? Do Collections map to categories? Any missing PDFs?",
    header: "Consistency",
    options: [
      {label: "Everything matches", description: "Counts match, categories align, and all PDFs are linked."},
      {label: "Minor discrepancies", description: "There are small mismatches I need to fix."},
      {label: "Major gaps", description: "Significant inconsistencies — many missing PDFs or mismatched counts."}
    ],
    multiSelect: false
  }]
})
```

### Phase E: Final Organization Check

**Step 7 — Organizational readiness check**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Are all 7 readiness items complete: Zotero structure set, screening table filled, PDFs linked, priorities assigned, categories clear, gaps flagged, excluded documented?",
    header: "Readiness",
    options: [
      {label: "All 7 items complete", description: "My literature is fully organized and ready for deep analysis."},
      {label: "Mostly complete (5-6/7)", description: "A few minor items remain."},
      {label: "Still working (1-4/7)", description: "I have significant organization work remaining."}
    ],
    multiSelect: false
  }]
})
```

### Step 3 Completion Gate:
Use **AskUserQuestion** with Yes/No options.

---

## Step 4: Deep Analysis of Literature

> **Book Reference**: Chapters 5–8

**Why this step matters**: This is the most critical analytical phase. The three structured tables (Definition, Methods, Results) are your primary tools.

### Phase A: Build Three Analytical Tables (Chapter 5)

**Table 1 — Definition Table**: Guide user to identify 3–5 core constructs first.

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "What are the 3-5 core constructs or key concepts that appear across your literature?",
    header: "Core Constructs",
    options: [
      {label: "I'll list my constructs", description: "I've identified the key concepts and can name them."},
      {label: "Need help identifying", description: "I've read the articles but am unsure which constructs are 'core' enough to track."}
    ],
    multiSelect: false
  }]
})
```

Guide through completing Definition Table, Methods Table, and Results Summary Table. Use **AskUserQuestion** to check completion of each.

### Phase B: Analyze Quantitative Research (Chapter 6)

Walk through specialized checklist for each quantitative article. Use **AskUserQuestion** for cross-study summary.

### Phase C: Analyze Qualitative Research (Chapter 7)

Walk through specialized checklist. **IMPORTANT**: Warn user not to apply quantitative criteria to qualitative studies. Use **AskUserQuestion** for cross-study summary.

### Phase D: Integrate by Group (Chapter 8)

Create Analysis Integration Tables and write 300–500 word summaries per category. Use **AskUserQuestion** to check progress.

### Step 4 Completion Gate:
Use **AskUserQuestion** with Yes/No options.

---

## Step 5: Synthesize Trends, Write Draft & Develop Coherent Essay

> **Book Reference**: Chapters 9–11
> **Writing Reference**: [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/)

**Why this step matters**: Transition from analysis to writing. Produce a well-organized, clearly argued draft — NOT an annotated bibliography.

### Phase A: Journal-Specific Preparation (Journal Reviews Only)

⛔ **ONLY execute this phase if the user selected Journal Review in Step 1.**

**A1** — Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Which journal(s) are you targeting for submission? Name 1-3 candidates.",
    header: "Target Journal",
    options: [
      {label: "I'll name my journal(s)", description: "I have specific journals in mind."},
      {label: "Need suggestions", description: "Based on my topic, can you suggest appropriate journals?"}
    ],
    multiSelect: false
  }]
})
```

**A2 — AI searches for recent reviews in target journal**

⛔ **AI ACTION REQUIRED**: The AI runs WebSearch to find 3-5 recent review articles in the target journal.

Search query: `site:[journal domain] "[topic]" review`

Present findings via **AskUserQuestion** with real URLs:
```
AskUserQuestion({
  questions: [{
    question: "I searched [journal name] for recent review articles. Here are [N] relevant ones I found. Which would you like to analyze for style? (Select 3-5.)",
    header: "Journal Reviews",
    options: [
      {label: "[Title] ([Year])", description: "Authors: [names]. [Brief note on approach]. [Real URL]"},
      {label: "[Title] ([Year])", description: "Authors: [names]. [Brief note on approach]. [Real URL]"},
      {label: "[Title] ([Year])", description: "Authors: [names]. [Brief note on approach]. [Real URL]"},
      {label: "[Title] ([Year])", description: "Authors: [names]. [Brief note on approach]. [Real URL]"},
      {label: "[Title] ([Year])", description: "Authors: [names]. [Brief note on approach]. [Real URL]"},
      {label: "Search differently", description: "Try a different search approach for this journal."}
    ],
    multiSelect: true
  }]
})
```

**A3** — Guide user through the 14-dimension style analysis table for selected papers.

### Phase B: Build an Outline (Chapter 9)

**B1 — Trend Identification**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Review your Analysis Summaries for trends. Which types of trends did you identify?",
    header: "Trends Found",
    options: [
      {label: "Temporal trends", description: "Changes in findings/focus over time."},
      {label: "Methodological trends", description: "Shifts in how research is conducted."},
      {label: "Theoretical trends", description: "Shifts in dominant frameworks or models."},
      {label: "Population/Geographic trends", description: "Changes in who/where is studied."}
    ],
    multiSelect: true
  }]
})
```

**B2 — Pattern Identification**

Use **AskUserQuestion** with options for consistent findings, contradictory findings, method-finding links, theory-finding links, cross-category tensions.

**B3 — Gap Summary**: Ask user to rank gaps by priority.

**B4 — Choose organizational scheme**

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Which organizational scheme will you use to structure your literature review?",
    header: "Organization",
    options: [
      {label: "Thematic", description: "Organize by themes or topics. Most common and effective for synthesis."},
      {label: "Chronological", description: "Organize by time period to show how the field has evolved."},
      {label: "Methodological", description: "Organize by research method to compare approaches."},
      {label: "Theoretical", description: "Organize by theoretical frameworks to compare different lenses."},
      {label: "Hybrid", description: "Combine multiple schemes (e.g., thematic within chronological)."}
    ],
    multiSelect: false
  }]
})
```

**B5 — Build detailed outline**: Provide template, review together before writing.

### Phase C: Write the First Draft (Chapter 10)

**CRITICAL RULE before writing starts:**

> ⛔ FORBIDDEN: "Smith (2020) found... Jones (2019) reported..."
> ✅ CORRECT: "Regarding [Theme X], research consistently indicates [finding]. For example, both Smith (2020) and Chen (2021) found that... However, Jones (2019), using a different methodology, reached the opposite conclusion..."

Introduce Manchester Academic Phrasebank. Writing order: Most familiar category first → Others → Cross-theme → Conclusion → Introduction last.

After each section, use **AskUserQuestion** to check for annotated bibliography pattern.

### Phase D: Develop a Coherent Essay (Chapter 11 — 9 Guidelines)

Walk through each guideline using **AskUserQuestion**. For Guideline 3 (Thesis Statement — most important):
```
AskUserQuestion({
  questions: [{
    question: "Guideline 3 (MOST IMPORTANT): Can you identify your review's thesis statement — the central argument? (It should argue something, e.g., 'This review argues that...' not just 'This paper reviews X.')",
    header: "Thesis Statement",
    options: [
      {label: "Yes, I have one", description: "I can state my thesis clearly as a specific argument."},
      {label: "I'm not sure", description: "I may need help formulating a thesis."},
      {label: "Let me revise", description: "I realize my draft lacks a strong thesis. Let me work on one."}
    ],
    multiSelect: false
  }]
})
```

### Phase E: Process Recording

Use **AskUserQuestion** about process record maintenance.

### Step 5 Completion Gate:
Use **AskUserQuestion** with Yes/No options.

---

## Step 6: Edit, Finalize & Output

> **Book Reference**: Chapters 12–13 + Appendix A

**Why this step matters**: Systematic editing, precise formatting, and verified references make the difference between a draft and a submission-ready manuscript.

### Phase A: Comprehensive Self-Editing Checklist (Appendix A)

⛔ **Before editing, ask user to read entire manuscript once without marking anything.**

Walk through all 48 items across 5 dimensions using **AskUserQuestion** for each:

**Dimension 1 — Content & Synthesis (10 items)**:
```
AskUserQuestion({
  questions: [{
    question: "Check your draft against Content & Synthesis criteria. Which need revision? (Select all that apply.)",
    header: "Content",
    options: [
      {label: "Literature coverage", description: "Important studies or perspectives are missing."},
      {label: "Depth of analysis", description: "Need deeper critical engagement, not just description."},
      {label: "Trend identification", description: "Need to better highlight field evolution."},
      {label: "Contradictory findings", description: "Need to better discuss conflicting results."},
      {label: "Gap discussion", description: "Need clearer research gap identification."},
      {label: "Argument-centered writing", description: "Need stronger thesis-driven argument."},
      {label: "Critical evaluation", description: "Need more critical assessment of study quality."},
      {label: "Method discussion", description: "Need better methodological pattern discussion."},
      {label: "Theory integration", description: "Need stronger theoretical framework connection."}
    ],
    multiSelect: true
  }]
})
```

**Dimension 2 — Organization & Coherence, Dimension 3 — Style & Language, Dimension 4 — Citations & References, Dimension 5 — Presentation**: Same AskUserQuestion pattern.

### Phase B: Edit and Revise (Chapter 12)

Use **AskUserQuestion** to track editing rounds (Macro → Meso → Micro). Guide feedback incorporation protocol.

### Phase C: Refine the Final Title

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Rate your working title: informative, concise, engaging, uses keywords, audience-appropriate, reflects thesis. How does it score?",
    header: "Title Quality",
    options: [
      {label: "Strong (5-6/6)", description: "My title performs well on most criteria."},
      {label: "Adequate (3-4/6)", description: "Serviceable but could be stronger."},
      {label: "Needs work (0-2/6)", description: "Needs significant revision."}
    ],
    multiSelect: false
  }]
})
```

### Phase D: Format References via Zotero (Chapter 13)

Guide through 5-step reference formatting. Use **AskUserQuestion** to verify completion.

### Phase E: Output in Word and LaTeX

Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "Which output format(s) do you need for your final manuscript?",
    header: "Output Format",
    options: [
      {label: "Word (.docx + .pdf)", description: "Generate final manuscript as a Word document and PDF."},
      {label: "LaTeX (.tex + .pdf)", description: "Generate final manuscript as LaTeX source with compiled PDF."},
      {label: "Both Word and LaTeX", description: "I need both Word and LaTeX versions."}
    ],
    multiSelect: true
  }]
})
```

### Step 6 Completion Gate:
Use **AskUserQuestion**:
```
AskUserQuestion({
  questions: [{
    question: "🎉 All 6 steps are complete! Your literature review is finished. Would you like a final summary of what we accomplished?",
    header: "Done!",
    options: [
      {label: "Yes, show final summary", description: "Give me a recap of the entire workflow."},
      {label: "No, I'm all set", description: "I have everything I need. Thanks!"}
    ],
    multiSelect: false
  }]
})
```

---

## Quick Reference: 12 Key Principles

1. **Broad to narrow** — start wide, iteratively focus (Ch. 3)
2. **Skim before you read** — structural preview, not immediate deep reading (Ch. 4)
3. **Use structured tables** — Definition, Methods, Results tables are analysis tools (Ch. 5)
4. **Different criteria for quant vs. qual** — never apply quantitative standards to qualitative work (Ch. 6–7)
5. **Integrate by group before writing** — organize analysis results by category (Ch. 8)
6. **Build an outline first** — identify trends, patterns, gaps before writing (Ch. 9)
7. **Synthesize, don't annotate** — every paragraph must be theme-centered (Ch. 10–11)
8. **Have a thesis statement** — your review must ARGUE something (Ch. 11)
9. **Multi-round editing** — structural → paragraph → sentence (Ch. 12)
10. **Zotero throughout** — import early, tag consistently, verify before output (Ch. 4, 13)
11. **Use the Manchester Phrasebank** — functional sentence patterns for every writing task
12. **Seek feedback before finalizing** — advisor, peers, writing center (Ch. 12)

---

> 🎉 This skill enforces the complete Galván & Galván (2017) workflow — all 13 chapters + Appendix A.
> 🔍 v1.3.0: AI performs all literature searches via WebSearch/WebFetch, presents real results with URLs via AskUserQuestion.
