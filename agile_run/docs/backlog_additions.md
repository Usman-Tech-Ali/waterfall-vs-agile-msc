# Backlog Additions — Agile Run
**Project:** Task Management Web Application  
**Event:** Mid-Project Change Requests via Backlog Refinement  
**Date:** Sprint 2, Day 9 (2026-04-09)  
**Author:** Muhammad Subtain | B01811837

---

## Change Request Integration Process

During Sprint 2 backlog refinement session, three new requirements were identified and added to the product backlog. Unlike traditional Waterfall change control, these were handled through standard Agile backlog management practices.

---

## CR-001: Task Categories

**Story ID:** US-009  
**Title:** Task Categories  
**Description:** As a user, I want to categorize tasks so that I can organize them by type.  
**Story Points Assigned:** 2  
**Priority:** Low  
**Added to Sprint:** Sprint 3

### Integration Details
- **Impact Assessment:** Requires new database column, form field updates, display changes
- **Dependencies:** None - can be implemented independently
- **Accommodation:** Added to Sprint 3 without removing existing stories
- **Effort Estimate:** 2 story points (database migration + UI updates)

### Acceptance Criteria Added
- Tasks can be assigned Work, Personal, or Urgent category
- Category is displayed in task lists and dashboard
- Category can be filtered in task views

---

## CR-002: Status Summary Counts

**Story ID:** US-010  
**Title:** Status Summary Counts  
**Description:** As a user, I want to see task counts by status so that I can understand my workload distribution.  
**Story Points Assigned:** 1  
**Priority:** Low  
**Added to Sprint:** Sprint 3

### Integration Details
- **Impact Assessment:** Dashboard enhancement, requires query aggregation
- **Dependencies:** Builds on existing dashboard (US-008)
- **Accommodation:** Small addition to Sprint 3 scope
- **Effort Estimate:** 1 story point (dashboard widget + query logic)

### Acceptance Criteria Added
- Dashboard shows count of To Do, In Progress, Done tasks
- Counts update automatically when task status changes
- Overdue count is displayed separately

---

## CR-003: Task Comments

**Story ID:** US-011  
**Title:** Task Comments  
**Description:** As a user, I want to add comments to tasks so that I can provide updates and context.  
**Story Points Assigned:** 3  
**Priority:** Low  
**Added to Sprint:** Sprint 3

### Integration Details
- **Impact Assessment:** New database table, comment model, UI components
- **Dependencies:** Requires task edit page (part of US-006)
- **Accommodation:** Largest addition but fits within Sprint 3 capacity
- **Effort Estimate:** 3 story points (new model + forms + display)

### Acceptance Criteria Added
- Users can add text comments to any task
- Comments show author and timestamp
- Comments are displayed chronologically

---

## Sprint Capacity Impact

### Original Sprint 3 Plan
| Story ID | Title | Story Points |
|----------|-------|--------------|
| US-012 | Task List View | 2 |
| **Subtotal** | | **2** |

### Revised Sprint 3 Plan (After Backlog Refinement)
| Story ID | Title | Story Points | Type |
|----------|-------|--------------|------|
| US-012 | Task List View | 2 | Original |
| US-009 | Task Categories | 2 | CR-001 |
| US-010 | Status Summary Counts | 1 | CR-002 |
| US-011 | Task Comments | 3 | CR-003 |
| **Total** | | **8** | |

### Capacity Management
- **Original Sprint 3 Capacity:** 8 story points
- **Change Request Points:** 6 story points
- **Total Sprint 3 Load:** 8 story points
- **Accommodation Strategy:** No existing stories removed - change requests fit within planned capacity

---

## Agile Change Management Benefits

### Seamless Integration
- **No Formal Change Control:** Changes added through normal backlog refinement
- **No Documentation Overhead:** Standard user story format used
- **No Schedule Disruption:** Changes accommodated within existing sprint structure
- **No Scope Freeze Issues:** Backlog remains flexible and responsive

### Stakeholder Value
- **Immediate Feedback:** Changes can be incorporated in next sprint
- **Prioritization Flexibility:** Change requests prioritized against existing backlog
- **Iterative Refinement:** Requirements can evolve based on working software demos
- **Risk Mitigation:** Changes tested and integrated incrementally

### Comparison to Waterfall Approach
In a Waterfall methodology, these same changes would have required:
- Formal change request documentation
- Impact analysis and approval process
- Requirements document updates
- Design document revisions
- Test plan modifications
- Potential schedule and budget revisions

In Agile, they were handled as normal backlog items with standard story point estimation and sprint planning.

---

## Lessons Learned

### Effective Practices
- **Regular Refinement:** Mid-sprint refinement sessions enable responsive change management
- **Story Point Estimation:** Consistent estimation helps assess change impact quickly
- **Capacity Planning:** Maintaining sprint capacity buffer allows for change accommodation
- **Stakeholder Engagement:** Regular demos and reviews surface change needs early

### Success Factors
- **Flexible Backlog:** Product backlog designed to accommodate changing priorities
- **Team Velocity:** Consistent velocity enables predictable change integration
- **Technical Architecture:** Well-designed initial architecture supports feature additions
- **Communication:** Clear acceptance criteria ensure change requirements are understood