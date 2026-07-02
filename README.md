# Translation Quality Evaluation (Specialized)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/dungnotnull/translation-quality-evaluation-agent-skill)
[![Production Ready](https://img.shields.io/badge/status-production--ready-brightgreen.svg)](https://github.com/dungnotnull/translation-quality-evaluation-agent-skill)
[![Open Source](https://img.shields.io/badge/open--source-yes-success.svg)](https://github.com/dungnotnull/translation-quality-evaluation-agent-skill)

> A production-grade AI skill for evaluating translation quality using industry-standard frameworks (MQM, DQF, ISO 17100, ISO 12616, Skopos Theory) with multi-dimensional scoring and evidence-based improvement roadmaps.

---

## Overview

The **Translation Quality Evaluation (specialized)** skill turns Claude into a senior translation-quality reviewer and certified reviser fluent in localization industry standards. It runs a research-first harness that evaluates translations across 8 dimensions, binds findings to citable technical frameworks, and delivers prioritized improvement roadmaps with effort/impact analysis.

### Key Features

- **Framework-Grounded Evaluation**: All assessments bound to MQM, DQF, ISO 17100, ISO 12616, and Skopos Theory
- **Multi-Dimensional Scoring**: 8 comprehensive dimensions (Accuracy, Terminology, Fluency, Register, Domain Conventions, Locale Conventions, Consistency, Readability)
- **Evidence-Based Findings**: Every score supported by quoted evidence and framework citations
- **MQM Error Typology**: Structured error logging with severity-weighted categorization
- **Prioritized Roadmaps**: Effort/impact-ranked improvement recommendations with measurable success metrics
- **Self-Improving Knowledge Base**: Automated weekly updates from authoritative sources
- **Cluster Integration**: Shared sub-skills for reuse across design-creative-media cluster
- **Standardized Output**: JSON schema v1.0.0 for interoperability

---

## Table of Contents

- [Evaluation Frameworks](#evaluation-frameworks)
- [Scoring Dimensions](#scoring-dimensions)
- [Installation](#installation)
- [Usage](#usage)
- [Skill Architecture](#skill-architecture)
- [Quality Gates](#quality-gates)
- [Testing](#testing)
- [Cluster Integration](#cluster-integration)
- [Output Schema](#output-schema)
- [Knowledge Base](#knowledge-base)
- [Development](#development)
- [License](#license)

---

## Evaluation Frameworks

The skill uses five world-renowned, citable frameworks for defensible evaluation:

### MQM (Multidimensional Quality Metrics)
Error-typology-based quality scoring with hierarchical categorization (Accuracy, Fluency, Terminology, Design, Locale Convention, Verity) and four severity levels (Critical, Major, Minor, Trivial).

### DQF (TAUS Dynamic Quality Framework)
Use-case-calibrated quality models for different content types (Publishing, Internal Communication, Technical Documentation, User-Generated Content, Legal/Medical).

### ISO 17100:2015
International standard for translation services requirements covering translator competence (translation, linguistic, cultural, research, technical, domain) and process requirements (translation, review, verification).

### Skopos Theory
Purpose-driven translation framework where the Skopos (purpose) of the target text determines translation methods and functional equivalence over formal equivalence.

### ISO 12616:2022
Translation-oriented terminology standard covering term quality criteria (accuracy, consistency, clarity, currency, appropriateness) and terminology management processes.

---

## Scoring Dimensions

| Dimension | Description | Weight (Default) |
|-----------|-------------|------------------|
| **Accuracy** | No mistranslation, omission, or addition | 0.25 |
| **Terminology** | Domain-specific terms correct and consistent | 0.15 |
| **Fluency** | Natural phrasing and smooth flow | 0.15 |
| **Register & Style Fidelity** | Appropriate formality level and tone | 0.10 |
| **Domain Conventions** | Industry-standard patterns and formats | 0.10 |
| **Locale Conventions** | Date, number, currency formatting | 0.07 |
| **Consistency** | Uniform terminology and phrasing | 0.10 |
| **Readability** | Clear structure and accessibility | 0.07 |

Each dimension is scored 0-100 with explicit evidence and framework citation.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Claude Code CLI or compatible AI agent system

### Setup

1. Clone the repository:

```bash
git clone https://github.com/dungnotnull/translation-quality-evaluation-agent-skill.git
cd translation-quality-evaluation-agent-skill
```

2. Install Python dependencies:

```bash
pip install crawl4ai beautifulsoup4 requests
```

3. Verify installation:

```bash
python tests/test_runner.py --scenario 1
```

### Automated Knowledge Updates (Optional)

Set up weekly automated knowledge base updates:

```bash
# Edit crontab
crontab -e

# Add weekly cron job (Sundays at 02:00 UTC)
0 2 * * 0 cd /path/to/translation-quality-evaluation-agent-skill && python tools/knowledge_updater.py >> logs/cron.log 2>&1
```

See tools/cron-schedule.md for detailed configuration options.

---

## Usage

### Basic Usage

Invoke the skill through your AI agent system:

```
User: "Evaluate this translation for accuracy and terminology quality"

Source: "The patient should take 500mg of acetaminophen every 4-6 hours for pain."

Target: "El paciente debe tomar 500mg de acetaminofeno cada 4-6 horas para el dolor."
```

### Evaluation Modes

**Full Assessment**: Score all 8 dimensions with comprehensive findings

```
"Full assessment of this medical translation"
```

**Targeted Concern**: Focus on specific dimensions

```
"This translation feels awkward. Assess fluency and naturalness specifically."
```

**Benchmark Comparison**: Compare revised version against baseline

```
"Compare this revised translation against the original and show improvement per dimension"
```

### Example Output

The skill delivers:

1. **Executive Summary**: Overall score/band with top 3 findings
2. **Scorecard**: Per-dimension scores with evidence
3. **Detailed Findings**: Strengths and weaknesses with citations
4. **Error Log**: MQM-typed errors with severity and locations
5. **Prioritized Roadmap**: Quick wins / Major projects / Long-term
6. **Sources Cited**: All frameworks and references used

---

## Skill Architecture

### Harness Flow

```
User Input (Source, Target, Request)
    │
    ▼
Framework Selection (sub-evaluation-framework-selector)
    │
    ▼
Error Typology (sub-error-typology)
    │
    ▼
Scoring Engine (sub-scoring-engine)
    │
    ▼
Improvement Roadmap (sub-improvement-roadmap)
    │
    ▼
Quality Gates (5 validation checks)
    │
    ▼
Final Output (Scorecard + Roadmap)
```

### Sub-Skills

| Sub-Skill | Purpose | Tools |
|-----------|---------|-------|
| sub-evaluation-framework-selector | Select governing standards | Read, WebSearch, WebFetch |
| sub-error-typology | MQM error categorization | Read, WebSearch |
| sub-scoring-engine | Multi-dimensional scoring | Read, WebSearch |
| sub-improvement-roadmap | Prioritized recommendations | Read, Write |

### Shared Cluster Sub-Skills

The skill provides four shared sub-skills for cluster reuse:

- sub-error-detection: MQM-based error detection and categorization
- sub-terminology-validator: ISO 12616 terminology validation
- sub-consistency-checker: Multi-document consistency checking
- sub-style-analyzer: Skopos theory style and register analysis

See docs/cluster-integration.md for detailed reuse documentation.

---

## Quality Gates

The skill enforces five mandatory quality gates before output:

1. Every dimension has a numeric score AND evidence/justification
2. At least one named framework is explicitly cited
3. Every roadmap item has effort, impact, and a measurable success metric
4. Devil's-advocate review challenges top findings
5. All errors have MQM category, severity, and exact spans

**No gate is skippable** — output is withheld if any gate fails.

---

## Testing

### Running Tests

```bash
# Run all scenarios
python tests/test_runner.py --all

# Run specific scenario
python tests/test_runner.py --scenario 1

# Run functional scenarios only
python tests/test_runner.py --type functional

# Run with verbose output
python tests/test_runner.py --all --verbose

# Generate HTML report
python tests/test_runner.py --all --report
```

### Test Coverage

11 comprehensive scenarios covering:

- 5 functional scenarios (Full Assessment, Targeted Concern, Benchmark Loop, Multi-Document, Legal Precision)
- 6 adversarial/edge scenarios (Incomplete Input, Mixed Domain, Inconsistent Terms, Register Violation, Locale Errors, Offline Mode)

All 8 dimensions and all 5 quality gates are validated.

### Test Results

```
Summary: 11/11 scenarios passed
- All functional scenarios: PASS (5/5)
- All adversarial scenarios: PASS (6/6)
```

---

## Cluster Integration

### Design-Creative-Media Cluster

This skill is part of the design-creative-media cluster with standardized:

- Shared sub-skills for error detection, terminology validation, consistency checking, and style analysis
- JSON output schema (v1.0.0) for interoperability
- Reuse map and integration patterns
- Version management and governance

### Compatible Skills

Planned cluster skills that will reuse shared sub-skills:

- Content Quality Assessment
- Localization Quality Review
- Technical Writing Review

See docs/cluster-integration.md for complete integration documentation.

---

## Output Schema

### JSON Schema v1.0.0

Standardized JSON output for interoperability:

```json
{
  "schema_version": "1.0.0",
  "skill_id": 95,
  "skill_slug": "translation-quality-evaluation",
  "evaluation_timestamp": "2026-07-02T14:30:00Z",
  "dimensions": {
    "accuracy": {"score": 90, "evidence": ["..."], "framework": "MQM"},
    "terminology": {"score": 85, "evidence": ["..."], "framework": "MQM + ISO 12616"}
  },
  "overall_score": {
    "score": 89.1,
    "band": "Good"
  },
  "error_log": [...],
  "roadmap": {
    "quick_wins": [...],
    "major_projects": [...],
    "long_term": [...]
  }
}
```

See docs/scoring-output-schema.json for complete schema specification and docs/examples/valid-evaluation-output.json for example output.

---

## Knowledge Base

### SECOND-KNOWLEDGE-BRAIN.md

Comprehensive, self-improving knowledge base containing:

- Detailed MQM error typology with severity levels
- DQF use case categories and quality models
- ISO 17100 competence requirements
- Skopos theory and ISO 12616 standards
- Complete scoring rubrics for all 8 dimensions
- Key research papers and state-of-the-art methods
- Authoritative data sources and industry publications
- Framework selection matrix and weighting strategies

### Automated Updates

Weekly automated updates from authoritative sources:

- TAUS Quality (taus.net)
- MQM Framework (themqm.org)
- ISO Standards (iso.org)
- GALA Global (gala-global.org)
- ArXiv cs.CL (recent research)

Updates include deduplication, relevance scoring, and dated entries with citations.

---

## Development

### Project Status

All phases complete and production-ready:

| Phase | Status | Deliverables |
|-------|--------|--------------|
| Phase 0 | Complete | Frameworks, dimensions, sources |
| Phase 1 | Complete | 4 core sub-skills |
| Phase 2 | Complete | Main harness, quality gates |
| Phase 3 | Complete | Knowledge base, crawler, cron |
| Phase 4 | Complete | 11 test scenarios, test runner |
| Phase 5 | Complete | 4 shared sub-skills, schema, integration |

### File Structure

```
translation-quality-evaluation-agent-skill/
├── README.md
├── CLAUDE.md
├── PROJECT-detail.md
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md
├── SECOND-KNOWLEDGE-BRAIN.md
├── docs/
│   ├── cluster-integration.md
│   ├── scoring-output-schema.json
│   ├── scoring-output-schema-guide.md
│   └── examples/
│       └── valid-evaluation-output.json
├── skills/
│   ├── main.md
│   ├── sub-evaluation-framework-selector.md
│   ├── sub-error-typology.md
│   ├── sub-scoring-engine.md
│   ├── sub-improvement-roadmap.md
│   └── shared/
│       ├── sub-error-detection.md
│       ├── sub-terminology-validator.md
│       ├── sub-consistency-checker.md
│       └── sub-style-analyzer.md
├── tools/
│   ├── knowledge_updater.py
│   ├── cron-schedule.md
│   └── run_knowledge_update.sh
├── tests/
│   ├── test-scenarios.md
│   └── test_runner.py
└── logs/
    ├── knowledge_updater.log
    ├── test_results.log
    └── test_report.html
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Run test suite
5. Submit pull request

For shared sub-skill modifications, see docs/cluster-integration.md governance section.

---

## License

MIT License - see LICENSE file for details.

Free for open source and commercial use.

---

## Acknowledgments

- MQM Framework (themqm.org)
- TAUS DQF (taus.net)
- ISO Standards (iso.org)
- GALA Global (gala-global.org)
- Localization industry research community

---

## Contact

**Repository**: https://github.com/dungnotnull/translation-quality-evaluation-agent-skill

**Issues**: https://github.com/dungnotnull/translation-quality-evaluation-agent-skill/issues

**Skill ID**: 95
**Cluster**: design-creative-media
**Version**: 1.0.0

---

**Translation Quality Evaluation (specialized)** - Professional-grade translation quality assessment grounded in industry standards.

*Ready for production deployment and open source collaboration.*
