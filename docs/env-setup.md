# Django Project with SQLite and Django REST Framework

This project is built using Django with SQLite as the database and Django REST Framework for creating APIs. For testing API endpoints, Postman is used. End-to-end tests are written in `tests.py`.

## Requirements

- Python 3.6 or higher
- Django
- Django REST Framework
- Django REST Framework SimpleJWT

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mastervectormaster/shopping_cart.git
cd shopping_cart
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

By default, this project uses SQLite, which is configured in `settings.py`.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

## Testing API Endpoints with Postman

1. Open Postman.
2. Import the Postman collection (if available) or manually create requests for your API endpoints.
3. Set the appropriate request headers, body, and parameters as needed.

## Running Tests

End-to-end tests are written in the `tests.py` file. To run the tests, use the following command:

```bash
python manage.py test
```

## Useful Links

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
