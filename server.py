from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'KeepItSecretKeepItSafe'
# Routes and Locations Below!
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
	if len(request.form['firstname']) < 1:
		flash("Name cannot be empty")
	elif len(request.form['lastname']) < 1:
		flash("Last Name cannot be empty")
	elif len(request.form['email']) < 1:
		flash('Email cannot be blank')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address")
	elif len(request.form['password']) < 1:
		flash("Provide a password")
	elif request.form['confirm-password'] != request.form['password']:
		flash('Passwords do not match!')
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True)