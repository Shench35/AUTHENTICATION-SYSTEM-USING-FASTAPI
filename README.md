# Authentication System Using FastAPI

A robust and secure authentication system built with FastAPI, providing user registration, login, and token-based authentication.

## Features

- User registration with email validation
- Secure password hashing
- JWT (JSON Web Token) based authentication
- Protected routes and endpoints
- User login and logout functionality
- Token refresh mechanism
- Password reset capabilities

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **JWT** - JSON Web Tokens for secure authentication
- **Passlib** - Password hashing library
- **PostgreSQL/SQLite** - Database (specify which one you're using)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-auth-system.git
cd fastapi-auth-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
DATABASE_URL=sqlite:///./auth.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication

#### Register a new user
```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "securepassword123"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=securepassword123
```

#### Get current user
```http
GET /api/auth/me
Authorization: Bearer <your-jwt-token>
```

#### Refresh token
```http
POST /api/auth/refresh
Authorization: Bearer <your-refresh-token>
```

## Usage Example

```python
import requests

# Register a new user
response = requests.post(
    "http://localhost:8000/api/auth/register",
    json={
        "email": "newuser@example.com",
        "username": "newuser",
        "password": "password123"
    }
)

# Login
response = requests.post(
    "http://localhost:8000/api/auth/login",
    data={
        "username": "newuser@example.com",
        "password": "password123"
    }
)
token = response.json()["access_token"]

# Access protected route
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(
    "http://localhost:8000/api/auth/me",
    headers=headers
)
```

## Project Structure

```
fastapi-auth-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── routers/
│   │   └── auth.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   └── database.py
│
├── tests/
│   └── test_auth.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Security Features

- Passwords are hashed using bcrypt
- JWT tokens with configurable expiration
- Protected routes using dependency injection
- CORS middleware configured
- Environment-based configuration

## Testing

Run the test suite:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=app tests/
```

## Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/fastapi-auth-system](https://github.com/yourusername/fastapi-auth-system)

## Acknowledgments

- FastAPI documentation
- JWT.io
- Python community