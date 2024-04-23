from flask import Flask, render_template, url_for, redirect, request, session
# import pandas as pd

sanitize = Flask(__name__)

# def sanitize_input(input_string):
   
   
#     sanitized_string = input_string.replace("<", "").replace(">", "")
#     return sanitized_string

@sanitize.route('/')
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
    sanitize.run(debug=True)