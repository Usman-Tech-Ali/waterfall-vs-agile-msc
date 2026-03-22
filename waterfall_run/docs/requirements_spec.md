# Requirements Specification — Waterfall Run
**Project:** Task Management Web Application  
**Phase:** Requirements (Week 5)  
**Methodology:** Waterfall  
**Author:** Muhammad Subtain | B01811837  
**Date:** 2026-03-22  
**Status:** FROZEN — No changes permitted after sign-off

---

## 1. Project Overview

A server-rendered web application for managing tasks among registered users. Built with Python/Flask, SQLite/SQLAlchemy, and HTML/Jinja2 templates. All requirements are defined upfront and frozen before any design or coding begins.

---

## 2. Functional Requirements

### FR-01: User Registration
- The system shall allow a new user to register with a unique username, email address, and password.
- Passwords shall be stored as hashed values (bcrypt).
- Duplicate usernames or emails shall be rejected with an appropriate error message.
- On successful registration, the user is redirected to the login page.

### FR-02: User Login / Logout
- The system shall authenticate users via username and password.
- On successful login, a session is created using Flask-Login.
- On logout, the session is destroyed and the user is redirected to the login page.
- Unauthenticated users attempting to access protected routes shall be redirected to login.

### FR-03: Task Creation
- Authenticated users shall be able to create a task with the following fields:
  - Title (required, max 120 characters)
  - Description (optional, text)
  - Assignee (required, selected from list of registered users)
  - Due Date (required, date picker)
  - Priority (required, enum: Low / Medium / High)
- The creator of the task is recorded automatically.
- On creation, a notification is generated for the assignee.

### FR-04: Task Assignment
- A task may be assigned to any registered user at creation time.
- The assignee can be changed after creation by the task creator.
- Reassignment shall generate a new notification for the new assignee.

### FR-05: Task Status Updates
- Tasks shall have a status field with three allowed values: To Do, In Progress, Done.
- Default status on creation is "To Do".
- Any authenticated user can update the status of a task assigned to them.
- The task creator can update the status of any task they created.
- A notification is generated for the assignee when status changes.

### FR-06: In-App Notifications
- The system shall generate a notification record when:
  - A task is assigned to a user (on creation or reassignment).
  - A task's status is updated.
- Notifications are displayed on the user's dashboard.
- Notifications have a read/unread state.
- Users can mark notifications as read.
- Unread notification count is shown in the navigation bar.

### FR-07: Dashboard
- The authenticated user's dashboard shall display:
  - A table of all tasks assigned to the current user.
  - Each row shows: Title, Priority, Status, Due Date, Creator.
  - A count of overdue tasks (due date < today and status != Done).
  - A summary table of task counts by status (To Do / In Progress / Done).
  - A list of unread notifications.

---

## 3. Non-Functional Requirements

### NFR-01: Security
- Passwords must never be stored in plaintext.
- All routes that return user data must require authentication.
- CSRF protection via Flask-WTF (or equivalent form token).

### NFR-02: Performance
- All page loads shall complete within 2 seconds under normal single-user load.
- Database queries shall use indexed foreign keys.

### NFR-03: Usability
- The UI shall be functional and readable without any JavaScript frameworks.
- Forms shall display inline validation errors.
- Navigation shall be consistent across all pages.

### NFR-04: Maintainability
- Code shall follow PEP 8 style guidelines.
- Application shall use the Flask application factory pattern.
- Database models shall be defined using SQLAlchemy ORM.

### NFR-05: Portability
- The application shall run on Python 3.10+ with dependencies listed in requirements.txt.
- The SQLite database file shall be stored locally under /instance/.

---

## 4. Constraints

- No external APIs or email services.
- No JavaScript-heavy frontend frameworks (React, Vue, etc.).
- No Redis or background task queues.
- Must run fully locally.
- Frontend: HTML + Jinja2 + minimal plain CSS only.

---

## 5. Out of Scope (Baseline)

- Password reset via email.
- File attachments on tasks.
- Admin panel.
- Role-based access control beyond creator/assignee rules.

---

## 6. Acceptance Criteria Summary

| ID | Feature | Acceptance Criterion |
|----|---------|----------------------|
| AC-01 | Registration | New user can register and is stored in DB |
| AC-02 | Login | Valid credentials create a session |
| AC-03 | Logout | Session is cleared on logout |
| AC-04 | Task Creation | Task saved with all fields, notification created |
| AC-05 | Task Assignment | Assignee receives notification |
| AC-06 | Status Update | Status changes saved, notification generated |
| AC-07 | Notifications | Unread count shown in nav, markable as read |
| AC-08 | Dashboard | Shows assigned tasks, overdue count, status summary |
