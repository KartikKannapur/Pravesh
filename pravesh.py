from flask import Flask
from flask import render_template
from flask import request, url_for
from wtforms import StringField, SubmitField
from wtforms import TextField, PasswordField, validators, HiddenField, Form
from wtforms import TextAreaField, BooleanField, RadioField, SelectMultipleField
from wtforms.widgets import CheckboxInput
from praveshServices import *


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

class CreateEventForm(Form):
  event_name = TextField("EventName")
  event_date = TextField("EventDate")
  event_venue = TextField("EventVenue")
  event_description = TextAreaField("EventDescription")
  event_techId = RadioField("EventTechId")
  event_GPLusLink = TextField("GooglePlusEventLink")
  event_points = TextField("EventPoints")
  event_dev_registered = TextField("EventDevRegistered")
  event_dev_attended = TextField("EventDevAttended")
  
  
  submit = SubmitField("CreateEvent")

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
	
        print firstName_var, lastName_var, email_var, phone_var, dob_var, sex_var, org_var
        print github_var, linkedin_var, gplus_var

	techid_var_str = ""
	for techid in techid_var:
		techid_var_str = techid_var_str + techid + ", "
		print techid

	print techid_var_str


	# MODIFED BY ANUJ:

	# TODO: REGISTER NEW DEVELOPER BY CALLING A SERVICE FROM praveshServices.py:

	# Register New Developer:
	o_pravesh = pravesh()
	o_pravesh.createDeveloperProfile(firstName_var, lastName_var, email_var, phone_var, dob_var, sex_var, org_var, github_var, linkedin_var, gplus_var, techid_var_str)



  return render_template('register.html', form=form)

#Create Event
@app.route('/event/', methods=('GET', 'POST'))
def createEvent():
  form = CreateEventForm()
  if request.method == 'POST':
        event_name_var = request.form["event_name"]
        event_date_var = request.form["event_date"]
        event_venue_var = request.form["event_venue"]
        event_description_var = request.form["event_description"]
        event_techId_var = request.form["event_techId"]
        event_GPLusLink_var = request.form["event_GPLusLink"]
        event_points_var = request.form["event_points"]
        event_dev_registered_var = request.form["event_dev_registered"]
        event_dev_attended_var = request.form["event_dev_attended"]
  
        print event_name_var, event_date_var, event_venue_var, event_description_var, event_techId_var
        print event_GPLusLink_var, event_points_var, event_dev_registered_var, event_dev_attended_var

  
  #ANUJ can add the services here.


  return render_template('event.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()
