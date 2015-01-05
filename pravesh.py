from flask import Flask
from flask import render_template
from flask import request, url_for
from wtforms import StringField, SubmitField
from wtforms import TextField, PasswordField, validators, HiddenField, Form
from wtforms import TextAreaField, BooleanField, RadioField, SelectMultipleField
from wtforms.widgets import CheckboxInput

app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'MyLongSampleSecretKey'

#app.secret_key = 'development key'

class RegistrationForm(Form):
  firstName = TextField("FirstName")
  lastName = TextField("LastName")
  email = TextField("email")
  phone = TextField("Phone")
  dob = TextField("DateofBirth")
  sex = RadioField("Sex")
  org = TextField("Organization")
  github = TextField("GitHubUsername")
  linkedin = TextField("LinkedIn ")
  gplus = TextField("GooglePlusUsername")
  techid = CheckboxInput("InterestedTechnology")
  
  submit = SubmitField("Submit")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/register/', methods=('GET', 'POST'))
def register():
  form = RegistrationForm()
  if request.method == 'POST':
        firstName_var = request.form['firstName']
        lastName_var = request.form['lastName']
        email_var = request.form['email']
        phone_var = request.form['phone']
        dob_var = request.form['dob']
        sex_var = request.form['sex_mf']
        org_var = request.form['org']
        github_var = request.form['github']
        linkedin_var = request.form['linkedin']
        gplus_var = request.form['gplus']
        techid_var = request.form.getlist('techid')
	
        print firstName_var, lastName_var, sex_var
	for techid in techid_var:
		print techid

  return render_template('register.html', form=form)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()
