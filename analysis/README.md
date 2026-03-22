# Analysis: Waterfall vs Agile Comparative Study
**MSc IT with Project Management — Primary Simulation**  
**Author:** Muhammad Subtain | B01811837  
**Institution:** University of the West of Scotland  
**Date:** 2026-04-19

---

## Overview

This analysis directory contains a comprehensive comparative study of Waterfall and Agile methodologies applied to an identical software development scope under controlled conditions. The analysis includes quantitative metrics, qualitative observations, and a decision-support tool for methodology selection.

---

## Contents

### 1. Comparison Report
**File:** `comparison_report.md`

A structured 4-section report covering:
- **Section A:** Quantitative metrics comparison (hours, defects, change requests)
- **Section B:** Qualitative themes (documentation overhead, change management, predictability, iterative value)
- **Section C:** Critical limitations (order effect bias, solo execution, single simulation, small scale)
- **Section D:** Literature contextualization (CHAOS Report, Digital.ai, Leong et al., PMI)

**Key Findings:**
- Waterfall discovered 12 defects during testing phase (8.4 hrs fix effort); Agile found 7 defects during development (3.1 hrs fix effort)
- Waterfall's late defect discovery required regression testing; Agile's early detection prevented cascading issues
- Agile superior in change management (8 hrs rework vs 5 hrs, but zero schedule impact)
- Waterfall superior in upfront planning (10 hrs documentation provided clarity)
- Both methodologies achieved 100% feature delivery
- Hybrid approaches recommended for mixed project characteristics

### 2. Excel Workbook
**File:** `metrics.xlsx`

Six sheets with data and charts:
- **Sheet 1 — Raw Metrics:** Side-by-side comparison of all quantitative metrics
- **Sheet 2 — Time Breakdown:** Hours by phase/sprint with bar chart
- **Sheet 3 — Defect Comparison:** Defects found and fix effort with bar chart
- **Sheet 4 — Rework Comparison:** Rework hours per change request with bar chart
- **Sheet 5 — Agile Burndown:** Sprint burndown data with line chart
- **Sheet 6 — Summary Dashboard:** Key metrics and findings

**How to Open:**
```bash
# Windows
start metrics.xlsx

# macOS
open metrics.xlsx

# Linux
libreoffice metrics.xlsx
```

### 3. Decision-Support Tool
**Directory:** `decision_tool/`

A Streamlit web application that recommends Agile, Waterfall, or Hybrid based on project characteristics.

**Files:**
- `app.py` — Main Streamlit application
- `requirements.txt` — Python dependencies
- `scoring_matrix.md` — Detailed explanation of scoring logic

**How to Run:**
```bash
cd decision_tool
pip install -r requirements.txt
streamlit run app.py
```

The tool opens in your browser at `http://localhost:8501`

**Inputs:**
- Requirements Volatility (1-10 slider)
- Regulatory Intensity (None / Low / High)
- Team Size (Solo / Small 2-5 / Large 6+)
- Team Distribution (Co-located / Hybrid / Remote)
- Project Type (Fixed-scope / Cloud-native / AI-integrated / Mixed)
- Timeline Pressure (1-10 slider)

**Outputs:**
- Recommendation badge (Agile / Waterfall / Hybrid)
- Confidence level (High / Medium / Low)
- Explanation of recommendation
- Radar chart showing all three scores
- Detailed score breakdown

---

## Key Metrics Summary

### Development Effort
| Metric | Waterfall | Agile | Difference |
|--------|-----------|-------|-----------|
| Total hours | 46.9 | 52.5 | +5.6 |
| Planning/Documentation | 10.0 | 7.0 | -3.0 |
| Coding | 14.5 | 42.5 | +28.0 |
| Testing | 9.0 | 3.0 | -6.0 |
| Rework (CRs) | 5.0 | 8.0 | +3.0 |
| Rework (Defects) | 8.4 | 0.0 | -8.4 |

### Defect Metrics
| Metric | Waterfall | Agile | Difference |
|--------|-----------|-------|-----------|
| Total defects | 12 | 7 | -5 |
| High severity | 3 | 1 | +2 |
| Medium severity | 5 | 4 | +1 |
| Low severity | 4 | 2 | +2 |
| Fix effort (hrs) | 8.4 | 3.1 | +5.3 |
| Avg fix time | 0.7 hrs | 0.44 hrs | +0.26 |

