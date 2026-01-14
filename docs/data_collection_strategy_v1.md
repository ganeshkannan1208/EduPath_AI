EduPath AI — Phase 2
Data Collection & Curation Strategy
Version: v1.0

Objective:
Define authoritative data sources, extraction methods, verification rules, and responsibilities for building India-wide structured datasets for schools, colleges, exams, programs, jobs, skills, and vocational trades.

------------------------------------
1. DATA CATEGORIES & SOURCES
------------------------------------

A) Schools
- UDISE+ (Government)
- CBSE Portal
- CISCE/ICSE Portal
- State Education Department Portals (36 boards)
Coverage: National + State
Authority: High

B) Colleges & Universities
- UGC (University recognition)
- AICTE (Technical institution approvals)
- NIRF (Rankings)
- NAAC (Accreditation)
Coverage: National + State
Authority: High

C) Exams
- NTA (JEE, NEET, CUET)
- UPSC (Civil Services, NDA/CDS)
- SSC (CHSL/CGL)
- Banking (IBPS/RBI/SBI)
- RRB (Railways)
- State PSCs
Coverage: National + State
Authority: High–Medium

D) ITI / Vocational
- NCVT
- DGT
- NSDC
- NAPS
Coverage: National
Authority: High

E) Jobs & Careers
- NSQF (Skill level framework)
- Sector Skill Councils (SSC)
- NASSCOM (tech roles)
- Government notifications
Coverage: National
Authority: Medium–High

F) Skills
- NSDC
- Sector Skill Councils
- NASSCOM (IT/Software)
- MOOCs (secondary:
  - SWAYAM
  - NPTEL
  - Coursera
  - Udemy)
Authority: Medium (MOOCs = supplemental)

------------------------------------
2. COLLECTION METHOD MATRIX
------------------------------------

+-------------+----------+------------+-------------+
| Category    | Manual   | Scraping   | API/Export  |
+-------------+----------+------------+-------------+
| Schools     |   No     |   Yes      |  Partial    |
| Colleges    |   No     |   Yes      |  Yes        |
| Exams       |   Yes    |   Yes      |  No         |
| Programs    |   Yes    |   No       |  No         |
| Jobs        |   Yes    |   No       |  No         |
| Skills      |   Yes    |   No       |  No         |
| ITI Trades  |   No     |   No       |  Yes        |
+-------------+----------+------------+-------------+

Interpretation:
- Schools → UDISE exports + state portal scraping
- Colleges → AICTE/UGC/NIRF exports
- ITI → NCVT JSON exports
- Exams → Hybrid (manual + scraping)
- Programs → Manual population (schema-driven)
- Jobs/Skills → Manual extraction + mapping

------------------------------------
3. DATA VERIFICATION RULES
------------------------------------

(1) Eligibility consistency rule
Eligibility must not contradict program requirements.
Example:
If NEET requires 12th Science → MBBS program cannot allow Commerce.

(2) Domain alignment rule
Program domain must align with job domain.
Example:
B.Tech CSE → Software Engineer (OK)
B.Tech Civil → Software Engineer (Weak)

(3) Fee validation rule
fees_min ≤ fees_max
Invalid → reject or flag

(4) Accreditation rule
College claiming NAAC grade must have NAAC record.

(5) Ranking consistency rule
NIRF ranking must match published year.

(6) Location granularity rule
Location must follow:
State → City → Pincode

(7) Exam frequency rule
Frequency must be one of:
{Yearly, Bi-Yearly, Multiple, Irregular}

(8) No contradiction policy
Conflicting data → discard/flag rather than merge.

------------------------------------
4. RESPONSIBILITY MATRIX
------------------------------------

+-------------+----------------------+
| Category    | Population Method    |
+-------------+----------------------+
| Schools     | Govt source import   |
| Colleges    | Govt source import   |
| Exams       | Manual + Scraping    |
| Programs    | Manual (Phase 1)     |
| Jobs        | Manual (NSQF-level)  |
| Skills      | Manual (NSDC-level)  |
| ITI Trades  | Govt export          |
+-------------+----------------------+

Interpretation:
- We don’t rely on LLM for factual data.
- Structured sources have priority.

------------------------------------
5. INDIA COVERAGE STRATEGY
------------------------------------

Dataset must support:
✔ 28 States + 8 Union Territories
✔ National Boards
✔ State Boards
✔ National Exams
✔ State Exams
✔ National/State Institutions
✔ Government + Private + Public Sector

------------------------------------
6. DATA STORAGE FORMAT
------------------------------------

Primary: JSON
Secondary: CSV
Optional: Parquet (future optimization)
Tertiary: PDF/HTML (source archival)

------------------------------------
7. COHERENCE WITH PHASE 1 SCHEMAS
------------------------------------

Dataset templates must comply with:
- program_schema_v1.json
- exam_schema_v1.json
- job_schema_v1.json
- skill_schema_v1.json
- institution_schema_v1.json

------------------------------------
8. FUTURE AUTOMATION NOTES
------------------------------------

Potential automation:
✓ AICTE → API scraping
✓ NCVT → structured export
✓ UDISE → PDF → OCR → Extraction
✓ NIRF → CSV ranking ingestion

------------------------------------
End of Document
------------------------------------
