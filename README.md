# Educational Resource Sharing Platform (Django)

## Current Phase
- Authentication and Profile Management are DONE
- Resource domain models are DONE

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

Admin URL:
- `http://127.0.0.1:8000/admin/`

Auth URLs:
- `http://127.0.0.1:8000/accounts/signup/`
- `http://127.0.0.1:8000/accounts/login/`
- `http://127.0.0.1:8000/accounts/profile/`
