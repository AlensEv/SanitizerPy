from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sanitize.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'Todo'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(700), nullable=True)
    email = db.Column(db.String(700), nullable=True)
    password = db.Column(db.String(700), nullable=True)
    bad_user_name = db.Column(db.String(700), nullable=True)
    bad_email = db.Column(db.String(700), nullable=True)
    bad_password = db.Column(db.String(700), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/success')
def success_page():
    return render_template('index.html')

def create_tables():
    with app.app_context():
        # Create all tables
        db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        temp_username = request.form['username']
        temp_email = request.form['email']
        temp_password = request.form['password']

        # Create a new Todo object with the form data

        new_submission = Todo(user_name=username, email=email, password=password, bad_user_name=temp_username, bad_email=temp_email, bad_password=temp_password )

        db.session.add(new_submission)
        print("new1")
        # db.session.add(bad_submission)
        print("new2")
        db.session.commit()
        print("new3")
        return redirect('/')

        # try:
        #     # db.session.add(new_submission)
        #     # print("new1")
        #     # db.session.add(bad_submission)
        #     # print("new2")
        #     # db.session.commit()
        #     # print("new3")
        #     # return redirect('/')
        
        # except:
        #     return 'Error'
        
    else:
        # Render the template for GET request
        # Fetch all submissions from the database
        submissions = Todo.query.all()
        return render_template('index.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True , port=8080)
