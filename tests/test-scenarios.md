# Test Scenarios — Translation Quality Evaluation (specialized)

This document defines comprehensive test scenarios for validating the Translation Quality Evaluation skill. Each scenario includes input, expected behavior, framework expectations, quality gates, and pass criteria.

## Overview

Total scenarios: 11
- Functional scenarios: 5
- Adversarial/edge scenarios: 6

All tests validate the harness, scoring, quality gates, and graceful degradation.

---

# Functional Scenarios

## Scenario 1: Full Assessment

**Type:** Functional - Core workflow validation

**Input:**
```
Source: "The patient should take 500mg of acetaminophen every 4-6 hours for pain. Do not exceed 3000mg daily."
Target: "El paciente debe tomar 500mg de acetaminofeno cada 4-6 horas para el dolor. No exceder 3000mg diarios."
Request: "Full assessment of this medical translation"
```

**Expected behavior:**
1. Parse source, target, and domain (medical)
2. Select MQM and ISO 17100 frameworks (accuracy-critical content)
3. Score all 8 dimensions with evidence
4. Highlight accuracy and terminology correctness findings
5. Deliver a prioritized improvement roadmap

**Frameworks expected in output:**
- MQM (Multidimensional Quality Metrics)
- ISO 17100 (translation services - medical domain)
- DQF (Life Sciences quality model)

**Quality gates checked:**
- Every dimension has numeric score and evidence
- Roadmap items have effort, impact, and measurable success metric
- At least one framework explicitly cited

**Pass criteria:**
- Output contains scorecard with all 8 dimensions
- Each dimension has a score (0-100) and at least one evidence quote
- Roadmap is structured with Quick wins / Major projects / Long-term
- No silent assumptions (unknowns are surfaced if present)

**Test execution:**
```bash
# Run test
python tests/test_runner.py --scenario 1
```

---

## Scenario 2: Targeted Concern

**Type:** Functional - Focused evaluation

**Input:**
```
Source: "Click the 'Submit' button to complete your order. The order will be processed within 24 hours."
Target: "Clickea el botón 'Enviar' para completar su orden. La orden será procesada dentro 24 horas."
Request: "This translation feels awkward. Assess fluency and naturalness specifically."
```

**Expected behavior:**
1. Parse source, target, and domain (software UI)
2. Identify fluency as primary concern
3. Apply MQM Fluency category and DQF Software quality model
4. Diagnose specific fluency issues (e.g., "clickea" vs "haga clic en", awkward phrasing)
5. Return focused, measurable fixes with effort/impact

**Frameworks expected in output:**
- MQM Fluency category (Grammar, Mechanics, Style)
- DQF Software content quality model

**Quality gates checked:**
- Fluency dimension scored with specific evidence
- Roadmap items are measurable (e.g., "Replace 'clickea' with 'haga clic en'")

**Pass criteria:**
- Output focuses on fluency without ignoring other dimensions
- Specific awkward phrases are quoted with source-target comparison
- Roadmap provides concrete alternatives (not just "improve fluency")

**Test execution:**
```bash
python tests/test_runner.py --scenario 2
```

---

## Scenario 3: Benchmark / Improvement Loop

**Type:** Functional - Comparison evaluation

**Input:**
```
Original translation (v1): "The software's features includes data analysis and report generation."
Revised translation (v2): "The software's features include data analysis and report generation."
Request: "Compare v2 against v1 and show improvement per dimension"
```

**Expected behavior:**
1. Parse both versions (v1 and v2)
2. Score v1 against framework
3. Score v2 against same framework
4. Show before/after delta per dimension
5. Update roadmap based on remaining weaknesses

**Frameworks expected in output:**
- MQM (Accuracy, Fluency categories)
- DQF (Technical documentation quality model)

**Quality gates checked:**
- Both versions scored on same rubric
- Delta clearly shown per dimension
- Updated roadmap based on v2 remaining issues

**Pass criteria:**
- Output shows v1 scores, v2 scores, and delta
- Improvement is quantified (e.g., "Fluency: 65 → 85 (+20)")
- Roadmap focuses on remaining issues in v2, not fixed issues from v1

**Test execution:**
```bash
python tests/test_runner.py --scenario 3
```

---

## Scenario 4: Multi-Document Consistency Check

**Type:** Functional - Cross-document validation

