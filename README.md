# 📓 Minimalist Notes API
**A high-performance CRUD application bridging FastAPI efficiency with clean architectural design.**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)

---

## 🌟 Overview
This project is a sophisticated **Notes Management System** built to demonstrate the seamless integration of a Python backend with a distraction-free frontend. It utilizes **SQLAlchemy** for ORM and **Jinja2** for server-side rendering, ensuring a fast and scalable user experience.

### ✨ Key Features
* **Full CRUD Lifecycle:** Create, Read, Update, and Delete notes with instant database persistence.
* **Architectural Integrity:** Clean separation of concerns using `models`, `schemas`, and `database` configurations.
* **Minimalist UI:** A CSS-driven interface designed for focus and modern aesthetics.
* **Auto-Generated Docs:** Built-in Swagger UI access for real-time API testing.

---

## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, FastAPI |
| **Database** | MySQL (via SQLAlchemy ORM) |
| **Frontend** | HTML5, CSS3, Jinja2 Templates |
| **Validation** | Pydantic Models |

---

## 📂 Project Structure
```text
notes_app/
├── static/          # Custom CSS & Branding
├── templates/       # Jinja2 HTML Layouts
├── database.py      # Engine & Session configuration
├── main.py          # Application entry point & Routes
├── models.py        # SQLAlchemy database schemas
├── schemas.py       # Pydantic data validation
└── requirements.txt # Project dependencies
