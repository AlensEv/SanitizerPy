from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sanitize.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    user_name = db.Column(db.String(700), nullable=False )
    email = db.Column(db.String(700), nullable=False )
    password = db.Column(db.String(700), nullable=False )
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id



def create_tables():
    with app.app_context():
        # Create all tables
        db.create_all()



# def sanitize_input(input_string):
   
   
#     sanitized_string = input_string.replace("<", "").replace(">", "")
#     return sanitized_string

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def process():
#     # Get user input from the form
#     user_input = request.form['user_input']
    
#     # Sanitize the input
#     sanitized_input = sanitize_input(user_input)
    
#     # Store the sanitized input in the CSV file
#     with open('inputs.csv', 'a') as file:
#         file.write(f"{user_input},{sanitized_input}\n")
    
#   #  return "Input sanitized and stored successfully!"

# @app.route('/Userlogin')
# def display():
#     # Read the data from the CSV file
#     df = pd.read_csv('inputs.csv', names=['user_input', 'sanitized_input'])
    
#     # Render the data in an HTML template
#     return render_templates('display.html', data=df)

if __name__ == '__main__':
    app.run(debug=True)