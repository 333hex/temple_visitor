"""Legacy compatibility module.

This project registers all Flask routes in app.py to avoid route duplication
when the application is imported in different ways.
"""

from app import app  # noqa: F401
