# Metrics Summary — Agile Run
**Project:** Task Management Web Application  
**Methodology:** Agile (Scrum)  
**Author:** Muhammad Subtain | B01811837  
**Completion Date:** 2026-04-19

---

## Hours by Sprint

| Sprint | Planned Hours | Actual Hours | Variance |
|--------|---------------|--------------|----------|
| Sprint 1 | 18 | 19.0 | +1.0 |
| Sprint 2 | 18 | 17.5 | -0.5 |
| Sprint 3 | 16 | 16.0 | 0.0 |
| **Total** | **52** | **52.5** | **+0.5** |

---

## Story Points Delivery

| Sprint | Planned SP | Delivered SP | Velocity |
|--------|------------|--------------|----------|
| Sprint 1 | 9 | 9 | 9 |
| Sprint 2 | 10 | 10 | 10 |
| Sprint 3 | 8 | 8 | 8 |
| **Total** | **27** | **27** | **9 avg** |

**Delivery Rate:** 100% (27/27 story points completed)

---

## Defects Summary

| Metric | Value |
|--------|-------|
| Total defects found | 7 |
| High severity | 1 |
| Medium severity | 4 |
| Low severity | 2 |
| Total fix effort (hrs) | 3.1 |
| Average fix time per defect | 0.44 hrs |

---

## Change Request Integration

| Change Request | Story Points | Sprint Added | Rework Hours | Disruption Level |
|----------------|--------------|--------------|--------------|------------------|
| CR-001: Task Categories | 2 | Sprint 3 | 2.5 | Low |
| CR-002: Status Counts | 1 | Sprint 3 | 1.5 | Low |
| CR-003: Task Comments | 3 | Sprint 3 | 4.0 | Low |
| **Total** | **6** | | **8.0** | **Low** |

**Change Request Efficiency:** All CRs integrated through normal backlog refinement with zero schedule impact.

---

## Feature Delivery

| Feature Category | Stories | Delivered | Success Rate |
|------------------|---------|-----------|--------------|
| Authentication | 3 | 3 | 100% |
| Core Task Management | 4 | 4 | 100% |
| Notifications & Dashboard | 2 | 2 | 100% |
| Enhancement Features | 3 | 3 | 100% |
| **Total** | **12** | **12** | **100%** |

---

## Qualitative Observations

### Sprint Planning Efficiency
Agile sprint planning sessions (1-1.5 hours each) were significantly more efficient than the upfront Waterfall documentation phase. The iterative approach allowed for just-in-time planning that adapted to emerging requirements and technical discoveries.

### Flexibility in Change Management
The three change requests (CR-001, CR-002, CR-003) were seamlessly integrated through standard backlog refinement during Sprint 2. Unlike Waterfall's formal change control process, these were treated as normal user stories and prioritized against existing backlog items. No existing work was disrupted or required rework.

### Iterative Feedback Value
Regular sprint reviews and daily development cycles provided continuous validation of features. The dashboard (US-008) evolved significantly between Sprint 2 planning and completion based on hands-on experience with the task management workflow. This iterative refinement would not have been possible in a Waterfall approach.

### Risk Mitigation Through Early Delivery
Critical authentication and core task functionality were delivered in Sprint 1, providing a working foundation that reduced project risk. Issues with notification logic (3 defects) were discovered and resolved in Sprint 2 before they could impact the final delivery.

### Technical Debt Management
The flexible sprint structure allowed for technical improvements and refactoring as part of normal development. The comment system (CR-003) benefited from lessons learned during notification implementation, resulting in cleaner code architecture.

---

## Agile vs Waterfall Comparison (Dissertation Context)

### Adaptability
- **Agile Advantage:** Change requests absorbed with 8.0 hours of normal development effort
- **Waterfall Challenge:** Same changes would have required formal change control, documentation updates, and regression testing of completed phases

### Quality Assurance
- **Agile Benefit:** 7 defects found and fixed immediately (3.1 hours total)
- **Waterfall Risk:** Issues would accumulate until testing phase, requiring more extensive rework

### Stakeholder Engagement
- **Agile Value:** Regular sprint reviews would provide continuous stakeholder feedback and course correction opportunities
- **Waterfall Limitation:** Stakeholder input limited to formal milestone reviews with limited flexibility for changes

### Predictability vs Flexibility
- **Agile Balance:** Consistent 9 story point average velocity provided predictable delivery while maintaining flexibility for requirement changes
- **Waterfall Trade-off:** High predictability in process but low adaptability to changing requirements

### Time to Value
- **Agile Delivery:** Working authentication and task creation available after Sprint 1 (Week 8)
- **Waterfall Delivery:** No working features until final integration phase (Week 7)

---

## Key Success Factors

1. **Consistent Sprint Rhythm:** 2-week sprints provided optimal balance of planning overhead and delivery momentum
2. **Effective Backlog Management:** Regular refinement sessions enabled smooth integration of changing requirements
3. **Early Risk Mitigation:** Core functionality delivered first, reducing project risk
4. **Continuous Quality:** Defects caught and resolved immediately, preventing accumulation
5. **Stakeholder Value:** Each sprint delivered working software that could provide immediate value

---

## Recommendations for Future Agile Projects

- Maintain 2-week sprint duration for optimal rhythm and feedback cycles
- Invest in good initial architecture to support iterative enhancement
- Use story points consistently for reliable velocity tracking and capacity planning
- Prioritize core functionality in early sprints to establish solid foundation
- Embrace change requests as opportunities for value enhancement rather than scope disruption