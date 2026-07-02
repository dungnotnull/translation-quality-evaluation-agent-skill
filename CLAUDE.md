# CLAUDE.md — Translation Quality Evaluation (specialized)

**Skill name:** `translation-quality-evaluation`
**Tagline:** Score a specialized translation on accuracy, fluency, terminology, and register fidelity.
**Source idea:** #95 (cluster: `design-creative-media`)
**Current phase:** Phase 4 — Testing & Validation (initial build complete)

## Problem This Skill Solves
Buyers and agencies need an objective, standards-based way to evaluate whether a specialized translation is accurate, natural, terminologically correct, and faithful in register — beyond gut feeling.

## Harness Flow Summary
1. **sub-evaluation-framework-selector** → Bind the audit to named, citable technical standards so findings are defensible.
2. **sub-error-typology** → Produce a structured, severity-weighted error log so the score is fully traceable.
3. **sub-scoring-engine** → Produce a transparent, dimension-by-dimension score (0-100 or band) with evidence for every sub-score.
4. **sub-improvement-roadmap** → Convert weaknesses into a sequenced, effort/impact-ranked action plan the user can execute.
5. **main (synthesis)** → assemble the scored deliverable + prioritized roadmap and run final quality gates.

## Gates
No safety/compliance gate applies to this cluster; standard quality gates still apply.

## Sub-skills
- `skills/sub-evaluation-framework-selector.md` — Select the governing translation-quality standards/heuristics for this evaluation.
- `skills/sub-error-typology.md` — Tag errors against the MQM error hierarchy with severity.
- `skills/sub-scoring-engine.md` — Multi-dimensional scoring of the translation against the selected framework.
- `skills/sub-improvement-roadmap.md` — Prioritized improvement roadmap for the translation with effort/impact.

## Tools Required
WebSearch, WebFetch, Read, Write, Bash

## Knowledge Sources
- [TAUS Quality](https://www.taus.net)
- [MQM framework](https://themqm.org)
- [ISO 17100](https://www.iso.org/standard/59149.html)
- [Localization industry resources](https://www.gala-global.org)

ArXiv / research categories crawled: cs.CL

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that refreshes `SECOND-KNOWLEDGE-BRAIN.md` weekly from the sources above.

## Active Development Tasks
- [x] Scaffold deliverables and sub-skills
- [x] Define scoring dimensions against named frameworks
- [ ] Expand `SECOND-KNOWLEDGE-BRAIN.md` with first crawl batch
- [ ] Add 3 more adversarial test scenarios
- [ ] Wire shared cluster sub-skills for reuse

## Reference Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — living domain knowledge base
