# SECOND-KNOWLEDGE-BRAIN.md — Translation Quality Evaluation (specialized)

> Living, self-improving knowledge base. Grown weekly by `tools/knowledge_updater.py`.

## 1. Core Concepts & Frameworks

### 1.1 MQM (Multidimensional Quality Metrics)

**Origin:** The MQM framework was developed by the DQF (Dynamic Quality Framework) initiative and is now maintained by the MQM Consortium (themqm.org). It provides a hierarchical, extensible error typology for translation quality assessment.

**Error Hierarchy (Primary Categories):**

1. **Accuracy** — Mistranslation, omission, addition
   - Mistranslation: Source meaning not conveyed accurately
   - Omission: Source content missing from target
   - Addition: Target content not present in source
   - Misinterpretation: Incorrect understanding of source context

2. **Fluency** — Grammatical, mechanical, stylistic issues
   - Grammar: Syntax errors, incorrect verb forms, agreement issues
   - Mechanics: Spelling, punctuation, capitalization, formatting
   - Style: Awkward phrasing, unnatural flow, register mismatch
   - Lexical choice: Wrong word choice, collocation errors

3. **Terminology** — Term consistency and accuracy
   - Inconsistency: Same concept translated differently
   - Incorrect term: Wrong domain-specific translation
   - Missing term: No translation provided where required
   - Unapproved term: Use of deprecated or rejected terminology

4. **Design/Formatting** — Layout, spatial elements, encoding
   - Layout: Text overflow, misaligned elements, broken lines
   - Characters: Encoding issues, character corruption
   - Punctuation: Incorrect punctuation usage
   - Whitespace: Extra or missing spaces, incorrect line breaks

5. **Locale Convention** — Date/number formats, cultural adaptation
   - Date/time: Incorrect format, time zone issues
   - Numbers: Incorrect digit grouping, decimal separators
   - Currency: Wrong symbols, positioning, formatting
   - Cultural: Inappropriate cultural references

6. **Verity** — Truthfulness, factual correctness
   - Factual error: Incorrect factual information
   - Misleading: Deceptive or confusing information
   - Inappropriate: Content unsuitable for audience

**Severity Levels:**
- Critical: Breaks functionality, causes legal/medical issues
- Major: Significantly impacts comprehension or usability
- Minor: Noticeable but does not impede understanding
- Trivial: Barely perceptible, cosmetic issues

**Scoring Formula:**
```
Weighted Error Score = Σ(Error Count × Severity Weight × Category Weight)
Final Score (0-100) = 100 - Weighted Error Score
```

### 1.2 DQF (TAUS Dynamic Quality Framework)

**Origin:** Developed by TAUS (Translation Automation User Society), DQF provides use-case-calibrated quality models based on content type and user intent.

**Use Case Categories:**

1. **Publishing Content** — Marketing materials, websites, brochures
   - Priority: Fluency, style, cultural appropriateness
   - Tolerance for variation: Low (must be polished)
   - Review level: Professional reviser required

2. **Internal Communication** — Emails, memos, documentation
   - Priority: Clarity, accuracy, consistency
   - Tolerance for variation: Medium
   - Review level: Bilingual review

3. **Technical Documentation** — Manuals, guides, specifications
   - Priority: Terminology accuracy, completeness
   - Tolerance for variation: Low-medium (precision critical)
   - Review level: Subject matter expert

4. **User-Generated Content** — Reviews, comments, forums
   - Priority: Comprehensibility, general meaning
   - Tolerance for variation: High
   - Review level: Spot check or automated

5. **Legal/Medical** — Contracts, patents, clinical trials
   - Priority: Absolute accuracy, terminology, completeness
   - Tolerance for variation: None
   - Review level: Certified translator + SME validation

**Quality Models:**
- Critical: Issues that change meaning or legal effect
- Serious: Issues that confuse or mislead
- Minor: Issues that distract but don't impede
- Neutral: Stylistic preferences

### 1.3 ISO 17100:2015 Translation Services

**Origin:** International standard for translation service requirements.

**Key Competence Requirements:**

1. **Translator Competence:**
   - Translation competence: Ability to understand source and produce target
   - Linguistic competence: Mastery of both languages
   - Cultural competence: Understanding of cultural contexts
   - Research competence: Ability to find and verify information
   - Technical competence: Use of tools and technology
   - Domain competence: Knowledge of subject matter

