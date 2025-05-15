# FastAPI Task Manager API

This is a simple, containerized REST API built with **FastAPI**, designed to manage a collection of tasks using CRUD operations. It uses **SQLite** as a local database and provides full support for development and testing with **Docker** and **GitHub Actions** CI/CD.

---

## 🔧 Features

- FastAPI-based REST API
- SQLite database with SQLAlchemy ORM
- Full CRUD (Create, Read, Update, Delete) support
- Input validation using Pydantic
- Unit tests with `pytest`
- Dockerized using `Dockerfile` and `docker-compose`
- CI pipeline using GitHub Actions
- Swagger UI for interactive API documentation

---

## 🚀 Quick Start

### 🔹 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🛠️ Run the API Locally

```bash
# 1. Unzip the project and navigate into it
cd api_project

# 2. Run the app using Docker
chmod +x run.sh
./run.sh
```

Open your browser and visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

### ✅ From Docker

```bash
docker-compose exec api pytest
```

### ✅ Locally (Without Docker)

```bash
pip install -r requirements.txt
pytest
```

---

## 🧰 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | `/tasks/`        | Create a new task   |
| GET    | `/tasks/{id}`    | Retrieve a task     |
| PUT    | `/tasks/{id}`    | Update a task       |
| DELETE | `/tasks/{id}`    | Delete a task       |

You can test all these via [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI).

---

## 📂 Project Structure

```
api_project/
├── app/
│   ├── main.py         # API entry point
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas
│   ├── crud.py         # CRUD logic
│   └── database.py     # DB connection setup
├── tests/              # Pytest unit tests
├── .github/workflows/  # GitHub Actions CI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.sh
└── README.md
```

---

## ⚙️ CI/CD

This project uses GitHub Actions to:
- Install dependencies
- Run all unit tests on push/pull requests to `main`

Config is in `.github/workflows/ci.yml`.

---

## 📌 Notes

- The database (`tasks.db`) is stored inside the Docker volume.
- You can remove the DB file to reset data.

---

## 📬 Contact

Feel free to reach out for improvements, deployment help, or PostgreSQL integration.