**Input:**
```
Document 1 (UI): "To save your changes, click the 'Save' button."
Document 2 (Help): "Press 'Save' to store your modifications."
Document 3 (Tutorial): "Select 'Save' for keeping your edits."
All translated to Spanish with different terms for "Save": 'Guardar', 'Almacenar', 'Conservar'
Request: "Check consistency across these three UI strings"
```

**Expected behavior:**
1. Parse all three documents
2. Identify inconsistency in "Save" translation
3. Score Consistency dimension (should be low due to variation)
4. Reference ISO 12616 terminology management standard
5. Provide roadmap item for standardizing terminology

**Frameworks expected in output:**
- MQM Terminology category (Inconsistency)
- ISO 12616 (Translation-oriented terminology)

**Quality gates checked:**
- Consistency dimension explicitly scored
- Inconsistency is identified and quantified
- Roadmap includes measurable fix (e.g., "Standardize 'Save' to 'Guardar' across all UI elements")

**Pass criteria:**
- Output identifies all three variants of "Save" with locations
- Consistency score reflects the severity (should be < 60)
- Roadmap prioritizes terminology standardization

**Test execution:**
```bash
python tests/test_runner.py --scenario 4
```

---

## Scenario 5: Legal Document Precision

**Type:** Functional - High-stakes domain

**Input:**
```
Source (contract clause): "The licensee shall not sublicense, assign, or transfer this agreement without prior written consent from the licensor."
Target: "El licenciatario no podrá sublicenciar, ceder o transferir este acuerdo sin consentimiento escrito previo del licenciador."
Request: "Verify legal accuracy and terminology"
```

**Expected behavior:**
1. Parse source and target (legal domain)
2. Apply MQM Accuracy and Terminology categories
3. Apply ISO 17100 legal translation competence requirements
4. Verify legal terms are translated correctly (sublicenciar, ceder, transferir)
5. Score with emphasis on accuracy and terminology (lower weights on fluency)

**Frameworks expected in output:**
- MQM (Accuracy, Terminology)
- ISO 17100 (Legal domain competence)
- Skopos theory (Legal equivalence requires formal precision)

**Quality gates checked:**
- Accuracy dimension scored highest priority
- Every legal term verified
- No silent assumptions about legal effect

**Pass criteria:**
- Accuracy score >= 90 if translation is correct
- Legal terms are explicitly validated
- Any deviation changes meaning (critical error flagged)

**Test execution:**
```bash
python tests/test_runner.py --scenario 5
```

---

# Adversarial / Edge Scenarios

## Scenario 6: Incomplete Input

**Type:** Edge case - Missing critical information

**Input:**
```
Request: "Evaluate this translation" (no source or target provided)
```

**Expected behavior:**
1. Intake sub-skill detects missing mandatory fields
2. Skill asks targeted clarifying questions:
   - "Please provide the source text"
   - "Please provide the target translation"
   - "What is the domain/subject matter?"
3. No score is produced from assumptions
4. Unknowns are explicitly listed

**Quality gates checked:**
- No score is generated without complete input
- Skill does not fabricate assessment

**Pass criteria:**
- No scorecard or roadmap is produced
- Skill explicitly asks for missing information
- Error message is clear and actionable

**Test execution:**
```bash
python tests/test_runner.py --scenario 6
```

---

## Scenario 7: Mixed-Domain Source

**Type:** Adversarial - Domain boundary testing

**Input:**
```
Source: "The API endpoint POST /users/create accepts a JSON payload with user credentials and returns a JWT token valid for 3600 seconds. The UI should display 'Account created successfully' after token validation."
Target: [Translation with mixed technical and UI elements]
Request: "Evaluate this translation that mixes API documentation and UI text"
```

**Expected behavior:**
1. Detect multiple domains within single text (technical API + UI)
2. Apply DQF technical content model to API parts
3. Apply DQF software content model to UI parts
4. Score each section with appropriate weighting
5. Note any inconsistencies in domain treatment

**Frameworks expected in output:**
- MQM (multiple categories: Accuracy, Terminology, Locale Convention)
- DQF (Technical + Software quality models)

**Quality gates checked:**
- Skill recognizes domain mixture
- Different parts scored with appropriate rubrics
- No single rubric applied incorrectly to entire text

**Pass criteria:**
- Output identifies the domain mixture
- Scoring accounts for different requirements (API vs UI)
- Roadmap differentiates fixes by domain

**Test execution:**
```bash
python tests/test_runner.py --scenario 7
```

