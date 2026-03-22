# Defect Log — Waterfall Run
**Project:** Task Management Web Application  
**Phase:** Testing (Week 7)  
**Author:** Muhammad Subtain | B01811837

---

| Bug ID | Description | Severity | Date Found | Related TC | Fix Effort (hrs) | Fixed (Y/N) |
|--------|-------------|----------|------------|------------|------------------|-------------|
| WF-001 | User registration allows whitespace-only usernames | Medium | 2026-03-22 | TC-01 | 0.5 | Y |
| WF-002 | Session persists after logout if browser cache not cleared | High | 2026-03-22 | TC-08 | 1.2 | Y |
| WF-003 | Task creation form accepts past due dates without warning | Low | 2026-03-22 | TC-12 | 0.3 | Y |
| WF-004 | Assignee dropdown shows deleted users (soft delete issue) | Medium | 2026-03-22 | TC-10 | 0.8 | Y |
| WF-005 | Notification not created when task assigned to self | Low | 2026-03-22 | TC-05 | 0.4 | Y |
| WF-006 | Status update doesn't validate state transitions (e.g., Done → In Progress) | High | 2026-03-22 | TC-16 | 1.0 | Y |
| WF-007 | Dashboard overdue count includes completed tasks | High | 2026-03-22 | TC-21 | 0.9 | Y |
| WF-008 | Task edit form doesn't preserve description on validation error | Medium | 2026-03-22 | TC-13 | 0.6 | Y |
| WF-009 | Notification message truncates long task titles (>50 chars) | Low | 2026-03-22 | TC-17 | 0.3 | Y |
| WF-010 | Multiple rapid task assignments create duplicate notifications | Medium | 2026-03-22 | TC-05 | 0.7 | Y |
| WF-011 | Task list filter doesn't reset when navigating back from edit | Low | 2026-03-22 | TC-23 | 0.4 | Y |
| WF-012 | Reassigning task to same user creates unnecessary notification | Low | 2026-03-22 | TC-14 | 0.3 | Y |

---

## Defect Analysis

### By Severity
| Severity | Count | Percentage | Total Fix Effort (hrs) |
|----------|-------|------------|----------------------|
| High | 3 | 25% | 3.1 |
| Medium | 5 | 42% | 3.6 |
| Low | 4 | 33% | 1.7 |
| **Total** | **12** | **100%** | **8.4** |

### By Category
- **Session/Auth Issues:** 2 defects (WF-002, WF-005)
- **Data Validation:** 4 defects (WF-001, WF-003, WF-006, WF-007)
- **Notification Logic:** 3 defects (WF-009, WF-010, WF-012)
- **UI/UX Issues:** 3 defects (WF-004, WF-008, WF-011)

### Discovery Timeline
- **Day 1 (2026-03-22):** All 12 defects discovered during integration testing phase
- **Average Fix Time:** 0.7 hours per defect
- **Critical Issues:** 3 high-severity defects required immediate fixes before regression testing

### Key Observations

**Testing Phase Effectiveness:**
The comprehensive test plan (26 test cases) identified 12 defects during the testing phase, demonstrating the value of formal testing in Waterfall. However, the late discovery of these issues (Week 7) meant that fixes required regression testing of all affected test cases.

**Defect Distribution:**
- High-severity defects (3) were primarily logic errors (session handling, state validation, overdue calculation)
- Medium-severity defects (5) were mostly edge cases and data handling issues
- Low-severity defects (4) were UI/UX issues with minimal functional impact

**Rework Impact:**
The 8.4 hours of defect fixes, combined with 5 hours of change request rework, totaled 13.4 hours of rework effort in the testing phase. This represents 45% of the total development effort and demonstrates the cost of late defect discovery in Waterfall methodology.