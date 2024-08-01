#import necessary libraries from Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Initialize the Flask application
app = Flask(__name__)

#Configure the SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Disable modificaion tracker system

#Initialize the SQLAlchemy object
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Primary key column
    name = db.Column(db.String(100), nullable=False) #Name column
    email = db.Column(db.String(100), nullable=False) #Email column
#Define the route for the home page
@app.route('/')
def home():
    #Render the home.html template
    return render_template('home.html')

#Define the route for the form page with both GET and POST methods
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        #Get the name and email from the form
        name = request.form.get('name')
        email = request.form.get('email')
        #Validate the input
        if not name or not email:
            return 'Invalid input. Please go back and try again.', 400
        #Create a new User object and add it to the database
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        #redirect to the thank you page with the name parameter
        return redirect(url_for('thank_you', name=name))
    #Render the form.html template
    return render_template('form.html')

#Define the route for the thank you page
@app.route('/thank_you')
def thank_you():
    #get the name parameter from the URL
    name = request.args.get('name')
    #return a thank you message
    return f'Thank you, {name}'

#Run the Flask Application

if __name__ == '__name__':
    #Create the database tables
    db.create_all()
    app.run(debug=True)
    