---

## Scenario 8: Inconsistent Terminology

**Type:** Adversarial - Consistency testing

**Input:**
```
Source text with "software" appearing 10 times
Target text with "software" translated as: "software" (3x), "programa" (4x), "aplicación" (2x), "soft" (1x)
Request: "Evaluate terminology consistency"
```

**Expected behavior:**
1. Parse source and target
2. Identify "software" is translated with 4 different terms
3. Apply MQM Terminology (Inconsistency) and ISO 12616
4. Score Consistency dimension low (should be < 50)
5. Provide roadmap with specific recommendation for standardization

**Frameworks expected in output:**
- MQM Terminology category (Inconsistency)
- ISO 12616 (Term consistency management)

**Quality gates checked:**
- All instances of inconsistency are identified
- Consistency score reflects the severity
- Roadmap includes measurable standardization fix

**Pass criteria:**
- Output lists all 4 variants with locations/counts
- Consistency score is <= 50
- Roadmap prioritizes terminology standardization as high-impact

**Test execution:**
```bash
python tests/test_runner.py --scenario 8
```

---

## Scenario 9: Register Violation

**Type:** Adversarial - Register/style testing

**Input:**
```
Source: "The patient must adhere to the prescribed dosage regimen. Consult your physician if adverse effects occur." (formal medical)
Target: "Toma tus pastitas como te dije. Si te sientes mal, llama al doc." (informal colloquial)
Request: "Evaluate this translation"
```

**Expected behavior:**
1. Detect source register is formal/medical
2. Detect target register is informal/colloquial
3. Apply MQM Style category and Skopos theory
4. Score Register & Style Fidelity low (should be < 40)
5. Provide roadmap with specific register correction recommendations

**Frameworks expected in output:**
- MQM Fluency (Style)
- Skopos theory (Purpose determines appropriate register)
- DQF (Medical content requires formal register)

**Quality gates checked:**
- Register mismatch is identified
- Style dimension explicitly scored
- Roadmap provides specific register corrections

**Pass criteria:**
- Output identifies the register violation
- Register & Style Fidelity score is < 40
- Roadmap includes concrete recommendations (e.g., "Use formal address: 'usted' not 'tú'")

**Test execution:**
```bash
python tests/test_runner.py --scenario 9
```

---

## Scenario 10: Locale Convention Errors

**Type:** Adversarial - Locale format testing

**Input:**
```
Source: "The event starts on 01/05/2024 at 14:30. Tickets cost $1,250.00 and include a 3-course meal. Call +1 (555) 123-4567 to reserve."
Target: "El evento comienza el 01/05/2024 a las 14:30. Boletos cuestan $1.250,00 e incluyen comida de 3 platos. Llame +1 (555) 123-4567 para reservar." (Spanish locale)
Request: "Evaluate locale conventions"
```

**Expected behavior:**
1. Detect source is US locale
2. Detect target should be Spanish/Latin American locale
3. Apply MQM Locale Convention category
4. Identify errors:
   - Date format ambiguous (01/05 could be Jan 5 or May 1)
   - Number formatting: $1.250,00 uses European format but US dollars
   - No locale-specific phone format
5. Score Locale Conventions dimension

**Frameworks expected in output:**
- MQM Locale Convention category
- DQF (Internationalization considerations)

**Quality gates checked:**
- All locale errors are identified
- Locale Conventions dimension scored
- Roadmap includes specific format corrections

**Pass criteria:**
- Output identifies date ambiguity
- Output flags currency format mismatch
- Locale Conventions score reflects errors (< 60 if multiple errors)
- Roadmap includes correct format examples (e.g., "01/05/2024 → 5 de enero de 2024")

**Test execution:**
```bash
python tests/test_runner.py --scenario 10
```

---

## Scenario 11: Offline / Sources Unavailable

**Type:** Edge case - Graceful degradation

**Input:**
```
Request: "Evaluate this translation" with normal input
BUT: Simulate WebSearch/WebFetch tools are unavailable
```

**Expected behavior:**
1. Main harness detects external sources unavailable
2. Skill falls back to SECOND-KNOWLEDGE-BRAIN.md
3. Skill explicitly states the limitation
4. Reduced confidence is acknowledged
5. Evaluation proceeds with internal knowledge only

**Quality gates checked:**
- Skill degrades gracefully rather than failing
- Output explicitly signals degraded mode
- Framework citations are still provided (from internal knowledge)

