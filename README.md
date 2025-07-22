# FastAPI Popularity Poll

This project is a simple web application for voting in a popularity poll. It uses FastAPI for the backend and PostgreSQL for data storage.

## PostgreSQL Setup

The application expects a local PostgreSQL server. The steps below show a basic setup.

1. **Install PostgreSQL**

   On Ubuntu/Debian systems:
   ```bash
   sudo apt-get update
   sudo apt-get install postgresql
   ```

   On macOS with Homebrew:
   ```bash
   brew install postgresql
   ```

2. **Create the database and user**

   Start the PostgreSQL service and then run:
   ```bash
   sudo -u postgres psql -c "CREATE DATABASE polls;"
   sudo -u postgres psql -c "CREATE USER postgres WITH ENCRYPTED PASSWORD 'password';"
   sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE polls TO postgres;"
   ```
   Adjust the username or password if you prefer different credentials.

3. **Verify the connection URL**

   Ensure `DATABASE_URL` in `database.py` matches your setup. By default it is:
   ```
   postgresql://postgres:password@localhost/polls
   ```

Once PostgreSQL is running and configured, continue with the steps below to initialize and run the app.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure PostgreSQL is running and that `DATABASE_URL` in `database.py` matches your configuration.
3. Initialize the database with some sample candidates:
   ```bash
   python init_db.py
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open `http://localhost:8000` in your browser to vote and view results.
