# Cluster Integration Guide — Translation Quality Evaluation (specialized)

This document describes how the Translation Quality Evaluation skill integrates with the design-creative-media cluster, including shared sub-skills, reuse maps, and compatibility notes.

## Cluster Overview

**Cluster Name:** design-creative-media
**Cluster Skills:**
- Translation Quality Evaluation (specialized) — Skill #95 (this skill)
- Content Quality Assessment (planned)
- Localization Quality Review (planned)
- Technical Writing Review (planned)

**Shared Purpose:** Evaluate quality of creative and professional content using standardized frameworks and interoperable outputs.

## Shared Sub-Skills

The following shared sub-skills are available for reuse across the design-creative-media cluster:

### 1. sub-error-detection

**Location:** `skills/shared/sub-error-detection.md`
**Purpose:** Detect and categorize errors using MQM-based typology
**Version:** 1.0.0

**Reused By:**
- Translation Quality Evaluation (specialized) — Primary use for error categorization
- Content Quality Assessment — Detect factual and structural errors
- Localization Quality Review — Detect localization-specific errors

**Input/Output Contract:**
```yaml
# Input
source_text: string
target_text: string
domain: string
error_categories: array["Accuracy", "Fluency", "Terminology", "Design", "Locale_Convention", "Verity"]
severity_threshold: "Critical" | "Major" | "Minor" | "Trivial" | "All"

# Output
error_log: array of error objects with category, severity, spans
summary: object with totals by category and severity
```

**Usage in Translation Quality Evaluation:**
```yaml
# In main.md harness, invoke for error typology:
invoke: sub-error-detection
inputs:
  source_text: "{user_provided_source}"
  target_text: "{user_provided_target}"
  domain: "{detected_domain}"
  error_categories: ["Accuracy", "Fluency", "Terminology", "Locale_Convention"]
# Use error_log for MQM-based error scoring
```

### 2. sub-terminology-validator

**Location:** `skills/shared/sub-terminology-validator.md`
**Purpose:** Validate terminology consistency and correctness using ISO 12616
**Version:** 1.0.0

**Reused By:**
- Translation Quality Evaluation (specialized) — Validate medical/legal/technical terminology
- Content Quality Assessment — Ensure domain-specific term usage
- Localization Quality Review — Validate locale-appropriate terminology

**Input/Output Contract:**
```yaml
# Input
target_text: string
domain: string
term_list: array (optional)
consistency_check: boolean (default: true)
correctness_check: boolean (default: true)

# Output
terminology_report: object with term variants, issues, scores
```

**Usage in Translation Quality Evaluation:**
```yaml
# In sub-error-typology, invoke for terminology validation:
invoke: sub-terminology-validator
inputs:
  target_text: "{user_provided_target}"
  domain: "{detected_domain}"
  term_list: "{domain_specific_terms}"
# Use terminology_report for consistency and correctness scoring
```

### 3. sub-consistency-checker

**Location:** `skills/shared/sub-consistency-checker.md`
**Purpose:** Check consistency within and across documents
**Version:** 1.0.0

**Reused By:**
- Translation Quality Evaluation (specialized) — Validate translation consistency
- Content Quality Assessment — Ensure document suite consistency
- Technical Writing Review — Validate documentation consistency

**Input/Output Contract:**
```yaml
# Input
texts: array of strings
check_types: array["terminology", "phrasing", "formatting", "style", "cross_reference"]
domain: string (optional)
style_guide: string (optional)

# Output
consistency_report: object with overall score, issues by type, recommendations
```

**Usage in Translation Quality Evaluation:**
```yaml
# In multi-document evaluation, invoke for consistency:
invoke: sub-consistency-checker
inputs:
  texts: ["{document_1}", "{document_2}", "{document_3}"]
  check_types: ["terminology", "phrasing"]
  domain: "{detected_domain}"
# Use consistency_report for Consistency dimension scoring
```

### 4. sub-style-analyzer

**Location:** `skills/shared/sub-style-analyzer.md`
**Purpose:** Analyze style, register, and tone using Skopos theory
**Version:** 1.0.0

**Reused By:**
- Translation Quality Evaluation (specialized) — Validate register and style fidelity
- Content Quality Assessment — Evaluate tone appropriateness
- Brand Voice Analysis — Validate brand voice consistency

**Input/Output Contract:**
```yaml
# Input
text: string
target_audience: string
purpose: string
expected_register: "formal" | "neutral" | "informal" | "colloquial"
domain: string
style_guide: string (optional)

# Output
style_analysis: object with register/tone detection, match assessment, issues
```

**Usage in Translation Quality Evaluation:**
```yaml
# In main harness, invoke for register analysis:
invoke: sub-style-analyzer
inputs:
  text: "{user_provided_target}"
  target_audience: "{determined_audience}"
  purpose: "{determined_purpose}"
  expected_register: "{detected_expected_register}"
  domain: "{detected_domain}"
# Use style_analysis for Register & Style Fidelity dimension scoring
```

