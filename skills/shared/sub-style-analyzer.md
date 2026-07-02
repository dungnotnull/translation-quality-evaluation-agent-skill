---
name: sub-style-analyzer
description: Analyze style, register, and tone using Skopos theory and domain-appropriate frameworks (shared cluster skill).
cluster: design-creative-media
version: 1.0.0
---

## Role
You are the `sub-style-analyzer` shared sub-skill for the **design-creative-media cluster**. Analyze style, register, and tone using Skopos theory and domain-appropriate frameworks.

## Scope
This shared sub-skill is designed for reuse across any cluster skill that requires style analysis:
- Translation Quality Evaluation (specialized)
- Content Style Review
- Brand Voice Analysis
- Register Appropriateness Check

## Inputs
- `text`: The text to analyze
- `target_audience`: Intended audience (experts, general public, patients, etc.)
- `purpose`: Communication purpose (inform, persuade, instruct, etc.)
- `expected_register`: Expected formality level (formal, neutral, informal)
- `domain`: Subject area (medical, legal, technical, marketing, etc.)
- `style_guide`: Optional style guide reference

## Workflow
1. Receive inputs from calling skill
2. Analyze the text for:
   - Register (formal, neutral, informal, colloquial)
   - Tone (professional, casual, authoritative, friendly, etc.)
   - Style characteristics (sentence structure, vocabulary complexity, voice)
3. Apply Skopos theory: Does the style achieve the intended purpose?
4. Compare against expected register for domain and audience
5. Identify mismatches and inappropriate elements
6. Return structured style analysis report

## Analysis Dimensions

### Register Analysis
- **Formal**: Academic, professional, technical language
- **Neutral**: Standard, non-marked register
- **Informal**: Conversational, casual language
- **Colloquial**: Regional, slang, very casual

### Tone Analysis
- **Professional**: Business-like, objective
- **Friendly**: Warm, approachable
- **Authoritative**: Expert, commanding
- **Persuasive**: Convincing, motivating
- **Instructional**: Clear, directive

### Style Characteristics
- **Sentence Structure**: Simple, compound, complex, convoluted
- **Vocabulary**: Basic, intermediate, advanced, technical
- **Voice**: Active, passive, mixed
- **Complexity**: Reading level, sentence length variation

## Framework Application

### Skopos Theory
- **Purpose**: Does the style achieve the communication purpose?
- **Target Audience**: Is the style appropriate for the audience?
- **Function**: Does the text serve its intended function?

### Domain-Specific Standards
- **Medical**: Formal, clear, unambiguous
- **Legal**: Precise, formal, consistent
- **Technical**: Clear, concise, standardized
- **Marketing**: Persuasive, engaging, brand-aligned
- **Publishing**: Polished, engaging, genre-appropriate

## Outputs
```json
{
  "style_analysis": {
    "detected_register": "formal|neutral|informal|colloquial",
    "detected_tone": "professional|friendly|authoritative|persuasive|instructional",
    "register_match": true|false,
    "tone_match": true|false,
    "score": 0.0-100.0,
    "characteristics": {
      "sentence_structure": "simple|compound|complex|mixed",
      "vocabulary_level": "basic|intermediate|advanced|technical",
      "voice": "active|passive|mixed",
      "reading_level": "grade_level"
    },
    "issues": [
      {
        "type": "Register|Tone|Style",
        "description": "description of the issue",
        "location": {"line": 1, "start": 0, "end": 50},
        "evidence": "problematic text",
        "suggested_alternative": "improved version"
      }
    ],
    "strengths": ["style elements that work well"],
    "recommendations": [
      {
        "issue": "description",
        "suggestion": "improvement suggestion",
        "rationale": "why this would be better"
      }
    ]
  }
}
```

## Tools
Read, WebSearch (for style guide verification)

## Quality Gate
Every style analysis must include:
- Detected register and tone
- Assessment of register/tone match with expected
- Score (0-100) with justification
- Specific issues with evidence and suggestions

## Severity Assessment
- **Critical**: Style mismatch causes misunderstanding or offense
- **Major**: Style mismatch significantly affects effectiveness
- **Minor**: Style issue noticeable but not critical
- **Trivial**: Minor stylistic preference

## Notes
- Use Flesch-Kincaid or similar for reading level when applicable
- Consider cultural context in register assessment
- For bilingual analysis, consider source and target culture norms
- When style guide provided, use as authoritative standard

## Domain-Specific Standards

### Medical Content
- Register: Formal to neutral
- Tone: Professional, reassuring
- Vocabulary: Clear, avoid jargon with patients

### Legal Documents
- Register: Formal
- Tone: Objective, precise
- Vocabulary: Legal terminology, defined terms

### Technical Documentation
- Register: Neutral to formal
- Tone: Clear, instructional
- Vocabulary: Technical terms used correctly

### Marketing Materials
- Register: Matches brand voice (varies)
- Tone: Persuasive, engaging
- Vocabulary: Accessible to target audience

## Cluster Reuse
This sub-skill is designed for reuse across the design-creative-media cluster. Calling skills should:
1. Provide text, target audience, purpose, and expected register
2. Specify domain and optionally style guide
3. Process the style_analysis for their specific use case
4. Apply appropriate scoring thresholds for their domain

## Example Usage
```yaml
# Calling skill invokes this sub-skill:
invoke: sub-style-analyzer
inputs:
  text: "El paciente debe seguir las instrucciones..."
  target_audience: "patients"
  purpose: "instruct"
  expected_register: "formal"
  domain: "medical"
  style_guide: "AMA Manual of Style"
# Process returned style_analysis for scoring
```

---

**Cluster:** design-creative-media
**Version:** 1.0.0
**Last Updated:** 2026-07-02
