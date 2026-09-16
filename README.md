# Temple Visitor Management System

A simple Flask application for managing temple visitor registrations.

## Features
- Visitor registration form
- Visitor list display
- SQLite database persistence
- Environment-based configuration

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite

## Getting Started

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   - Home: http://localhost:5000/
   - Registration form: http://localhost:5000/register
   - Visitor list: http://localhost:5000/visitors

## Configuration
The app uses environment variables. You can create a `.env` file with values such as:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///temple_visitor.db
```

If `DATABASE_URL` is not set, the app falls back to a SQLite database named `temple_visitor.db`.

## Project Structure
- `app.py` — Flask application entry point
- `config.py` — application configuration
- `models.py` — database models
- `templates/` — HTML templates
- `static/` — static assets
- `requirements.txt` — Python package dependencies

## Notes
The app creates the database tables automatically on startup when the Flask app is initialized.
