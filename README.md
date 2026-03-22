# Waterfall vs Agile: Comparative Methodology Study
**MSc IT with Project Management — Primary Simulation Study**  
**Author:** Muhammad Subtain | B01811837  
**Institution:** University of the West of Scotland

---

## Overview

This repository contains a comprehensive comparative study of Waterfall and Agile methodologies applied to an identical software development scope under controlled conditions. The project includes two fully functional task management web applications (one built using Waterfall, one using Agile), detailed metrics collection, and a decision-support tool for methodology selection.

---

## Repository Structure

```
├── waterfall_run/              # Waterfall methodology implementation
│   ├── app/                    # Flask application
│   │   ├── auth/              # Authentication routes
│   │   ├── tasks/             # Task management routes
│   │   ├── notifications/     # Notification routes
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # CSS and static files
│   │   └── models.py          # Database models
│   ├── docs/                  # Waterfall methodology documentation
│   │   ├── requirements_spec.md
│   │   ├── system_design.md
│   │   ├── test_plan.md
│   │   ├── gantt_chart.md
│   │   ├── change_log.md
│   │   └── bug_log.md
│   ├── metrics/               # Waterfall metrics
│   │   ├── time_log.md
│   │   ├── defect_log.md
│   │   └── summary.md
│   ├── config.py              # Configuration
│   ├── run.py                 # Application entry point
│   └── requirements.txt       # Python dependencies
│
├── agile_run/                 # Agile methodology implementation
│   ├── app/                   # Flask application
│   │   ├── auth/              # Authentication routes
│   │   ├── main/              # Main routes
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # CSS and static files
│   │   └── models.py          # Database models
│   ├── docs/                  # Agile/Scrum artifacts
│   │   ├── product_backlog.md
│   │   ├── sprint_plan.md
│   │   ├── standup_log.md
│   │   ├── sprint_reviews.md
│   │   ├── retrospectives.md
│   │   ├── burndown_data.md
│   │   └── backlog_additions.md
│   ├── metrics/               # Agile metrics
│   │   ├── time_log.md
│   │   ├── defect_log.md
│   │   └── summary.md
│   ├── config.py              # Configuration
│   ├── run.py                 # Application entry point
│   └── requirements.txt       # Python dependencies
│
├── analysis/                  # Comparative analysis
│   ├── comparison_report.md   # Full 4-section comparison report
│   ├── metrics.xlsx           # Excel workbook with charts
│   ├── README.md              # Analysis guide
│   ├── VERIFICATION.md        # Verification checklist
│   ├── create_metrics_workbook.py  # Script to generate Excel
│   └── decision_tool/         # Decision-support tool
│       ├── app.py             # Streamlit application
│       ├── requirements.txt   # Dependencies
│       └── scoring_matrix.md  # Scoring logic documentation
│
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── LICENSE                    # License information
```

---

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Run Waterfall Application
```bash
cd waterfall_run
pip install -r requirements.txt
python run.py
```
Application runs on `http://localhost:5000`

### Run Agile Application
```bash
cd agile_run
pip install -r requirements.txt
python run.py
```
Application runs on `http://localhost:5001`

### Run Decision-Support Tool
```bash
cd analysis/decision_tool
pip install -r requirements.txt
streamlit run app.py
```
Tool opens at `http://localhost:8501`

### View Analysis
```bash
# Read the comparison report
cat analysis/comparison_report.md

# Open Excel metrics (Windows)
start analysis/metrics.xlsx

# Open Excel metrics (macOS)
open analysis/metrics.xlsx

# Open Excel metrics (Linux)
libreoffice analysis/metrics.xlsx
```

---

## Key Findings

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

### Key Insights
1. **Waterfall's late defect discovery** (Week 7 testing phase) required 8.4 hours of rework
2. **Agile's early detection** during development required only 3.1 hours of rework
3. **Waterfall's total rework:** 13.4 hours (45% of development effort)
4. **Agile's total rework:** 8.0 hours (15% of development effort)
5. **Both methodologies achieved 100% feature delivery** (10/10 features)

---

## Features Implemented

### Core Features (Both Applications)
- ✅ User Registration & Authentication
- ✅ Task Creation & Management
- ✅ Task Assignment
- ✅ Status Updates
- ✅ Notifications System
- ✅ Dashboard with Analytics

### Change Requests (Both Applications)
- ✅ CR-001: Task Categories (Work/Personal/Urgent)
- ✅ CR-002: Dashboard Status Counts
- ✅ CR-003: Task Comments System

---

## Analysis Components

### 1. Comparison Report (`analysis/comparison_report.md`)
A comprehensive 4-section report covering:
- **Section A:** Quantitative metrics comparison
- **Section B:** Qualitative themes (documentation, change management, predictability)
- **Section C:** Critical limitations (order effect, solo execution, single simulation)
- **Section D:** Literature contextualization (CHAOS Report, Digital.ai, PMI)

