from sanitize import sanitize, db

# Create an application context
with sanitize.app_context():
    # Create all database tables
    db.create_all()
