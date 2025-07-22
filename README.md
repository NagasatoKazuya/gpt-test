# FastAPI Popularity Poll

This project is a simple web application for voting in a popularity poll. It uses FastAPI for the backend and PostgreSQL for data storage.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure PostgreSQL and update `DATABASE_URL` in `database.py` if needed.
3. Initialize the database with some sample candidates:
   ```bash
   python init_db.py
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open `http://localhost:8000` in your browser to vote and view results.