**Pass criteria:**
- Output includes a clear notice: "External sources unavailable; using internal knowledge base"
- Scorecard and roadmap are still produced
- All quality gates still pass (using internal frameworks)
- No confidence is overstated

**Test execution:**
```bash
python tests/test_runner.py --scenario 11 --offline-mode
```

---

# Test Summary Matrix

| Scenario | Type | Key Dimension(s) | Primary Framework(s) | Critical Gate(s) |
|----------|------|------------------|---------------------|------------------|
| 1 - Full Assessment | Functional | All 8 dimensions | MQM, ISO 17100, DQF | All dimensions scored with evidence |
| 2 - Targeted Concern | Functional | Fluency, Naturalness | MQM Fluency, DQF | Specific fluency issues identified |
| 3 - Benchmark Loop | Functional | All dimensions (delta) | MQM, DQF | Delta shown per dimension |
| 4 - Multi-Doc Consistency | Functional | Consistency, Terminology | MQM Terminology, ISO 12616 | Inconsistency quantified |
| 5 - Legal Precision | Functional | Accuracy, Terminology | MQM, ISO 17100, Skopos | Legal accuracy verified |
| 6 - Incomplete Input | Edge | N/A (no evaluation) | N/A | No score generated |
| 7 - Mixed Domain | Adversarial | Multiple (by section) | MQM, DQF (multiple models) | Domains differentiated |
| 8 - Inconsistent Terms | Adversarial | Consistency, Terminology | MQM, ISO 12616 | All variants identified |
| 9 - Register Violation | Adversarial | Register & Style Fidelity | MQM, Skopos, DQF | Register mismatch flagged |
| 10 - Locale Errors | Adversarial | Locale Conventions | MQM Locale Convention | All format errors identified |
| 11 - Offline Mode | Edge | All 8 dimensions | Internal knowledge only | Degraded mode acknowledged |

---

# Test Execution Guide

## Running All Tests

```bash
# Run all scenarios
python tests/test_runner.py --all

# Run with detailed output
python tests/test_runner.py --all --verbose

# Run and generate report
python tests/test_runner.py --all --report
```

## Running Individual Tests

```bash
# Run specific scenario
python tests/test_runner.py --scenario 1

# Run specific scenarios
python tests/test_runner.py --scenario 1,3,5

# Run only functional scenarios
python tests/test_runner.py --type functional

# Run only adversarial scenarios
python tests/test_runner.py --type adversarial
```

## Interpreting Results

**Test Results Output:**
```
Scenario 1 (Full Assessment): PASS
  - Scorecard generated: YES
  - All dimensions scored: YES
  - Evidence provided: YES
  - Roadmap with metrics: YES
  - Framework cited: YES

Scenario 6 (Incomplete Input): PASS
  - No score generated: YES
  - Missing fields requested: YES
  - No assumptions made: YES

Summary: 11/11 scenarios passed
```

**Pass Criteria Checklist:**
- [ ] All functional scenarios pass (5/5)
- [ ] All adversarial scenarios pass (6/6)
- [ ] No false positives (scoring when should not)
- [ ] No false negatives (failing to score when should)
- [ ] All quality gates validated

---

# Expected Coverage

This test suite validates:

1. **Core workflow:** Intake → Framework selection → Scoring → Roadmap → Output
2. **Dimension coverage:** All 8 dimensions are scored and tested
3. **Framework coverage:** MQM, DQF, ISO 17100, ISO 12616, Skopos theory
4. **Quality gates:** All 5 quality gates are exercised
5. **Edge cases:** Incomplete input, mixed domains, offline mode
6. **Adversarial cases:** Inconsistency, register violation, locale errors
7. **Graceful degradation:** Fallback to internal knowledge

---

# Maintenance

**Add new scenarios:**
1. Define input, expected behavior, frameworks, gates, pass criteria
2. Add to test-scenarios.md
3. Update test_runner.py with scenario number
4. Update this summary matrix

**Update scenarios:**
1. Document change reason in this file
2. Update expected behavior if frameworks change
3. Verify pass criteria still valid

**Remove scenarios:**
1. Document reason for removal
2. Verify no coverage loss
3. Update summary matrix

---

**Last Updated:** 2026-07-02
**Test Version:** 2.0.0
**Total Scenarios:** 11 (5 functional, 6 adversarial/edge)
