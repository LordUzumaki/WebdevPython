#import necessary libraries from Flask
from flask import Flask, render_template, request, redirect, url_for

#Initialize the Flask application
app = Flask(__name__)

#Define the route for the home page
@app_route('/')
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
        
        #redirect to the thank you page with the name parameter
        