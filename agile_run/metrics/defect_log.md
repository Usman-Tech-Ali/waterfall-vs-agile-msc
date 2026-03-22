# Defect Log — Agile Run
**Project:** Task Management Web Application  
**Methodology:** Agile (Scrum)  
**Author:** Muhammad Subtain | B01811837

---

| Bug ID | Sprint Found | Description | Severity | Fix Effort (hrs) | Fixed Y/N |
|--------|--------------|-------------|----------|------------------|-----------|
| AG-001 | Sprint 1 | User registration allows duplicate usernames in edge case | Medium | 0.5 | Y |
| AG-002 | Sprint 1 | Task assignment notification not created for self-assignment | Low | 0.3 | Y |
| AG-003 | Sprint 2 | Dashboard overdue count includes completed tasks | High | 0.8 | Y |
| AG-004 | Sprint 2 | Notification display shows HTML entities instead of proper text | Medium | 0.4 | Y |
| AG-005 | Sprint 2 | Task status update doesn't trigger notification for task creator | Medium | 0.6 | Y |
| AG-006 | Sprint 3 | Task list filter doesn't persist after page refresh | Low | 0.3 | Y |
| AG-007 | Sprint 3 | Comment timestamps show UTC instead of local time | Low | 0.2 | Y |

---

## Defect Analysis

### By Sprint
| Sprint | Defects Found | Total Fix Effort (hrs) |
|--------|---------------|----------------------|
| Sprint 1 | 2 | 0.8 |
| Sprint 2 | 3 | 1.8 |
| Sprint 3 | 2 | 0.5 |
| **Total** | **7** | **3.1** |

### By Severity
| Severity | Count | Percentage | Avg Fix Effort (hrs) |
|----------|-------|------------|---------------------|
| High | 1 | 14% | 0.8 |
| Medium | 4 | 57% | 0.6 |
| Low | 2 | 29% | 0.3 |

### Defect Categories
- **Data Validation:** 2 defects (AG-001, AG-003)
- **Notification Logic:** 3 defects (AG-002, AG-004, AG-005)
- **UI/UX Issues:** 2 defects (AG-006, AG-007)

## Key Observations

### Early Detection Benefits
- **Sprint 1-2:** Most critical defects found early in development cycle
- **Iterative Testing:** Regular sprint reviews caught issues before they compounded
- **Quick Resolution:** Average fix time of 0.44 hours per defect due to fresh context

### Agile Advantages
- **Immediate Feedback:** Issues discovered during sprint demos and daily development
- **Continuous Integration:** Defects caught before feature completion
- **Low Rework Impact:** Early detection meant minimal code changes required

### Comparison Notes (for dissertation)
- **Lower Defect Count:** 7 defects vs. estimated 12-15 in Waterfall approach
- **Faster Resolution:** Average 0.44 hrs vs. estimated 1.2 hrs in Waterfall
- **Prevention Focus:** Iterative development prevented architectural issues
- **Context Retention:** Bugs fixed immediately while code was fresh in memory