### Change Request Impact
| Metric | Waterfall | Agile | Difference |
|--------|-----------|-------|-----------|
| CR rework hours | 5.0 | 8.0 | +3.0 |
| Schedule impact | +5 days | 0 days | -5 days |
| Disruption level | High | Low | Significant |

### Feature Delivery
| Metric | Waterfall | Agile |
|--------|-----------|-------|
| Features delivered | 10/10 | 10/10 |
| Delivery rate | 100% | 100% |

---

## How to Run Both Applications Simultaneously

To compare the Waterfall and Agile implementations side-by-side:

**Terminal 1 — Waterfall Run:**
```bash
cd waterfall_run
python run.py
# Opens on http://localhost:5000
```

**Terminal 2 — Agile Run:**
```bash
cd agile_run
python run.py
# Opens on http://localhost:5001
```

**Terminal 3 — Decision Tool:**
```bash
cd analysis/decision_tool
streamlit run app.py
# Opens on http://localhost:8501
```

Both applications use the same feature set (6 baseline + 3 change requests) but different development methodologies. You can register users, create tasks, and test the full workflow in both.

---

## File Map

```
analysis/
├── README.md                          ← This file
├── comparison_report.md               ← Full comparative analysis (4 sections)
├── metrics.xlsx                       ← Excel workbook with 6 sheets and charts
├── create_metrics_workbook.py         ← Script to generate metrics.xlsx
│
└── decision_tool/
    ├── app.py                         ← Streamlit decision-support tool
    ├── requirements.txt               ← Python dependencies (streamlit, plotly)
    └── scoring_matrix.md              ← Detailed scoring logic explanation
```

---

## Methodology Selection Guide

### Choose Waterfall if:
- Requirements are stable and well-understood upfront
- Project is subject to regulatory compliance (HIPAA, SOX, etc.)
- Team is large and distributed
- Project scope is fixed and changes are expensive
- Stakeholder involvement is limited to formal milestones

### Choose Agile if:
- Requirements are volatile or evolving
- Project is in a dynamic market (startup, innovation)
- Team is small and co-located
- Stakeholder involvement is continuous
- Early delivery of working software is valuable

### Choose Hybrid if:
- Requirements are partially stable (core fixed, details evolving)
- Project has moderate regulatory requirements
- Team is small-to-medium and distributed
- Project has both fixed-scope and evolving components
- Organization is transitioning from Waterfall to Agile

---

## Literature References

- **Standish CHAOS Report (2020-2025):** Agile 42-50% success vs Waterfall 13-26%
- **Digital.ai 18th State of Agile (2025):** 74% hybrid adoption, 84% AI integration pressure
- **Leong et al. (2023):** Agile risks in distributed teams and immature organizations
- **PMI Pulse of the Profession (2025):** Hybrid methodologies growing, higher success rates

---

## Critical Limitations

1. **Order Effect:** Waterfall executed first (Weeks 5-7), Agile second (Weeks 8-10). Developer gained familiarity with codebase, potentially providing 2-3 hour advantage to Agile.

2. **Solo Execution:** Time logs self-reported by single developer. Mitigated by Git commit timestamps and standardized categories.

3. **Single Simulation:** Findings illustrative but not statistically generalizable. Based on small-scale task management application.

4. **Small Scale:** Does not represent enterprise complexity (large teams, regulatory compliance, legacy integration, deployment pipelines).

---

## Recommendations

1. **For small-to-medium projects with evolving requirements:** Use Agile or Agile-heavy hybrid
2. **For fixed-scope projects with stable requirements:** Use Waterfall or Waterfall-heavy hybrid
3. **For mixed characteristics:** Use hybrid approach combining Waterfall's planning with Agile's flexibility
4. **For regulated industries:** Use Waterfall or hybrid with strong governance
5. **For startups and innovation:** Use Agile with continuous stakeholder engagement

---

## Contact & Questions

For questions about this analysis, refer to:
- `comparison_report.md` for detailed findings
- `decision_tool/scoring_matrix.md` for scoring logic
- `metrics.xlsx` for raw data and visualizations

---

**Last Updated:** 2026-04-19  
**Status:** Complete