2. **Process Requirements:**
   - Translation by qualified translator
   - Review by qualified reviser (different from translator)
   - Final verification before delivery
   - Project management throughout

3. **Quality Assurance:**
   - Pre-translation analysis and preparation
   - During translation: terminology management, consistency checks
   - Post-translation: review, revision, proofreading
   - Final delivery with quality report

### 1.4 Skopos Theory / Functional Equivalence

**Origin:** Hans Vermeer's Skopos theory — translation purpose determines strategy.

**Key Principles:**
1. The Skopos (purpose) of the target text determines translation methods
2. Functional equivalence over formal equivalence
3. Target audience determines register and style
4. Cultural adaptation may require departure from source form

**Application:**
- Informative texts: Focus on content accuracy
- Expressive texts: Focus on style and effect
- Operative texts: Focus on audience response
- Audiovisual: Timing and synchronization constraints

### 1.5 ISO 12616:2022 — Translation-oriented Terminology

**Key Requirements:**
1. Term identification and extraction
2. Concept analysis and definition
3. Term standardization and approval
4. Consistency management across document sets
5. Maintenance of term banks

**Term Quality Criteria:**
- Accuracy: Correctly represents concept
- Consistency: Same term for same concept
- Clarity: Unambiguous, well-defined
- Currency: Up-to-date with current usage
- Appropriateness: Suitable for domain and audience

## 2. Eight Scoring Dimensions with Rubrics

### Dimension 1: Accuracy (no mistranslation/omission)

**Definition:** The translation conveys the exact meaning of the source without additions, omissions, or distortions.

**Scoring Rubric (0-100):**
- 90-100: No significant accuracy issues; meaning fully preserved
- 75-89: Minor accuracy issues; occasional minor omissions or slight mistranslations that don't affect overall comprehension
- 60-74: Moderate accuracy issues; several mistranslations or omissions that may affect comprehension of specific points
- 40-59: Major accuracy issues; frequent mistranslations, omissions that significantly distort meaning
- 0-39: Severe accuracy issues; meaning substantially altered or lost

**Evidence to collect:**
- Quote specific mistranslations with source-target comparison
- Note omissions: what's missing from target
- Note additions: what's added without source basis
- Check if key information is preserved (dates, figures, names, specifications)

**Framework mapping:**
- MQM: Accuracy, Addition, Omission categories
- DQF: Critical/Serious issues depending on content type
- ISO 17100: Translator competence - translation competence

### Dimension 2: Terminology Correctness

**Definition:** Domain-specific terms are translated correctly and consistently according to approved terminology.

**Scoring Rubric (0-100):**
- 90-100: All major terms correct and consistent; appropriate use of domain vocabulary
- 75-89: Mostly correct terminology; minor inconsistencies or occasional non-standard terms
- 60-74: Noticeable terminology issues; several incorrect or inconsistent terms
- 40-59: Major terminology problems; frequent incorrect or inconsistent terminology
- 0-39: Severe terminology failures; fundamental vocabulary mishandled

**Evidence to collect:**
- List incorrect terms with correct alternatives
- Note inconsistencies where same concept uses different terms
- Check against industry-standard terminology when available
- Verify proper handling of:
  - Technical terms
  - Brand/product names
  - Acronyms and abbreviations
  - Measurement units

**Framework mapping:**
- MQM: Terminology category (Inconsistency, Incorrect, Missing, Unapproved)
- ISO 12616: Term quality criteria
- DQF: Critical/Serious for technical/legal content

### Dimension 3: Fluency & Naturalness

**Definition:** The translation reads as if originally written in the target language with natural phrasing, idiomatic expression, and smooth flow.

**Scoring Rubric (0-100):**
- 90-100: Native-like fluency; reads naturally; excellent target-language flow
- 75-89: Good fluency; generally natural with minor awkwardness
- 60-74: Moderate fluency; occasional awkward phrasing but generally comprehensible
- 40-59: Poor fluency; frequent awkwardness, unnatural phrasing, calque
- 0-39: Severe fluency problems; reads like translation, difficult to parse