## Reuse Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                    design-creative-media Cluster                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────┐      ┌──────────────────────────────────┐   │
│  │   Shared Sub-    │      │    Translation Quality            │   │
│  │    Skills        │◄────►│    Evaluation (specialized) #95    │   │
│  └──────────────────┘      └──────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────────┐                                              │
│  │ sub-error-       │◄─────┐ Detects MQM-typed errors            │
│  │ detection        │      │                                      │
│  └──────────────────┘      │                                      │
│                             │                                      │
│  ┌──────────────────┐      │                                      │
│  │ sub-terminology-  │◄─────┤ Validates terminology (ISO 12616)  │
│  │ validator        │      │                                      │
│  └──────────────────┘      │                                      │
│                             │                                      │
│  ┌──────────────────┐      │                                      │
│  │ sub-consistency-  │◄─────┤ Checks consistency across docs      │
│  │ checker          │      │                                      │
│  └──────────────────┘      │                                      │
│                             │                                      │
│  ┌──────────────────┐      │                                      │
│  │ sub-style-        │◄─────┘ Analyzes register/style (Skopos)   │
│  │ analyzer         │                                            │
│  └──────────────────┘                                            │
│                                                                     │
│  Planned Reuse:                                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Content Quality Assessment (planned)                         │ │
│  │ └── Reuses: sub-error-detection, sub-style-analyzer         │ │
│  │ Localization Quality Review (planned)                       │ │
│  │ └── Reuses: sub-error-detection, sub-terminology-validator, │ │
│  │              sub-consistency-checker                          │ │
│  │ Technical Writing Review (planned)                          │ │
│  │ └── Reuses: sub-error-detection, sub-style-analyzer,        │ │
│  │              sub-consistency-checker                          │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Compatibility Notes

### Version Compatibility

**Shared Sub-Skill Version:** 1.0.0
**Compatible With:**
- Translation Quality Evaluation (specialized) v1.0.0+
- Any cluster skill following the input/output contracts

**Breaking Changes:**
- Changes to input/output field names
- Removal of required fields
- Changes to enum values (severity, category, etc.)

**Non-Breaking Changes:**
- Addition of optional fields
- Expansion of enum values
- Changes to descriptions/documentation

### Schema Compatibility

**Output Schema:** `scoring-output-schema.json` v1.0.0
**Compatible With:**
- Any consumer expecting v1.x.x schema
- JSON Schema validators (Draft 7)

**Migration Notes:**
- v1.0.0 → v2.0.0: Will require migration support for breaking changes
- Consumers should verify `schema_version` before processing

### Framework Compatibility

**Supported Frameworks:**
- MQM (Multidimensional Quality Metrics)
- DQF (TAUS Dynamic Quality Framework)
- ISO 17100 (Translation Services)
- ISO 12616 (Translation-oriented Terminology)
- Skopos Theory

**Framework Versions:**
- MQM: 2022+
- DQF: 2021+
- ISO 17100: 2015+
- ISO 12616: 2022+

## Integration Patterns

### Pattern 1: Direct Sub-Skill Invocation

```yaml
# In calling skill (e.g., main.md)
invoke: sub-error-detection
inputs:
  source_text: "{{source}}"
  target_text: "{{target}}"
  domain: "{{domain}}"
# Process returned error_log
```

### Pattern 2: Chained Sub-Skills

```yaml
# First skill outputs become second skill inputs
invoke: sub-error-detection
inputs: {...}
# Store error_log

invoke: sub-terminology-validator
inputs:
  target_text: "{{target}}"
  error_categories: "{{error_log.categories}}"  # From previous result
# Combine results for final scoring
```

### Pattern 3: Parallel Sub-Skills

```yaml
# Run multiple sub-skills in parallel for efficiency
parallel:
  - invoke: sub-error-detection
    inputs: {...}
  - invoke: sub-terminology-validator
    inputs: {...}
  - invoke: sub-style-analyzer
    inputs: {...}
# Combine all results for comprehensive evaluation
```

## Data Flow

