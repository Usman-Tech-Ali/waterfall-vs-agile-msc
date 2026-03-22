# System Design Document — Waterfall Run
**Project:** Task Management Web Application  
**Phase:** Design (Week 5)  
**Author:** Muhammad Subtain | B01811837  
**Date:** 2026-03-22

---

## 1. Architecture Overview

```
waterfall_run/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # SQLAlchemy ORM models
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py        # /register, /login, /logout
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── routes.py        # /tasks/*, /dashboard
│   ├── notifications/
│   │   ├── __init__.py
│   │   └── routes.py        # /notifications/*
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── tasks/
│   │   │   ├── dashboard.html
│   │   │   ├── create_task.html
│   │   │   ├── edit_task.html
│   │   │   └── task_list.html
│   │   └── notifications/
│   │       └── notifications.html
│   └── static/
│       └── style.css
├── instance/
│   └── tasks.db             # SQLite database (auto-created)
├── config.py
├── run.py
└── requirements.txt
```

**Pattern:** Flask Application Factory with Blueprints  
**Database:** SQLite via SQLAlchemy ORM  
**Auth:** Flask-Login (session-based)  
**Templating:** Jinja2 (server-rendered)

---

## 2. Database Schema

### Table: `user`
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| username | VARCHAR(80) | UNIQUE, NOT NULL |
| email | VARCHAR(120) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(256) | NOT NULL |

### Table: `task`
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| title | VARCHAR(120) | NOT NULL |
| description | TEXT | NULLABLE |
| priority | VARCHAR(10) | NOT NULL — 'Low', 'Medium', 'High' |
| status | VARCHAR(20) | NOT NULL, DEFAULT 'To Do' |
| due_date | DATE | NOT NULL |
| created_at | DATETIME | DEFAULT now() |
| creator_id | INTEGER | FK → user.id, NOT NULL |
| assignee_id | INTEGER | FK → user.id, NOT NULL |

### Table: `notification`
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| user_id | INTEGER | FK → user.id, NOT NULL |
| message | VARCHAR(255) | NOT NULL |
| is_read | BOOLEAN | DEFAULT False |
| created_at | DATETIME | DEFAULT now() |
| task_id | INTEGER | FK → task.id, NULLABLE |

### Table: `comment` *(CR-003 — added during change control)*
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| task_id | INTEGER | FK → task.id, NOT NULL |
| author_id | INTEGER | FK → user.id, NOT NULL |
| body | TEXT | NOT NULL |
| created_at | DATETIME | DEFAULT now() |

---

## 3. Route Plan

### Auth Blueprint (`/auth`)
| Method | Route | Description |
|--------|-------|-------------|
| GET/POST | `/auth/register` | Registration form |
| GET/POST | `/auth/login` | Login form |
| GET | `/auth/logout` | Logout and redirect |

### Tasks Blueprint (`/`)
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Redirect to dashboard |
| GET | `/dashboard` | User dashboard |
| GET | `/tasks` | All tasks list |
| GET/POST | `/tasks/create` | Create new task |
| GET/POST | `/tasks/<id>/edit` | Edit task (title, desc, assignee, due date, priority, status) |
| POST | `/tasks/<id>/status` | Quick status update |

### Notifications Blueprint (`/notifications`)
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/notifications` | All notifications for current user |
| POST | `/notifications/<id>/read` | Mark single notification as read |
| POST | `/notifications/read-all` | Mark all as read |

---

## 4. UI Page List

| Page | Template | Description |
|------|----------|-------------|
| Login | `auth/login.html` | Username + password form |
| Register | `auth/register.html` | Username, email, password form |
| Dashboard | `tasks/dashboard.html` | Assigned tasks, overdue count, status summary, notifications |
| Task List | `tasks/task_list.html` | All tasks with filter by status/priority |
| Create Task | `tasks/create_task.html` | Task creation form |
| Edit Task | `tasks/edit_task.html` | Edit all task fields + status |
| Notifications | `notifications/notifications.html` | Full notification list |

---

## 5. Key Design Decisions

- **Blueprints** keep auth, tasks, and notifications concerns separated.
- **Flask-Login** `current_user` proxy used throughout templates for nav and access control.
- **Notifications** are created server-side in task routes whenever assignment or status changes occur — no async/websockets needed.
- **Overdue** is computed at query time: `due_date < date.today() AND status != 'Done'`.
- **Password hashing** uses Werkzeug's `generate_password_hash` / `check_password_hash`.
