# Product Backlog — Agile Run
**Project:** Task Management Web Application  
**Methodology:** Agile (Scrum)  
**Author:** Muhammad Subtain | B01811837  
**Date:** 2026-03-22

---

## Epic: Task Management System
Build a web-based task management application for team collaboration.

---

## User Stories

### Authentication & User Management

**US-001: User Registration**  
*Story Points: 2*  
As a new user, I want to register for an account so that I can access the task management system.

**Acceptance Criteria:**
- User can create account with username, email, and password
- System validates unique username and email
- Password is securely hashed before storage

**US-002: User Login**  
*Story Points: 1*  
As a registered user, I want to log in to my account so that I can access my tasks.

**Acceptance Criteria:**
- User can authenticate with username and password
- Session is maintained across page navigation
- Invalid credentials show appropriate error message

**US-003: User Logout**  
*Story Points: 1*  
As a logged-in user, I want to log out so that my session is secure.

**Acceptance Criteria:**
- User can log out from any page
- Session is completely cleared
- User is redirected to login page

### Task Management Core

**US-004: Task Creation**  
*Story Points: 3*  
As a user, I want to create tasks with details so that I can organize work items.

**Acceptance Criteria:**
- User can create task with title, description, assignee, due date, priority
- Task is saved to database with creator information
- Form validates required fields

**US-005: Task Assignment**  
*Story Points: 2*  
As a user, I want to assign tasks to team members so that work can be distributed.

**Acceptance Criteria:**
- User can select any registered user as assignee
- Assignee receives notification when task is assigned
- Assignment can be changed after task creation

**US-006: Task Status Updates**  
*Story Points: 2*  
As a user, I want to update task status so that progress is tracked.

**Acceptance Criteria:**
- Status can be changed between To Do, In Progress, Done
- Status changes trigger notifications to assignee
- Status history is maintained

### Notifications & Dashboard

**US-007: In-App Notifications**  
*Story Points: 3*  
As a user, I want to receive notifications about task changes so that I stay informed.

**Acceptance Criteria:**
- Notifications appear when tasks are assigned to me
- Notifications appear when my task status changes
- Unread notification count is visible in navigation

**US-008: Personal Dashboard**  
*Story Points: 5*  
As a user, I want a dashboard showing my tasks so that I can see my workload at a glance.

**Acceptance Criteria:**
- Dashboard shows all tasks assigned to me
- Overdue tasks are highlighted
- Recent notifications are displayed

### Enhancement Features (Change Requests)

**US-009: Task Categories**  
*Story Points: 2*  
As a user, I want to categorize tasks so that I can organize them by type.

**Acceptance Criteria:**
- Tasks can be assigned Work, Personal, or Urgent category
- Category is displayed in task lists and dashboard
- Category can be filtered in task views

**US-010: Status Summary Counts**  
*Story Points: 1*  
As a user, I want to see task counts by status so that I can understand my workload distribution.

**Acceptance Criteria:**
- Dashboard shows count of To Do, In Progress, Done tasks
- Counts update automatically when task status changes
- Overdue count is displayed separately

**US-011: Task Comments**  
*Story Points: 3*  
As a user, I want to add comments to tasks so that I can provide updates and context.

**Acceptance Criteria:**
- Users can add text comments to any task
- Comments show author and timestamp
- Comments are displayed chronologically

**US-012: Task List View**  
*Story Points: 2*  
As a user, I want to view all tasks in a filterable list so that I can see the complete project status.

**Acceptance Criteria:**
- All tasks are displayed in a table format
- Tasks can be filtered by status and priority
- Each task shows key details and edit link

---

## Backlog Summary

| Story ID | Title | Story Points | Priority |
|----------|-------|--------------|----------|
| US-001 | User Registration | 2 | High |
| US-002 | User Login | 1 | High |
| US-003 | User Logout | 1 | High |
| US-004 | Task Creation | 3 | High |
| US-005 | Task Assignment | 2 | High |
| US-006 | Task Status Updates | 2 | High |
| US-007 | In-App Notifications | 3 | Medium |
| US-008 | Personal Dashboard | 5 | High |
| US-009 | Task Categories | 2 | Low |
| US-010 | Status Summary Counts | 1 | Low |
| US-011 | Task Comments | 3 | Low |
| US-012 | Task List View | 2 | Medium |

**Total Story Points:** 27  
**Total Stories:** 12