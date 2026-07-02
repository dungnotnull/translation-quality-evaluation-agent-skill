# Scoring Output Schema Guide

## Overview

The Translation Quality Evaluation skill outputs evaluation results in a standardized JSON format defined by `scoring-output-schema.json`. This schema enables interoperability across the design-creative-media cluster of skills.

**Schema Version:** 1.0.0
**Schema ID:** `https://skills.design-creative-media.cluster/schemas/translation-quality-scoring/v1.0.0.json`

## Schema Purpose

1. **Interoperability:** Downstream skills can parse and process evaluation results consistently
2. **Validation:** JSON schema validation ensures all required fields are present
3. **Extensibility:** Versioned schema allows for future enhancements without breaking compatibility
4. **Integration:** Enables integration with external tools and pipelines

## Required Fields

Every evaluation output MUST include:

- `schema_version`: Schema version (e.g., "1.0.0")
- `skill_id`: Unique skill identifier (95 for this skill)
- `skill_slug`: Human-readable identifier ("translation-quality-evaluation")
- `evaluation_timestamp`: ISO 8601 timestamp
- `source_language`: ISO 639-1 code (e.g., "en")
- `target_language`: ISO 639-1 code (e.g., "es")
- `domain`: Content domain (medical, legal, technical, etc.)
- `frameworks`: Array of evaluation frameworks used
- `dimensions`: Object with all 8 dimension scores
- `overall_score`: Overall weighted score and band
- `quality_gates_passed`: Array of passed quality gates
- `roadmap`: Improvement roadmap with Quick wins / Major projects / Long-term

## Dimension Scoring

All 8 dimensions MUST be scored:

```json
{
  "dimensions": {
    "accuracy": {
      "score": 85,
      "evidence": ["No significant mistranslations found", "All key information preserved"],
      "framework": "MQM",
      "weight": 0.35
    },
    "terminology": {
      "score": 90,
      "evidence": ["Medical terms translated correctly", "Consistent use of 'acetaminofén'"],
      "framework": "MQM + ISO 12616",
      "weight": 0.20
    },
    "fluency": {
      "score": 75,
      "evidence": ["Some awkward phrasing in paragraph 3"],
      "framework": "MQM",
      "weight": 0.15
    },
    "register": {
      "score": 85,
      "evidence": ["Appropriate formal register maintained"],
      "framework": "Skopos",
      "weight": 0.10
    },
    "domain_conventions": {
      "score": 80,
      "evidence": ["Medical document conventions followed"],
      "framework": "ISO 17100",
      "weight": 0.08
    },
    "locale_conventions": {
      "score": 70,
      "evidence": ["Date format needs adjustment: 01/05/2024 ambiguous"],
      "framework": "MQM",
      "weight": 0.07
    },
    "consistency": {
      "score": 85,
      "evidence": ["Terminology consistent throughout"],
      "framework": "MQM",
      "weight": 0.10
    },
    "readability": {
      "score": 80,
      "evidence": ["Clear sentence structure", "Appropriate reading level"],
      "framework": "DQF",
      "weight": 0.05
    }
  }
}
```

## Error Log Structure

Errors are logged with MQM-typed categorization:

```json
{
  "error_log": [
    {
      "error_id": "err_001",
      "category": "Accuracy",
      "subcategory": "Mistranslation",
      "severity": "Major",
      "severity_score": 0.7,
      "source_span": "The patient should take 500mg",
      "target_span": "El paciente debe tomar 500mg",
      "source_location": {
        "start": 0,
        "end": 28,
        "line": 1
      },
      "target_location": {
        "start": 0,
        "end": 27,
        "line": 1
      },
      "description": "Dosage instruction potentially ambiguous",
      "suggestion": "Clarify: 'El paciente debe tomar exactamente 500mg'"
    }
  ]
}
```

## Roadmap Structure

The roadmap is organized by effort/impact categories:

```json
{
  "roadmap": {
    "quick_wins": [
      {
        "recommendation": "Standardize date format to DD/MM/YYYY",
        "affected_dimensions": ["locale_conventions"],
        "effort": "Low",
        "impact": "Medium",
        "priority_score": 0.5,
        "success_metric": "Locale conventions score increases to 90+",
        "framework": "MQM Locale Convention"
      }
    ],
    "major_projects": [
      {
        "recommendation": "Review and standardize all medical terminology",
        "affected_dimensions": ["terminology", "consistency"],
        "effort": "High",
        "impact": "High",
        "priority_score": 1.0,
        "success_metric": "Terminology score > 90, Consistency score > 95",
        "framework": "ISO 12616"
      }
    ],
    "long_term": [
      {
        "recommendation": "Implement terminology management system",
        "affected_dimensions": ["terminology", "consistency"],
        "effort": "High",
        "impact": "High",
        "priority_score": 1.0,
        "success_metric": "Zero terminology inconsistencies in future documents",
        "framework": "ISO 12616"
      }
    ]
  }
}
```

