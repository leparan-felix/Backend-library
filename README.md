Library Backend API

This is the backend API for the Library App Frontend, built with Flask and SQLite/PostgreSQL. It provides a secure and scalable RESTful API for user management, item cataloging, task tracking, and commenting.
🔍 Overview

    🔐 User authentication with JWT

    📘 Item catalog for library entries

    ✅ Task management for users

    💬 Comment system

    🔎 Search functionality

    🔁 Token refresh support

    🧾 Validation, error handling, and secure password storage

⚙️ Technologies Used

    Flask

    SQLAlchemy

    Flask-JWT-Extended

    Flask-Migrate + Alembic

    Flask-Limiter

    bcrypt

    SQLite (dev) / PostgreSQL (prod)

    CORS for frontend connection

🚀 Setup Instructions
1. Clone the Repository

git clone git@github.com:leparan-felix/Backend-library.git
cd library-backend

2. Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Environment Configuration

Create a .env file:

FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=sqlite:///instance/library.db

5. Database Setup

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Or seed data:

python seed.py

6. Start the Server

flask run

Server will run at: http://localhost:5000
🔐 Authentication

    Passwords hashed with bcrypt

    JWT issued on login

    Refresh tokens supported

    All routes (except /api/register & /api/login) require a valid JWT

📑 API Documentation
🧑 User Management
Method	Endpoint	Description
POST	/api/register	Register a new user
POST	/api/login	Login and receive JWT
GET	/api/profile	Get user profile (auth required)
PUT	/api/profile	Update user profile
POST	/api/refresh	Get a new JWT using refresh token
Example: Register

POST /api/register
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "secure123"
}

✅ Task Management
Method	Endpoint	Description
POST	/api/tasks	Create a new task
GET	/api/tasks	List all tasks
PUT	/api/tasks/:id	Update a task
DELETE	/api/tasks/:id	Delete a task
📘 Item Catalog
Method	Endpoint	Description
POST	/api/items	Add a new item
GET	/api/items	List items (filter by category)
PUT	/api/items/:id	Update item
DELETE	/api/items/:id	Delete item
💬 Comment System
Method	Endpoint	Description
POST	/api/comments	Add a comment to an item
GET	/api/comments/:item_id	Get comments for an item
DELETE	/api/comments/:id	Delete comment (author or admin only)
🔎 Search
Method	Endpoint	Description
GET	/api/search	Search items/tasks by title/content

Example:

GET /api/search?q=fiction

📦 Token Refresh
Method	Endpoint	Description
POST	/api/refresh	Refresh access token
⚠️ Error Handling
Status	Description
400	Bad request or validation
401	Unauthorized (missing/invalid token)
404	Resource not found
500	Server error
📤 Deployment (Render / Railway / Heroku)
Docker (Optional)

Dockerfile

FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

docker build -t library-backend .
docker run -p 5000:5000 library-backend

Render (Example)

    Add environment variables in dashboard

    Build Command: pip install -r requirements.txt

    Start Command: flask run

🔗 Frontend

This API powers the frontend at:

👉 https://library-app-ecmu.vercel.app
📄 License




