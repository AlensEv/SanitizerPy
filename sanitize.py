from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import pandas as pd

sanitize = Flask(__name__)
sanitize.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sanitize.db'
db = SQLAlchemy(sanitize)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(700), nullable=False)
    email = db.Column(db.String(700), nullable=False)
    password = db.Column(db.String(700), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@sanitize.route('/success')
def success_page():
    return render_template('index.html')

def create_tables():
    with sanitize.app_context():
        # Create all tables
        db.create_all()



# def sanitize_input(input_string):
   
   
#     sanitized_string = input_string.replace("<", "").replace(">", "")
#     return sanitized_string

@sanitize.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new Todo object with the form data
        new_submission = Todo(user_name=username, email=email, password=password)
        print("new sub")

        try:
            db.session.add(new_submission)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
        
        return redirect(url_for('success_page'))  # Redirect to a success page
    else:
        # Render the template for GET request
        # Fetch all submissions from the database
        submissions = Todo.query.all()
        print("I posted ")
        # Render the template for GET request and pass the submissions to it
        return render_template('index.html', submissions=submissions)






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
    sanitize.run(debug=True , port=8080)
