### Expense Tracker API (FastAPI + PostgreSQL)

* A simple and efficient Expense Tracker Backend API built using FastAPI, PostgreSQL, and Docker/virtual environment.
* This API allows users to add, update, delete, and view expenses with proper database storage.

### Features

* Fast and lightweight FastAPI backend
* CRUD operations for expenses
* PostgreSQL database connection using psycopg2
* Environment variables managed with dotenv
* Modular project structure using APIRouters
* JSON responses for all endpoints

### 📂 Project Structure
expense-tracker/
│── main_exp.py
│── exp_cal.py
│── exp_show.py
│── requirements.txt
│── .env

### 🛠️ Installation & Setup
1️. Clone Repo
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows

3️. Install Dependencies
pip install -r requirements.txt

4️. Setup Environment Variables
Create .env:
   DB_HOST=localhost
   DB_NAME=yourdbname
   DB_USER=yourdbuser
   DB_PASS=yourdbpassword
   DB_PORT=5432

5️. Run FastAPI App
uvicorn app:app --reload

### Swagger UI:
http://127.0.0.1:8000/docs


### Summary
> This project is an Employee Risk Tracker built with FastAPI and Streamlit, where employee data is stored in PostgreSQL.
> It calculates savings and risk scores based on salary, expenses, attendance, and performance, and visualizes the results through an interactive dashboard.