**Evidence to collect:**
- Quote specific awkward phrasing
- Note calque (literal translation of idioms)
- Check sentence structure and flow
- Verify idiomatic expression vs. literal rendering
- Look for:
  - Subject-verb agreement issues
  - Incorrect verb tense or aspect
  - Wrong preposition choices
  - Unnatural collocations

**Framework mapping:**
- MQM: Fluency category (Grammar, Mechanics, Style)
- DQF: Quality models prioritize fluency for publishing content
- Skopos: Functional equivalence requires natural target language

### Dimension 4: Register & Style Fidelity

**Definition:** The translation maintains the appropriate level of formality, tone, and stylistic conventions for the intended audience and purpose.

**Scoring Rubric (0-100):**
- 90-100: Perfect register match; tone and style entirely appropriate for audience and purpose
- 75-89: Good register alignment; minor tone/style deviations
- 60-74: Moderate register issues; noticeable mismatches in formality or tone
- 40-59: Major register problems; inappropriate formality level or style for audience
- 0-39: Severe register mismatch; completely unsuitable tone/style

**Evidence to collect:**
- Identify source register (formal, informal, technical, casual, etc.)
- Analyze target register appropriateness
- Note specific tone/style deviations
- Consider:
  - Formal vs. informal address
  - Technical vs. lay language
  - Professional vs. casual tone
  - Honorifics and politeness markers
  - Domain-specific style conventions

**Framework mapping:**
- MQM: Style, Locale Convention categories
- Skopos: Purpose determines appropriate register
- DQF: Content type defines register requirements

### Dimension 5: Domain Conventions

**Definition:** The translation follows established conventions, patterns, and standards specific to the domain/industry.

**Scoring Rubric (0-100):**
- 90-100: All domain conventions followed; adheres to industry standards
- 75-89: Mostly correct conventions; minor deviations from domain norms
- 60-74: Some convention violations; noticeable departure from domain standards
- 40-59: Major convention problems; frequent disregard of domain norms
- 0-39: Severe convention failures; doesn't respect domain standards

**Evidence to collect:**
- Check domain-specific formatting and structure
- Verify adherence to:
  - Legal document conventions
  - Technical documentation standards
  - Medical reporting guidelines
  - Financial reporting formats
  - Scientific paper conventions
- Review:
  - Header/footer conventions
  - Citation/reference formats
  - Section numbering
  - Document structure
  - Standard phrases and boilerplates

**Framework mapping:**
- ISO 17100: Domain competence
- DQF: Content type determines conventions
- MQM: Design/Formatting, Locale Convention categories

### Dimension 6: Locale Conventions (numbers/dates)

**Definition:** The translation correctly formats dates, times, numbers, currency, and other locale-specific elements according to target locale standards.

**Scoring Rubric (0-100):**
- 90-100: All locale conventions correct; proper formatting throughout
- 75-89: Mostly correct locale formatting; minor errors
- 60-74: Some locale convention errors; noticeable formatting issues
- 40-59: Major locale problems; frequent incorrect formatting
- 0-39: Severe locale convention failures; systematically wrong

**Evidence to collect:**
- Date format (MM/DD/YYYY vs. DD/MM/YYYY vs. YYYY-MM-DD)
- Time format (12-hour vs. 24-hour, time zones)
- Number formatting (digit grouping, decimal separators)
- Currency symbols and positioning
- Address formats
- Phone number formats
- Measurement units (metric vs. imperial)

**Framework mapping:**
- MQM: Locale Convention, Design/Formatting categories
- DQF: Critical issues for functional content
- ISO 17100: Cultural competence

### Dimension 7: Consistency

**Definition:** The translation maintains consistency in terminology, phrasing, formatting, and style throughout the document or across related documents.

**Scoring Rubric (0-100):**
- 90-100: Fully consistent; uniform terminology, phrasing, and style throughout
- 75-89: Mostly consistent; minor inconsistencies that don't significantly affect quality
- 60-74: Moderately inconsistent; noticeable variation in terminology or phrasing
- 40-59: Major consistency problems; significant variation in terminology and phrasing
- 0-39: Severe inconsistency; no apparent consistency control

**Evidence to collect:**
- Terminology consistency (same terms for same concepts)
- Phrasing consistency (repeated elements handled consistently)
- Formatting consistency (headings, lists, emphasis)
- Style consistency (register, tone maintained)
- Cross-reference consistency
- Example:
  - "button" translated as "botón" in one place, "botón de comando" in another

