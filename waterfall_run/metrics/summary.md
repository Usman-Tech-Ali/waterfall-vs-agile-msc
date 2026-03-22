# Metrics Summary — Waterfall Run
**Project:** Task Management Web Application  
**Author:** Muhammad Subtain | B01811837  
**Status:** To be completed after testing phase

---

## Hours by Phase

| Phase | Estimated (hrs) | Actual (hrs) |
|-------|----------------|--------------|
| Requirements | 6 | 4.0 |
| Design | 10 | 6.0 |
| Coding | 22 | 14.5 |
| Testing | 11 | 9.0 |
| Rework (CRs) | 7 | 5.0 |
| Rework (Defects) | 0 | 8.4 |
| **Total** | **56** | **46.9** |

---

## Defects

| Metric | Value |
|--------|-------|
| Total defects found | 12 |
| High severity | 3 |
| Medium severity | 5 |
| Low severity | 4 |
| Total fix effort (hrs) | 8.4 |

---

## Features Delivered

| Feature | Delivered (Y/N) |
|---------|----------------|
| FR-01: User Registration | Y |
| FR-02: Login / Logout | Y |
| FR-03: Task Creation | Y |
| FR-04: Task Assignment | Y |
| FR-05: Status Updates | Y |
| FR-06: Notifications | Y |
| FR-07: Dashboard | Y |
| CR-001: Category field | Y |
| CR-002: Status counts on dashboard | Y |
| CR-003: Comments | Y |
| **Total** | **10 / 10** |

---

## Qualitative Observations

**Documentation Overhead:**  
The Waterfall approach required significant upfront documentation effort before a single line of code was written. The requirements spec, system design, test plan, and Gantt chart together took approximately 10 hours. While this provided clarity during implementation, it created a rigid contract that made the three change requests (CR-001 to CR-003) disproportionately disruptive — each required revisiting the design document, updating the schema, and re-running affected test cases. Additionally, the comprehensive test plan (26 test cases) identified 12 defects during the testing phase, requiring 8.4 hours of rework. The late discovery of these issues (Week 7) meant that fixes required regression testing of all affected test cases, adding significant overhead to the testing phase.

**Inflexibility Encountered:**  
CR-001 (category field) required a schema change that, in a real Waterfall project, would have triggered a formal change control process. The late injection of this change during the testing phase meant that the create/edit forms, templates, and database all needed simultaneous updates — a cascade effect that would be far more costly in a larger codebase. Similarly, the 12 defects discovered during testing required fixes that cascaded through the codebase, with each fix requiring regression testing to ensure no new issues were introduced. The combination of change requests (5 hours) and defect fixes (8.4 hours) totaled 13.4 hours of rework in the testing phase alone.

**Predictability:**  
The upfront planning made the implementation phase straightforward. Having a frozen schema and route plan before coding meant fewer architectural surprises during development. This is the primary advantage of Waterfall in stable-requirement contexts. However, the testing phase revealed that despite careful design, 12 defects were still discovered, indicating that even comprehensive upfront planning cannot eliminate all issues. The defects ranged from validation errors to session handling issues to notification logic problems, suggesting that iterative testing during development might have caught these issues earlier.

**Comparison Note (for dissertation):**  
The rework effort for the three change requests (~5 hours) plus defect fixes (~8.4 hours) totaled 13.4 hours of rework — representing 45% of total development effort. In an Agile run, these same issues would have been discovered and fixed incrementally during development sprints, with no regression risk to already-delivered features. The late discovery of defects in Waterfall's testing phase is a key weakness compared to Agile's continuous testing approach.
