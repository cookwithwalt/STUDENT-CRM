# Student CRM (Django)

A modern, scalable mini college management system built with Django.

## Features
- Student CRUD (name, email, phone, address)
- Course CRUD (name, duration, description)
- Enrollment management (student + course + enrollment date)
- Search students by name/email
- Dashboard stats (students, courses, enrollments)
- Bootstrap-powered responsive UI

## Project Structure
- `student_crm/` - Django project root
- `student_crm/crm/` - CRM app (models, views, urls, templates)

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   cd student_crm
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run server:
   ```bash
   python manage.py runserver
   ```

## URLs
- `/dashboard/` - Dashboard
- `/students/` - Students list + search
- `/courses/` - Courses list
- `/enrollments/` - Enrollments list
- `/admin/` - Django admin

## If you still see an old form error
If you previously ran the app before pulling this fix, clear cached bytecode and run migrations again:

```bash
# from repository root
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
cd student_crm
python manage.py migrate
python manage.py runserver
```
