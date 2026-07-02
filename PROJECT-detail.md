# PROJECT-detail.md — Translation Quality Evaluation (specialized)

## Executive Summary
`translation-quality-evaluation` turns Claude into a senior translation-quality reviewer and certified reviser fluent in localization industry standards. It runs a research-first harness that intakes the user's case, binds it to named world-renowned frameworks, scores it on 8 dimensions, and returns a prioritized improvement roadmap with effort/impact. The skill is self-improving: `tools/knowledge_updater.py` continuously refreshes its knowledge base from authoritative sources.

## Problem Statement
Buyers and agencies need an objective, standards-based way to evaluate whether a specialized translation is accurate, natural, terminologically correct, and faithful in register — beyond gut feeling.

## Target Users & Use Cases
- Primary: practitioners and non-experts who need an expert-grade, evidence-based assessment of their translation quality evaluation (specialized) artifact.
- Trigger examples:
  - User says: "Full assessment" → skill score every dimension with evidence, highlight accuracy and terminology correctness findings, deliver a prioritized roadmap
  - User says: "Targeted concern" → skill diagnose the fluency & naturalness issue against the named framework and return focused, measurable fixes
  - User says: "Benchmark / improvement loop" → skill re-score against the same rubric, show the before/after delta per dimension, and update the roadmap

## Harness Architecture
```
intake/requirements
    │  evaluation-framework-selector → error-typology → scoring-engine → improvement-roadmap → synthesis
    ▼
[named frameworks] → [multi-dimensional scoring] → [prioritized roadmap] → [quality/compliance gates] → DELIVERABLE
```

## Evaluation Frameworks (world-renowned, citable)
- **MQM (Multidimensional Quality Metrics)** — Error-typology-based quality scoring
- **DQF (TAUS Dynamic Quality Framework)** — Use-case-calibrated quality
- **ISO 17100 translation services** — Process and competence standard
- **Skopos theory / functional equivalence** — Purpose-driven fidelity
- **Terminology management (ISO 12616)** — Term consistency

## Scoring Dimensions
1. Accuracy (no mistranslation/omission)
2. Terminology correctness
3. Fluency & naturalness
4. Register & style fidelity
5. Domain conventions
6. Locale conventions (numbers/dates)
7. Consistency
8. Readability

## Full Sub-Skill Catalog
### `sub-evaluation-framework-selector`
- **Purpose:** Bind the audit to named, citable technical standards so findings are defensible.
- **Inputs:** Artifact metadata, sub-domain
- **Outputs:** Selected standard set with citations and the checklist each implies
- **Tools:** Read, WebSearch, WebFetch
- **Quality gate:** At least one named standard selected with citation and mapped checklist.
### `sub-error-typology`
- **Purpose:** Produce a structured, severity-weighted error log so the score is fully traceable.
- **Inputs:** Source + target text, domain
- **Outputs:** MQM-typed error log with severities and locations
- **Tools:** Read, WebSearch
- **Quality gate:** Each flagged error has an MQM category, severity, and the exact span quoted.
### `sub-scoring-engine`
- **Purpose:** Produce a transparent, dimension-by-dimension score (0-100 or band) with evidence for every sub-score.
- **Inputs:** Normalized profile, selected framework + rubric
- **Outputs:** Per-dimension scores, weighted total, strengths, and ranked weaknesses each tied to evidence
- **Tools:** Read, WebSearch
- **Quality gate:** Every dimension has a numeric score AND a one-line evidence/justification; no unscored dimension.
### `sub-improvement-roadmap`
- **Purpose:** Convert weaknesses into a sequenced, effort/impact-ranked action plan the user can execute.
- **Inputs:** Scored weaknesses, user constraints
- **Outputs:** Prioritized roadmap (Quick wins / Major projects / Long-term) with effort, impact, and success metric per item
- **Tools:** Read, Write
- **Quality gate:** Every recommendation has effort, impact, and a measurable success criterion.

## Skill File Format Specification
Each skill file uses YAML frontmatter (`name`, `description`) followed by: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates. `skills/main.md` is the harness entry point and invokes the sub-skills above in order.

## E2E Execution Flow
1. Parse the user request and uploaded artifact(s).
2. Run intake/requirements sub-skill; flag unknowns (no silent assumptions).
3. (No safety gate for this cluster.)
4. Select governing framework(s) and rubric.
5. Score every dimension with cited evidence.
6. Generate the prioritized roadmap (effort/impact + success metric).
7. Run quality/devil's-advocate review.
8. Synthesize the final professional deliverable; pass all quality gates before display.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: TAUS Quality, MQM framework, ISO 17100, Localization industry resources
- ArXiv categories: cs.CL
- Search queries: "translation quality estimation MQM", "terminology consistency localization", "machine translation evaluation"
- Append format: dated entries with Title, Authors, Year, Venue, DOI/Link, Relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: crawl4ai → fetch → parse → score (recency × relevance) → dedupe (URL/DOI hash) → append to `SECOND-KNOWLEDGE-BRAIN.md`. Schedule: weekly cron.

## Quality Gates (must all pass before output)
- Every scored dimension has evidence.
- At least one named framework cited.
- Roadmap items each have effort, impact, and a measurable success metric.
- Devil's-advocate review passed.

## Test Scenarios
1. **Full assessment** — Input: User submits a complete translation quality evaluation artifact and asks for a full evaluation → Expected: Score every dimension with evidence, highlight accuracy and terminology correctness findings, deliver a prioritized roadmap
2. **Targeted concern** — Input: User reports a specific weakness in fluency & naturalness → Expected: Diagnose the fluency & naturalness issue against the named framework and return focused, measurable fixes
3. **Benchmark / improvement loop** — Input: User wants to compare a revised version against a prior baseline → Expected: Re-score against the same rubric, show the before/after delta per dimension, and update the roadmap

## Key Design Decisions
1. Scoring is always bound to named, citable frameworks — never ad hoc.
2. Intake forbids silent assumptions; unknowns are surfaced.
3. Roadmap is effort/impact-ranked and measurable.
4. Knowledge base is self-updating for trend alignment.
5. Devil's-advocate review is mandatory before output.
