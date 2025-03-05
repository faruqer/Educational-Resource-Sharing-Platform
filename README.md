# Educational Resource Sharing Platform (Django)

## Final Status
- Phase 1: Project bootstrap — DONE
- Phase 2: Authentication and profiles — DONE
- Phase 3: Resource domain models — DONE
- Phase 4: Resource CRUD + search (web) — DONE
- Phase 5: REST API endpoints — DONE
- Phase 6: Basic automated tests — DONE
- Phase 7: Documentation and final polish — DONE



## Features
- User signup, login, logout, and profile management
- Resource categories and educational resource data model
- Resource create/read/update/delete web flows with owner-only edit/delete
- Search and category filtering for resource listing
- REST API for categories and resources
- Basic automated tests for resource model/view behavior

## Run
1. Create and activate a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply initial Django migrations:
   ```bash
   python manage.py migrate
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```

## Run Tests
```bash
python manage.py test
```

Admin URL:
- `http://127.0.0.1:8000/admin/`

Auth URLs:
- `http://127.0.0.1:8000/accounts/signup/`
- `http://127.0.0.1:8000/accounts/login/`
- `http://127.0.0.1:8000/accounts/profile/`

Resource URLs:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/resources/new/`

API URLs:
- `http://127.0.0.1:8000/api/categories/`
- `http://127.0.0.1:8000/api/resources/`

## Tech Stack
- Django 5.1.6
- Django REST Framework 3.15.2
- SQLite (default)
- Django Templates
