# Test Plan — Waterfall Run
**Project:** Task Management Web Application  
**Phase:** Design (written before coding begins)  
**Author:** Muhammad Subtain | B01811837  
**Date:** 2026-03-22

---

## Test Approach

Manual black-box testing via browser. Each test case is executed after full implementation. Results logged in `defect_log.md`. Regression tests re-run after each change request is applied.

---

## Test Cases

### Authentication

| TC-ID | Feature | Test Description | Steps | Expected Result | Status |
|-------|---------|-----------------|-------|-----------------|--------|
| TC-01 | Registration | Valid registration | 1. Navigate to /auth/register 2. Enter unique username, email, password 3. Submit | User created, redirected to login page | — |
| TC-02 | Registration | Duplicate username | 1. Register with existing username | Error message shown, user not created | — |
| TC-03 | Registration | Duplicate email | 1. Register with existing email | Error message shown, user not created | — |
| TC-04 | Registration | Empty required fields | 1. Submit form with blank username | Validation error shown | — |
| TC-05 | Login | Valid credentials | 1. Navigate to /auth/login 2. Enter correct username/password 3. Submit | Session created, redirected to dashboard | — |
| TC-06 | Login | Invalid password | 1. Enter correct username, wrong password | Error message shown, no session created | — |
| TC-07 | Login | Non-existent user | 1. Enter username that doesn't exist | Error message shown | — |
| TC-08 | Logout | Logout flow | 1. While logged in, navigate to /auth/logout | Session cleared, redirected to login | — |
| TC-09 | Auth guard | Access protected route unauthenticated | 1. Without logging in, navigate to /dashboard | Redirected to login page | — |

### Task Management

| TC-ID | Feature | Test Description | Steps | Expected Result | Status |
|-------|---------|-----------------|-------|-----------------|--------|
| TC-10 | Task Creation | Create valid task | 1. Login 2. Navigate to /tasks/create 3. Fill all fields 4. Submit | Task saved, notification created for assignee, redirected to dashboard | — |
| TC-11 | Task Creation | Missing required field | 1. Submit task form without title | Validation error shown, task not saved | — |
| TC-12 | Task Creation | Due date in past | 1. Submit task with past due date | Task saved (no restriction), appears as overdue on dashboard | — |
| TC-13 | Task Edit | Edit task fields | 1. Navigate to /tasks/<id>/edit 2. Change title and priority 3. Submit | Changes saved and reflected on dashboard | — |
| TC-14 | Task Edit | Change assignee | 1. Edit task, select different assignee | New assignee receives notification | — |
| TC-15 | Status Update | Update status To Do → In Progress | 1. On edit page, change status to In Progress | Status updated, notification generated | — |
| TC-16 | Status Update | Update status In Progress → Done | 1. Change status to Done | Status updated, task no longer counted as overdue | — |

### Notifications

| TC-ID | Feature | Test Description | Steps | Expected Result | Status |
|-------|---------|-----------------|-------|-----------------|--------|
| TC-17 | Notification | Notification on task assignment | 1. User A creates task assigned to User B 2. Login as User B | Notification visible on dashboard and /notifications | — |
| TC-18 | Notification | Notification on status change | 1. Update task status 2. Check assignee notifications | New notification appears for assignee | — |
| TC-19 | Notification | Mark as read | 1. Click mark-as-read on a notification | Notification marked read, unread count decreases | — |
| TC-20 | Notification | Mark all as read | 1. Click mark-all-read | All notifications marked read, count shows 0 | — |

### Dashboard

| TC-ID | Feature | Test Description | Steps | Expected Result | Status |
|-------|---------|-----------------|-------|-----------------|--------|
| TC-21 | Dashboard | Overdue count | 1. Create task with past due date, status To Do 2. View dashboard | Overdue count reflects the task | — |
| TC-22 | Dashboard | Status summary | 1. Create tasks with different statuses 2. View dashboard | Summary table shows correct counts per status | — |
| TC-23 | Dashboard | Only assigned tasks shown | 1. Login as User B 2. View dashboard | Only tasks assigned to User B are shown | — |

---

## Change Request Test Cases (added after CR injection)

| TC-ID | CR | Test Description | Expected Result | Status |
|-------|----|-----------------|-----------------|--------|
| TC-24 | CR-001 | Create task with category | Category field visible, value saved and displayed | — |
| TC-25 | CR-002 | Dashboard status counts | Counts for To Do / In Progress / Done shown as numbers | — |
| TC-26 | CR-003 | Add comment to task | Comment saved and displayed on task edit page | — |

---

## Pass/Fail Criteria

- All TC-01 through TC-23 must pass before the project is considered complete.
- Any failure is logged in `defect_log.md` with severity and fix effort.
- TC-24 through TC-26 are regression tests run after change requests are applied.
