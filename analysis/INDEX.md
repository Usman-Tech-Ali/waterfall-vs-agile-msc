# Analysis Directory Index
**Waterfall vs Agile Comparative Study — MSc IT with Project Management**

---

## 📋 Quick Start

1. **Read the findings:** `README.md` (5 min read)
2. **View the data:** `metrics.xlsx` (open in Excel/Sheets)
3. **Get a recommendation:** `decision_tool/app.py` (run Streamlit app)
4. **Deep dive:** `comparison_report.md` (full analysis)

---

## 📁 Files Overview

### Core Documents

| File | Purpose | Size | Read Time |
|------|---------|------|-----------|
| `README.md` | Overview, key findings, how to run | 8 KB | 5 min |
| `comparison_report.md` | Full comparative analysis (4 sections) | 28 KB | 20 min |
| `VERIFICATION.md` | Verification checklist | 8 KB | 5 min |
| `INDEX.md` | This file | 3 KB | 2 min |

### Data & Tools

| File | Purpose | Type | Sheets/Lines |
|------|---------|------|--------------|
| `metrics.xlsx` | Quantitative metrics with charts | Excel | 6 sheets, 5 charts |
| `create_metrics_workbook.py` | Script to generate Excel workbook | Python | 300 lines |
| `decision_tool/app.py` | Streamlit decision-support tool | Python | 415 lines |
| `decision_tool/requirements.txt` | Python dependencies | Text | 2 lines |
| `decision_tool/scoring_matrix.md` | Scoring logic explanation | Markdown | 250 lines |

---

## 🎯 By Use Case

### I want to understand the findings quickly
→ Read `README.md` (5 minutes)

### I want to see the data
→ Open `metrics.xlsx` (Excel workbook with 6 sheets and 5 charts)

### I want to get a methodology recommendation
→ Run `decision_tool/app.py` (Streamlit web app)

### I want the full academic analysis
→ Read `comparison_report.md` (393 lines, 4 sections)

### I want to understand the scoring algorithm
→ Read `decision_tool/scoring_matrix.md` (detailed explanation)

### I want to verify everything is correct
→ Read `VERIFICATION.md` (checklist of all components)

---

## 📊 Key Metrics at a Glance

### Development Effort
- **Waterfall:** 29.5 hours (10 planning, 14.5 coding, 5 rework)
- **Agile:** 52.5 hours (7 planning, 42.5 coding, 3 testing, 8 rework)

### Defect Detection
- **Waterfall:** 0 defects found (testing phase not executed)
- **Agile:** 7 defects found and fixed (3.1 hours total)

### Change Request Impact
- **Waterfall:** 5 hours rework, +5 days schedule impact, High disruption
- **Agile:** 8 hours rework, 0 days schedule impact, Low disruption

### Feature Delivery
- **Both:** 10/10 features delivered (100% delivery rate)

---

## 🔍 Comparison Report Sections

### Section A: Quantitative Metrics
- Overall development effort comparison
- Defect metrics (count, severity, fix effort)
- Change request impact analysis (CR-001, CR-002, CR-003)
- Feature delivery rates

### Section B: Qualitative Themes
- Documentation overhead (Waterfall) vs sprint planning overhead (Agile)
- Change request handling and disruption levels
- Predictability and control trade-offs
- Iterative value: early detection, visibility, flexibility

### Section C: Critical Limitations
- Order effect bias (Waterfall first, Agile second)
- Solo execution and self-logging subjectivity
- Single simulation generalizability constraints
- Small scale vs enterprise complexity

### Section D: Literature Contextualization
- Standish CHAOS Report alignment (Agile 42-50% vs Waterfall 13-26%)
- Digital.ai 18th State of Agile (74% hybrid adoption)
- Leong et al. on Agile risks in distributed teams
- PMI Pulse of the Profession on hybrid growth

---

## 🛠️ Decision Tool Features

### Inputs (6 parameters)
1. Requirements Volatility (1-10 slider)
2. Regulatory Intensity (None / Low / High)
3. Team Size (Solo / Small 2-5 / Large 6+)
4. Team Distribution (Co-located / Hybrid / Remote)
5. Project Type (Fixed-scope / Cloud-native / AI-integrated / Mixed)
6. Timeline Pressure (1-10 slider)

### Outputs
- Recommendation badge (Agile / Waterfall / Hybrid)
- Confidence level (High / Medium / Low)
- Explanation text (references input values)
- Radar chart (all three scores)
- Score breakdown table
- Methodology guide

### Scoring Algorithm
- Agile score: volatility × 7 + timeline × 4 + project type bonus - regulatory penalty
- Waterfall score: (10 - volatility) × 7 + regulatory bonus + team size bonus - timeline penalty
- Hybrid score: (Agile + Waterfall) / 2 + 10

---

## 📈 Excel Workbook Sheets

| Sheet | Purpose | Rows | Columns | Chart |
|-------|---------|------|---------|-------|
| Raw Metrics | Side-by-side comparison | 19 | 4 | None |
| Time Breakdown | Hours by phase/sprint | 8 | 4 | Bar chart |
| Defect Comparison | Defects and fix effort | 9 | 4 | Bar chart |
| Rework Comparison | Rework per change request | 7 | 4 | Bar chart |
| Agile Burndown | Sprint burndown data | 13 | 7 | Line chart |
| Summary Dashboard | Key metrics summary | 18 | 3 | None |

---

## 🚀 How to Run

### View the Comparison Report
```bash
cat analysis/comparison_report.md
```

### Open the Excel Workbook
```bash
# Windows
start analysis/metrics.xlsx

# macOS
open analysis/metrics.xlsx

# Linux
libreoffice analysis/metrics.xlsx
```

### Run the Decision Tool
```bash
cd analysis/decision_tool
pip install -r requirements.txt
streamlit run app.py
# Opens at http://localhost:8501
```

### Run Both Applications Simultaneously
```bash
# Terminal 1: Waterfall (port 5000)
cd waterfall_run && python run.py

# Terminal 2: Agile (port 5001)
cd agile_run && python run.py

# Terminal 3: Decision Tool (port 8501)
cd analysis/decision_tool && streamlit run app.py
```

---

## 📚 Literature References

- **Standish CHAOS Report (2020-2025):** Agile 42-50% success vs Waterfall 13-26%
- **Digital.ai 18th State of Agile (2025):** 74% hybrid adoption, 84% AI integration
- **Leong et al. (2023):** Agile risks in distributed teams and immature organizations
- **PMI Pulse of the Profession (2025):** Hybrid methodologies growing, higher success rates

---

## ✅ Verification Status

- ✅ All 4 sections of comparison report complete
- ✅ All 9 key metrics included with real data
- ✅ Excel workbook with 6 sheets and 5 charts
- ✅ Streamlit decision tool fully functional
- ✅ Scoring algorithm implemented and tested
- ✅ All literature references included
- ✅ Critical limitations honestly addressed
- ✅ README with complete instructions

**Status:** Ready for dissertation submission and presentation

---

## 📞 Questions?

Refer to:
- `README.md` for overview and quick start
- `comparison_report.md` for detailed findings
- `decision_tool/scoring_matrix.md` for scoring logic
- `VERIFICATION.md` for component checklist

---

**Last Updated:** 2026-04-19  
**Project:** MSc IT with Project Management — Waterfall vs Agile Comparative Study  
**Author:** Muhammad Subtain | B01811837  
**Institution:** University of the West of Scotland