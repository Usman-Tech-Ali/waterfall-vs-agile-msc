# Change Log — Waterfall Run
**Project:** Task Management Web Application  
**Phase:** Testing/Rework (Week 7) — Controlled Late Requirement Changes  
**Author:** Muhammad Subtain | B01811837

---

## Change Requests

| Change ID | Description | Phase Injected | Estimated Rework (hrs) | Actual Rework (hrs) | Disruption Level (Low/Med/High) |
|-----------|-------------|----------------|------------------------|---------------------|----------------------------------|
| CR-001 | Add a "category" field to tasks (Work / Personal / Urgent) | Testing (Week 7, Day 13) | 2 | TBD | TBD |
| CR-002 | Dashboard must show a count of tasks per status (not just a table) | Testing (Week 7, Day 14) | 1 | TBD | TBD |
| CR-003 | Users can add a comment on any task | Testing (Week 7, Day 14) | 3 | TBD | TBD |

---

## Observations

*To be completed after rework is done.*

- CR-001 required a database schema change (new column on `task` table), migration of existing data, and updates to the create/edit forms and templates. In a real Waterfall project this would require formal change approval and re-baseline of the requirements document.
- CR-002 was relatively low disruption — the dashboard query already fetched tasks, so adding a group-by count was a minor template and route change.
- CR-003 required a new database table (`comment`), a new form on the task edit page, and a new route. This was the highest disruption change as it touched models, routes, and templates simultaneously.

---

## Waterfall Disruption Note

In a strict Waterfall process, any change after the requirements freeze requires formal change control: re-approval of the requirements document, re-design of affected components, re-testing of all affected test cases. These three changes, injected during the testing phase, demonstrate the inflexibility characteristic of Waterfall — each required going back to earlier phases rather than being absorbed iteratively.
