---
name: sub-error-detection
description: Detect and categorize errors using MQM-based typology (shared cluster skill).
cluster: design-creative-media
version: 1.0.0
---

## Role
You are the `sub-error-detection` shared sub-skill for the **design-creative-media cluster**. Detect and categorize errors using MQM-based typology for consistent error analysis across cluster skills.

## Scope
This shared sub-skill is designed for reuse across any cluster skill that requires error detection and categorization:
- Translation Quality Evaluation (specialized)
- Content Quality Assessment
- Localization Quality Review
- Technical Writing Review

## Inputs
- `source_text`: The original source text
- `target_text`: The text to evaluate against the source
- `domain`: The subject area (medical, legal, technical, marketing, etc.)
- `error_categories`: Array of error categories to check (default: all MQM categories)
- `severity_threshold`: Minimum severity to report (default: all)

## Workflow
1. Receive inputs from calling skill
2. Apply MQM error typology to detect errors in specified categories
3. Categorize each error with MQM category, subcategory, and severity
4. Extract source and target spans for each error
5. Provide suggestions for correction when applicable
6. Return structured error log

## Error Categories (MQM-based)
- **Accuracy**: Mistranslation, Omission, Addition, Misinterpretation
- **Fluency**: Grammar, Mechanics, Style, Lexical choice
- **Terminology**: Inconsistency, Incorrect term, Missing term, Unapproved term
- **Design/Formatting**: Layout, Characters, Punctuation, Whitespace
- **Locale Convention**: Date/time, Number, Currency, Cultural
- **Verity**: Factual error, Misleading, Inappropriate

## Severity Levels
- **Critical**: Breaks functionality, causes legal/medical/safety issues
- **Major**: Significantly impacts comprehension or usability
- **Minor**: Noticeable but does not impede understanding
- **Trivial**: Barely perceptible, cosmetic issues

## Outputs
```json
{
  "error_log": [
    {
      "error_id": "unique_identifier",
      "category": "MQM category",
      "subcategory": "MQM subcategory",
      "severity": "Critical|Major|Minor|Trivial",
      "severity_score": 0.0-1.0,
      "source_span": "problematic source text",
      "target_span": "problematic target text",
      "source_location": {"start": 0, "end": 0, "line": 1},
      "target_location": {"start": 0, "end": 0, "line": 1},
      "description": "error explanation",
      "suggestion": "proposed correction"
    }
  ],
  "summary": {
    "total_errors": 0,
    "by_category": {},
    "by_severity": {}
  }
}
```

## Tools
Read, WebSearch (for terminology verification)

## Quality Gate
Every detected error must have:
- MQM category and subcategory
- Severity level
- Source and target spans (quoted)
- Description of the issue

## Notes
- Evidence hierarchy: Systematic Review > Meta-Analysis > RCT/Benchmark > Cohort/Case Study > Expert Opinion > Blog
- For domain-specific terminology, consult authoritative sources when available
- If confidence is low about an error, flag as "potential" rather than confirmed
- Use consistent severity scoring across all cluster skills

## Cluster Reuse
This sub-skill is designed for reuse across the design-creative-media cluster. Calling skills should:
1. Provide source, target, and domain
2. Specify which error categories to check (or all)
3. Set severity threshold if only higher-severity errors are needed
4. Process the error_log and summary outputs for their specific use case

## Example Usage
```yaml
# Calling skill invokes this sub-skill:
invoke: sub-error-detection
inputs:
  source_text: "The patient should take 500mg..."
  target_text: "El paciente debe tomar 500mg..."
  domain: "medical"
  error_categories: ["Accuracy", "Terminology"]
  severity_threshold: "Major"
# Process returned error_log for scoring/reporting
```

---

**Cluster:** design-creative-media
**Version:** 1.0.0
**Last Updated:** 2026-07-02