### 2. Excel Workbook (`analysis/metrics.xlsx`)
Six sheets with embedded charts:
- Raw Metrics (side-by-side comparison)
- Time Breakdown (bar chart)
- Defect Comparison (bar chart)
- Rework Comparison (bar chart)
- Agile Burndown (line chart)
- Summary Dashboard

### 3. Decision-Support Tool (`analysis/decision_tool/app.py`)
Interactive Streamlit application that recommends Agile, Waterfall, or Hybrid based on:
- Requirements Volatility
- Regulatory Intensity
- Team Size
- Team Distribution
- Project Type
- Timeline Pressure

---

## Methodology Documentation

### Waterfall Artifacts
- Requirements Specification
- System Design Document
- Test Plan (26 test cases)
- Gantt Chart
- Change Log
- Bug Log
- Defect Log (12 defects)

### Agile Artifacts
- Product Backlog
- Sprint Plans (3 sprints)
- Daily Standup Logs
- Sprint Reviews
- Retrospectives
- Burndown Data
- Backlog Additions
- Defect Log (7 defects)

---

## Metrics & Data

### Waterfall Metrics
- **Total Development Time:** 46.9 hours
- **Defects Found:** 12 (3 High, 5 Medium, 4 Low)
- **Defect Fix Effort:** 8.4 hours
- **Change Request Rework:** 5.0 hours
- **Total Rework:** 13.4 hours (45% of effort)

### Agile Metrics
- **Total Development Time:** 52.5 hours
- **Defects Found:** 7 (1 High, 4 Medium, 2 Low)
- **Defect Fix Effort:** 3.1 hours
- **Change Request Rework:** 8.0 hours
- **Total Rework:** 8.0 hours (15% of effort)

---

## Technology Stack

### Backend
- Python 3.8+
- Flask (web framework)
- SQLite (database)
- SQLAlchemy (ORM)

### Frontend
- HTML5
- CSS3
- Jinja2 (templating)

### Analysis Tools
- Python (data processing)
- openpyxl (Excel generation)
- Streamlit (web UI)
- Plotly (visualization)

---

## Installation & Setup

### Clone Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### Install Dependencies
```bash
# Waterfall
cd waterfall_run
pip install -r requirements.txt

# Agile
cd ../agile_run
pip install -r requirements.txt

# Analysis tools
cd ../analysis/decision_tool
pip install -r requirements.txt
```

### Run Applications
```bash
# Terminal 1: Waterfall (port 5000)
cd waterfall_run && python run.py

# Terminal 2: Agile (port 5001)
cd agile_run && python run.py

# Terminal 3: Decision Tool (port 8501)
cd analysis/decision_tool && streamlit run app.py
```

---

## Project Limitations

1. **Order Effect:** Waterfall executed first; Agile may have benefited from prior problem-solving familiarity
2. **Solo Execution:** Self-logged time is subjective; mitigated by Git commit timestamps
3. **Single Simulation:** Findings are illustrative, not statistically generalizable
4. **Small Scale:** Single-developer MVP does not reflect enterprise complexity

---

## Literature References

- **Standish CHAOS Report:** Agile ~42-50% success vs Waterfall ~13-26%
- **Digital.ai 18th State of Agile 2025:** 74% hybrid adoption, 84% AI integration pressure
- **Leong et al. (2023):** Agile risks in distributed or immature teams
- **PMI Pulse of the Profession 2025:** Hybrid methodology growth trends

---

## Recommendations

### Choose Waterfall When:
- Requirements are well-defined and stable
- Regulatory compliance requires extensive documentation
- Project scope is fixed and unlikely to change
- Team is experienced with formal processes
- Predictability is more important than flexibility

### Choose Agile When:
- Requirements are volatile or evolving
- Rapid time-to-market is critical
- Stakeholder feedback is frequent
- Team is co-located or has good communication
- Flexibility and adaptability are priorities

### Choose Hybrid When:
- Project has mixed characteristics
- Some components are stable, others volatile
- Regulatory requirements exist but not all-encompassing
- Team has experience with both methodologies
- Organization is transitioning between approaches

---

## Contributing

This is a research project for academic purposes. For questions or suggestions, please contact the author.

---

## License

This project is provided for educational and research purposes.

---

## Author

**Muhammad Subtain**  
B01811837  
University of the West of Scotland  
MSc IT with Project Management

---

## Verification

All components have been verified and tested:
- ✅ Both applications run without errors
- ✅ All features implemented and functional
- ✅ Metrics collected and documented
- ✅ Analysis complete and verified
- ✅ Decision tool functional
- ✅ All documentation complete

For detailed verification, see `analysis/VERIFICATION.md`

---

**Last Updated:** March 23, 2026  
**Status:** Ready for GitHub Upload
