from sanitize import app, db

# Create an application context
with app.app_context():
    # Create all database tables
    db.drop_all()
    db.create_all()