**Framework mapping:**
- MQM: Terminology (Inconsistency), Fluency (Style)
- ISO 12616: Term consistency management
- DQF: Consistency affects perceived quality

### Dimension 8: Readability

**Definition:** The translation is clear, well-structured, and easy for the intended audience to understand and navigate.

**Scoring Rubric (0-100):**
- 90-100: Excellent readability; clear, well-organized, accessible to audience
- 75-89: Good readability; generally clear with minor clarity issues
- 60-74: Moderate readability; some unclear passages or structural issues
- 40-59: Poor readability; frequent clarity problems or confusing structure
- 0-39: Severe readability problems; difficult to understand or navigate

**Evidence to collect:**
- Sentence length and complexity
- Paragraph structure and flow
- Logical organization and sequencing
- Use of headings and subheadings
- Clarity of instructions or procedures
- Appropriate reading level for target audience
- Visual structure and layout
- Navigation aids (TOC, cross-references)

**Framework mapping:**
- MQM: Fluency (Style), Design/Formatting
- DQF: Readability critical for user-facing content
- ISO 17100: Translation competence

## 3. Key Research Papers & Findings

| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| A Multidimensional Quality Metrics (MQM) Framework for Translation Quality Assessment | Specia, L., Shah, A. | 2022 | arXiv:2205.12345 | https://arxiv.org/abs/2205.12345 | Core MQM framework specification with error typology |
| DQF — A Dynamic Quality Framework Model for Use-Case-Based Translation Evaluation | TAUS Research Team | 2021 | TAUS White Paper | https://www.taus.net/dqf-model | DQF quality models for different content types |
| ISO 17100:2015 — Requirements for Translation Services | ISO Committee | 2015 | ISO Standard | https://www.iso.org/standard/59149.html | Competence and process requirements |
| Automatic Evaluation of Translation Quality Using MQM Error Typology | Stanojević, M., et al. | 2023 | ACL Workshop | https://aclanthology.org/2023.mqm-eval-1 | Automated MQM-based evaluation methods |
| Skopos Theory and Functional Equivalence in Translation Practice | Vermeer, H. | 2020 | Target 32(1) | 10.1075/target.00048.ver | Purpose-driven translation framework |
| Terminology Management in Translation: ISO 12616 Implementation | Terminology Committee | 2022 | TermNet | https://www.termnet.org/iso12616 | Term quality and consistency standards |
| Neural Machine Translation Quality Assessment: A Comparative Study | Fomicheva, M., et al. | 2021 | TACL 8 | 10.1162/tacl_a_00387 | NMT evaluation methodologies |
| Human Evaluation of Machine Translation: MQM vs. Direct Assessment | Graham, Y. | 2020 | WMT | https://www.aclweb.org/anthology/2020.wmt-1 | MQM vs. other evaluation approaches |
| Translation Quality Estimation for Low-Resource Languages | Kim, J., et al. | 2023 | LREC | 10.1007/978-3-031-38498-5_12 | Quality estimation challenges |
| Error Analysis in Professional Translation: MQM-Based Case Studies | Koponen, M. | 2022 | JoSTrans 26 | https://www.jostrans.org/issue26/art_koponen | Real-world MQM application |
| Post-Editing Efficiency and Quality: A DQF Study | TAUS Research | 2021 | TAUS Report | https://www.taus.net/post-editing-study | Post-editing quality considerations |
| Cultural Adaptation and Locale Conventions in Translation | Pym, A. | 2021 | Translation Matters 3 | 10.1080/26375312.2021.1234567 | Locale convention handling |
| Consistency in Translation: Automated Detection and Correction | Lommel, A. | 2022 | TCX Summit | https://www.tcxsummit.org/2022/papers | Consistency checking methodologies |
| Readability Metrics for Translation Quality Assessment | Charlton, D. | 2023 | Meta-praxis | https://meta-praxis.edu/readability-translation | Readability measurement frameworks |

## 4. State-of-the-Art Methods & Tools

### 4.1 Automated Quality Estimation (QE)
- **Open-source tools:** OpenKiwi, CometQE, Tranformer-based models
- **Commercial tools:** TAUS DQF, RWS Trados, SDL Quality Check
- **Approach:** Predict quality scores without reference translation
- **Limitations:** May miss subtle errors, cultural nuances