## Quality Gates

Quality gates track which validation checks passed:

```json
{
  "quality_gates_passed": [
    "Every dimension has numeric score and evidence",
    "At least one framework explicitly cited",
    "Roadmap items have effort, impact, and measurable success metric",
    "Devil's-advocate review completed"
  ],
  "quality_gates_failed": []
}
```

## Framework References

All frameworks used must be cited:

```json
{
  "frameworks": [
    {
      "name": "MQM",
      "version": "2022",
      "citation": "https://themqm.org",
      "application": "Used MQM error typology for error categorization and dimension scoring"
    },
    {
      "name": "ISO 17100",
      "version": "2015",
      "citation": "https://www.iso.org/standard/59149.html",
      "application": "Applied ISO 17100 competence requirements for medical domain evaluation"
    }
  ]
}
```

## Validation

### JSON Schema Validation

Use a JSON schema validator to ensure outputs conform:

```bash
# Using ajv (npm install -g ajv-cli)
ajv validate -s docs/scoring-output-schema.json -d evaluation_output.json

# Using Python jsonschema
pip install jsonschema
python -m jsonschema -i evaluation_output.json docs/scoring-output-schema.json
```

### Example Valid Output

See `docs/examples/valid-evaluation-output.json` for a complete example of valid output.

## Integration with Other Skills

### Consuming Evaluation Results

Other skills can parse evaluation results:

```python
import json

def load_evaluation_result(json_file):
    with open(json_file) as f:
        result = json.load(f)

    # Verify schema version
    assert result['schema_version'].startswith('1.')

    # Access overall score
    overall_score = result['overall_score']['score']
    quality_band = result['overall_score']['band']

    # Access dimension scores
    accuracy_score = result['dimensions']['accuracy']['score']

    # Access roadmap
    quick_wins = result['roadmap']['quick_wins']

    return result
```

### Aggregating Multiple Evaluations

Compare evaluations over time:

```python
def compare_evaluations(eval1, eval2):
    comparison = {
        'timestamp_delta': eval2['evaluation_timestamp'] - eval1['evaluation_timestamp'],
        'score_delta': eval2['overall_score']['score'] - eval1['overall_score']['score'],
        'dimension_deltas': {}
    }

    for dim in eval1['dimensions']:
        delta = eval2['dimensions'][dim]['score'] - eval1['dimensions'][dim]['score']
        comparison['dimension_deltas'][dim] = delta

    return comparison
```

## Schema Versioning

The schema uses semantic versioning:

- **Major (X.0.0):** Breaking changes, not backward compatible
- **Minor (0.X.0):** New features, backward compatible
- **Patch (0.0.X):** Bug fixes, documentation

### Handling Multiple Versions

Skills should support the last two major versions:

```python
def validate_evaluation_result(result):
    schema_version = result.get('schema_version', '1.0.0')
    major_version = int(schema_version.split('.')[0])

    if major_version == 1:
        schema = load_schema('v1.0.0')
    elif major_version == 2:
        schema = load_schema('v2.0.0')
    else:
        raise ValueError(f"Unsupported schema version: {schema_version}")

    return validate(result, schema)
```

## Extending the Schema

For cluster-specific extensions, use the `metadata` field:

```json
{
  "metadata": {
    "evaluator": "Translation Quality Evaluation skill v1.0.0",
    "evaluation_duration_ms": 1250,
    "confidence": 0.9,
    "confidence_explanation": "High confidence based on clear source and target text",
    "notes": [
      "Source text was well-structured",
      "Target text showed consistent terminology"
    ],
    "custom_fields": {
      "cluster_specific": "value"
    }
  }
}
```

## Common Pitfalls

1. **Missing evidence:** Every dimension score must have at least one evidence string
2. **Wrong language codes:** Use ISO 639-1 (two-letter codes), not full names
3. **Invalid severity values:** Must be one of: Critical, Major, Minor, Trivial
4. **Missing framework citation:** Each framework must have name, version, and citation
5. **Roadmap items without metrics:** Every roadmap item needs a measurable success metric

## Support

For schema questions or issues:
- Check this guide
- Review `docs/scoring-output-schema.json`
- See `docs/examples/valid-evaluation-output.json`
- Consult cluster integration documentation

---

**Last Updated:** 2026-07-02
**Schema Version:** 1.0.0