```
User Input (Source, Target, Request)
    │
    ▼
┌─────────────────────────────────────────┐
│  Translation Quality Evaluation         │
│  (main.md harness)                      │
└─────────────────────────────────────────┘
    │
    ├─────────────────────────────────────────────────────┐
    │                                                     │
    ▼                                                     ▼
┌──────────────────────┐                       ┌──────────────────────┐
│ sub-evaluation-     │                       │ Shared Sub-Skills:   │
│ framework-selector  │                       │                      │
│ (skill-specific)    │                       │ • sub-error-detection│
└──────────────────────┘                       │ • sub-terminology-   │
    │                                          │   validator          │
    │                                          │ • sub-consistency-   │
    │                                          │   checker            │
    │                                          │ • sub-style-analyzer │
    │                                          └──────────────────────┘
    │                                                     │
    │                                                     │
    ▼                                                     ▼
┌──────────────────────┐                       ┌──────────────────────┐
│ sub-error-typology   │◄──────────────────────┤ Shared sub-skill     │
│ (skill-specific)    │                       │ outputs              │
└──────────────────────┘                       └──────────────────────┘
    │                                                     │
    │                                                     │
    ▼                                                     ▼
┌──────────────────────┐                       ┌──────────────────────┐
│ sub-scoring-engine   │◄──────────────────────┤ Combined analysis    │
│ (skill-specific)    │                       │                      │
└──────────────────────┘                       └──────────────────────┘
    │
    ▼
┌──────────────────────┐
│ sub-improvement-     │
│ roadmap              │
│ (skill-specific)    │
└──────────────────────┘
    │
    ▼
Final Output (Scorecard + Roadmap)
    │
    ▼
Standardized JSON (scoring-output-schema.json)
```

## Standards and References

### MQM Framework
- **Specification:** https://themqm.org
- **Error Categories:** Accuracy, Fluency, Terminology, Design, Locale_Convention, Verity
- **Severity Levels:** Critical, Major, Minor, Trivial

### DQF Framework
- **Specification:** https://www.taus.net/dqf-model
- **Quality Models:** Publishing, Internal Communication, Technical, User-Generated, Legal/Medical
- **Content Types:** Use-case determines quality priorities

### ISO 17100
- **Specification:** https://www.iso.org/standard/59149.html
- **Competence Requirements:** Translation, Linguistic, Cultural, Research, Technical, Domain
- **Process:** Translation, Review, Verification

### ISO 12616
- **Specification:** https://www.iso.org/standard/73325.html
- **Term Quality:** Accuracy, Consistency, Clarity, Currency, Appropriateness
- **Management:** Identification, Standardization, Consistency, Maintenance

### Skopos Theory
- **Origin:** Hans Vermeer
- **Principle:** Purpose (Skopos) determines translation strategy
- **Application:** Functional equivalence over formal equivalence

## Future Cluster Skills

### Content Quality Assessment (Planned)
**Purpose:** Evaluate content quality for accuracy, completeness, and clarity
**Shared Sub-Skills:**
- `sub-error-detection` — Factual errors, structural issues
- `sub-style-analyzer` — Tone appropriateness, readability

### Localization Quality Review (Planned)
**Purpose:** Validate localized content for cultural appropriateness and locale conventions
**Shared Sub-Skills:**
- `sub-error-detection` — Localization-specific errors
- `sub-terminology-validator` — Locale-appropriate terminology
- `sub-consistency-checker` — Multi-locale consistency
- `sub-style-analyzer` — Cultural appropriateness

### Technical Writing Review (Planned)
**Purpose:** Evaluate technical documentation for clarity, accuracy, and completeness
**Shared Sub-Skills:**
- `sub-error-detection` — Technical inaccuracies
- `sub-consistency-checker` — Documentation consistency
- `sub-style-analyzer` — Technical style and readability

## Cluster Governance

### Version Management
- Shared sub-skills use semantic versioning
- Breaking changes require major version increment
- Cluster skills specify compatible sub-skill versions

### Change Coordination
- Proposed changes to shared sub-skills announced to cluster
- Feedback period before breaking changes
- Migration guides provided for major versions

### Quality Assurance
- All shared sub-skills must pass cluster quality gates
- Input/output contracts validated with test suite
- Documentation maintained with code

## Contributing

### Adding New Shared Sub-Skills

1. **Propose:** Document purpose, input/output contract, and use cases
2. **Review:** Cluster review for compatibility and necessity
3. **Implement:** Create sub-skill in `skills/shared/`
4. **Test:** Add tests and validate with cluster test suite
5. **Document:** Update this integration guide
6. **Version:** Assign initial version (1.0.0)

### Modifying Existing Shared Sub-Skills

1. **Assess Impact:** Determine if change is breaking or non-breaking
2. **Propose:** Document change and rationale
3. **Review:** Cluster review for approval
4. **Version:** Increment version appropriately
5. **Migrate:** Provide migration guide if breaking
6. **Test:** Validate with cluster test suite

## Support and Maintenance

**Cluster Maintainer:** Translation Quality Evaluation skill team
**Shared Sub-Skill Owner:** Cluster consortium
**Issue Tracker:** [To be established]
**Documentation:** See `docs/cluster-integration.md`

---

**Last Updated:** 2026-07-02
**Cluster Version:** 1.0.0
**Schema Version:** 1.0.0
