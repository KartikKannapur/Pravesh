from flask import Flask
from flask import render_template
from flask import request, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, RadioField, SelectMultipleField
from wtforms.widgets import CheckboxInput

app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'MyLongSampleSecretKey'

#app.secret_key = 'development key'

class RegistrationForm(Form):
  firstName = TextField("First Name")
  lastName = TextField("Last Name")
  email = TextField("Email")
  phone = TextField("Phone")
  dob = TextField("Date of Birth")
  sex = RadioField("Male","Female")
  org = TextField("Organization")
  github = TextField("GitHub Username")
  linkedin = TextField("LinkedIn ")
  gplus = TextField("Google Plus Username")
  techid = CheckboxInput("Interested Technology")
  
  submit = SubmitField("Send")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/register/', methods=('GET', 'POST'))
def register():
	form = RegistrationForm()

	return render_template('register.html', form=form)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()