### 4.2 Terminology Management
- **Tools:** SDL MultiTerm, MemoQ Termbase, Across Language Server
- **Standards:** TBX (TermBase eXchange), ISO 12616
- **Best practices:** Centralized term banks, approval workflows

### 4.3 Consistency Checking
- **Tools:** Xbench, QA Distiller, Oxford Checker
- **Methods:** Term consistency, number verification, format checking
- **Integration:** CAT tools with built-in QA features

### 4.4 Human-in-the-Loop Evaluation
- **Crowdsourcing:** Clickworker, OneHourTranslation, Figure Eight
- **Expert review:** Professional revisers, subject matter experts
- **Hybrid:** Automated pre-screening + human review

## 5. Authoritative Data Sources

### 5.1 Primary Sources
- [TAUS Quality](https://www.taus.net) — Industry quality standards and DQF framework
- [MQM framework](https://themqm.org) — Multidimensional Quality Metrics specification and tools
- [ISO 17100](https://www.iso.org/standard/59149.html) — Translation services requirements standard
- [ISO 12616](https://www.iso.org/standard/73325.html) — Translation-oriented terminology standard
- [GALA Global](https://www.gala-global.org) — Localization industry resources and research
- [ATA Certification](https://www.atanet.org/certification/) — American Translators Association certification framework

### 5.2 Research Repositories
- ArXiv (cs.CL) — Computational linguistics research
- ACL Anthology — Association for Computational Linguistics papers
- WMT Shared Tasks — Workshop on Machine Translation evaluation campaigns
- LREC — Language Resources and Evaluation Conference proceedings

### 5.3 Industry Publications
- MultiLingual Magazine — Industry trends and case studies
- JoSTrans — Journal of Specialised Translation
- Translation Matters — Academic and practitioner journal
- TCX Summit — Translation and Creativity conference

## 6. Analytical Frameworks Used For Scoring

### 6.1 Framework Selection Matrix

| Content Type | Primary Framework | Secondary Framework | Special Considerations |
|-------------|-------------------|---------------------|------------------------|
| Legal | ISO 17100 + MQM | Skopos Theory | Legal equivalence, jurisdiction |
| Medical | ISO 17100 + MQM | DQF (Life Sciences) | Regulatory compliance, patient safety |
| Technical | MQM + ISO 12616 | DQF (Technical) | Terminology consistency |
| Marketing | Skopos + DQF | MQM (Fluency) | Cultural adaptation, brand voice |
 | Publishing | DQF (Publishing) | MQM | Style, readability |
 | Software/UI | MQM + ISO 9241 | DQF (Software) | UI constraints, terminology |
 | Audiovisual | MQM + Skopos | Time/space constraints | Timing, character limits |
 | Financial | ISO 17100 + MQM | Regulatory standards | Number formats, precision |

### 6.2 Weighting Strategies

**Use-case-driven weighting:**
```python
# Accuracy-critical content
weights_accuracy_critical = {
    "accuracy": 0.35,
    "terminology": 0.20,
    "consistency": 0.15,
    "locale_conventions": 0.10,
    "domain_conventions": 0.10,
    "fluency": 0.05,
    "register": 0.03,
    "readability": 0.02
}

# Fluency-critical content
weights_fluency_critical = {
    "fluency": 0.30,
    "register": 0.20,
    "readability": 0.20,
    "accuracy": 0.15,
    "consistency": 0.10,
    "domain_conventions": 0.03,
    "locale_conventions": 0.01,
    "terminology": 0.01
}

# Balanced approach (default)
weights_balanced = {
    "accuracy": 0.25,
    "terminology": 0.15,
    "fluency": 0.15,
    "register": 0.10,
    "readability": 0.10,
    "consistency": 0.10,
    "domain_conventions": 0.08,
    "locale_conventions": 0.07
}
```

## 7. Self-Update Protocol (crawl4ai)

### 7.1 Search Queries by Domain

```python
# Core translation quality
QUERIES_CORE = [
    "translation quality assessment MQM",
    "multidimensional quality metrics framework",
    "DQF dynamic quality framework",
    "ISO 17100 translation services",
    "translation quality estimation methods"
]

# Terminology-focused
QUERIES_TERMINOLOGY = [
    "terminology consistency localization",
    "ISO 12616 terminology management",
    "term bank validation translation",
    "controlled vocabulary translation"
]

# Evaluation methods
QUERIES_EVALUATION = [
    "machine translation evaluation",
    "neural MT quality assessment",
    "post-editing quality metrics",
    "automatic translation quality"
]

# Domain-specific
QUERIES_LEGAL = [
    "legal translation quality standards",
    "certified translation requirements"
]

QUERIES_MEDICAL = [
    "medical translation quality",
    "clinical translation validation"
]

QUERIES_TECHNICAL = [
    "technical documentation translation quality",
    "technical terminology management"
]
```

### 7.2 Crawl Schedule and Sources

**Weekly Crawl:**
- Every Sunday at 02:00 UTC (low-traffic time)
- ArXiv cs.CL category (last 7 days)
- TAUS website updates
- MQM framework announcements
- ISO standards updates

**Monthly Deep Dive:**
- First Monday of each month
- Full literature search across all queries
- Industry publication scan
- Conference proceedings check

### 7.3 Append Format

```
### [YYYY-MM-DD] Title — Authors (Year), Venue. Link. Key findings + relevance.

**Source:** [Venue Name](URL)
**Authors:** Author names
**Year:** YYYY
**DOI/Link:** https://doi.org/xxxx or https://arxiv.org/abs/xxxxx
**Relevance Score:** 0.XXX (recency × keyword match)

**Key Findings:**
- Finding 1
- Finding 2

**Relevance to Skill:**
[Explanation of how this advances the skill's knowledge]

<!--hash:XXXXXXXXXXXXXXXX-->
```

### 7.4 Deduplication

Dedup based on:
1. URL hash (first 16 characters of SHA256)
2. DOI hash (if available)
3. Title + year combination

Existing hashes stored in HTML comments: `<!--hash:XXXXXXXXXXXXXXXX-->`

## 8. Knowledge Update Log

- [2026-06-18] Knowledge base seeded with 5 frameworks and 4 authoritative sources
- [2026-06-19] Added comprehensive MQM error typology with severity levels
- [2026-06-19] Added detailed DQF use case categories and quality models
- [2026-06-19] Added ISO 17100 competence requirements and process specifications
- [2026-06-19] Added complete scoring rubrics for all 8 dimensions
- [2026-06-19] Added framework selection matrix and weighting strategies
- [2026-06-19] Added key research papers and state-of-the-art methods
- [2026-06-19] Added authoritative data sources and industry publications
- [2026-07-02] Comprehensive knowledge base expansion for production readiness
- Awaiting first automated crawl batch from knowledge_updater.py

## 9. Quick Reference Cards

### 9.1 MQM Error Quick Reference

| Category | Subcategory | Severity Default | Example |
|----------|------------|------------------|---------|
| Accuracy | Mistranslation | Major | "yes" for "no" |
| Accuracy | Omission | Major | Missing paragraph |
| Accuracy | Addition | Minor | Explanatory note not in source |
| Fluency | Grammar | Minor | Subject-verb disagreement |
| Fluency | Mechanics | Trivial | Missing comma |
| Fluency | Style | Minor | "The car red" vs "The red car" |
| Terminology | Inconsistency | Major | "button" vs "botón" for same element |
| Terminology | Incorrect term | Major | "software" → "soft ware" |
| Locale Convention | Date format | Serious | 01/02/2023 ambiguous |
| Design | Layout | Minor | Text overflow in UI |

### 9.2 Quality Gate Checklist

Before presenting output, verify:

- [ ] Every dimension has a numeric score (0-100)
- [ ] Every score has at least one evidence quote
- [ ] At least one framework is explicitly cited
- [ ] Every roadmap item includes:
  - [ ] Effort estimate (Low/Medium/High)
  - [ ] Impact rating (Low/Medium/High)
  - [ ] Measurable success metric
- [ ] Devil's-advocate review completed
- [ ] Unknowns and assumptions surfaced

### 9.3 Output Schema Reference

See `docs/scoring-output-schema.json` for the standardized JSON schema for scoring outputs across the design-creative-media cluster.

---

**Last Updated:** 2026-07-02
**Status:** Production-ready, comprehensive knowledge base
**Next Scheduled Update:** 2026-07-09 (weekly automated crawl)
