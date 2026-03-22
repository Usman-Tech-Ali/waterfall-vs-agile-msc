# Sprint Planning — Agile Run
**Project:** Task Management Web Application  
**Methodology:** Agile (Scrum)  
**Author:** Muhammad Subtain | B01811837  
**Sprint Duration:** 2 weeks each  
**Timeline:** Weeks 8-10

---

## Sprint 1: Foundation (Week 8)
**Goal:** Establish core authentication and task creation functionality  
**Duration:** Days 1-10 (2 weeks)  
**Capacity:** 9 story points

### Sprint 1 Backlog
| Story ID | Title | Story Points | Notes |
|----------|-------|--------------|-------|
| US-001 | User Registration | 2 | Database setup, models |
| US-002 | User Login | 1 | Flask-Login integration |
| US-003 | User Logout | 1 | Session management |
| US-004 | Task Creation | 3 | Core task model and form |
| US-005 | Task Assignment | 2 | User selection, basic notifications |

**Sprint 1 Total:** 9 story points

### Sprint 1 Technical Tasks
- Set up Flask application structure
- Configure SQLAlchemy and database models
- Implement authentication system
- Create basic HTML templates and CSS
- Set up task creation and assignment flow

---

## Sprint 2: Core Features (Week 9)
**Goal:** Complete task management workflow and notification system  
**Duration:** Days 11-20 (2 weeks)  
**Capacity:** 10 story points

### Sprint 2 Backlog
| Story ID | Title | Story Points | Notes |
|----------|-------|--------------|-------|
| US-006 | Task Status Updates | 2 | Status workflow implementation |
| US-007 | In-App Notifications | 3 | Notification system and display |
| US-008 | Personal Dashboard | 5 | Main user interface |

**Sprint 2 Total:** 10 story points

### Mid-Sprint Backlog Refinement
During Sprint 2, the following change requests will be added to the backlog:
- US-009: Task Categories (2 SP) → Added to Sprint 3
- US-010: Status Summary Counts (1 SP) → Added to Sprint 3  
- US-011: Task Comments (3 SP) → Added to Sprint 3

### Sprint 2 Technical Tasks
- Implement task status update workflow
- Build notification creation and display system
- Create comprehensive dashboard with task overview
- Add task filtering and search capabilities

---

## Sprint 3: Enhancement & Polish (Week 10)
**Goal:** Implement change requests and complete remaining features  
**Duration:** Days 21-30 (2 weeks)  
**Capacity:** 8 story points

### Sprint 3 Backlog
| Story ID | Title | Story Points | Notes |
|----------|-------|--------------|-------|
| US-012 | Task List View | 2 | All tasks view with filters |
| US-009 | Task Categories | 2 | CR-001: Work/Personal/Urgent |
| US-010 | Status Summary Counts | 1 | CR-002: Dashboard counts |
| US-011 | Task Comments | 3 | CR-003: Task commenting system |

**Sprint 3 Total:** 8 story points

### Sprint 3 Technical Tasks
- Add category field to task model and forms
- Implement status count widgets on dashboard
- Build commenting system for tasks
- Create comprehensive task list view
- Polish UI/UX and fix any remaining bugs

---

## Release Planning Summary

| Sprint | Story Points Planned | Key Deliverables |
|--------|---------------------|------------------|
| Sprint 1 | 9 | Authentication + Task Creation |
| Sprint 2 | 10 | Status Updates + Notifications + Dashboard |
| Sprint 3 | 8 | Enhancements + Change Requests |
| **Total** | **27** | **Complete Task Management System** |

### Definition of Done
- [ ] Code is written and tested
- [ ] Feature works in browser
- [ ] No critical bugs
- [ ] Code is committed to repository
- [ ] Acceptance criteria are met
- [ ] Feature is demonstrated in sprint review

### Velocity Assumptions
- Target velocity: 8-10 story points per sprint
- Based on single developer capacity
- Includes time for testing and bug fixes
- Buffer for learning curve in Sprint 1