# Finance RBAC Backend

A Django-based backend system for managing financial records with role-based access control (RBAC).

---
[![Django Docker CI](https://github.com/yakshithkd23/finance-rbac-backend-django/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/yakshithkd23/finance-rbac-backend-django/actions/workflows/docker-ci.yml)
##  Features

* User roles (Viewer, Analyst, Admin)
* Financial records CRUD
* Filtering support
* Dashboard analytics
* RBAC enforcement
* PostgreSQL with Docker

---

##  Tech Stack

* Python / Django
* PostgreSQL
* Docker & Docker Compose

---

##  Setup

### Run with Docker

```bash
docker compose up --build
```

---

##  Project Structure

* `users/` → User management & roles
* `records/` → Financial records
* `dashboard/` → Analytics
* `config/` → Project settings

---

##  API Reference

For detailed API documentation:
 https://drive.google.com/drive/folders/1RUomV5mANADqLpR7JhA5AIiXVUzwXugB?usp=drive_link

---

##  CI/CD

This project uses GitHub Actions for Continuous Integration:

* Docker-based testing
* Automated migrations
* Test execution on every push & pull request

---

##  Author

* Yakshith K D
