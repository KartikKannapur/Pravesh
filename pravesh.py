#
#						MODIFIED BY		:		ANUJ DUGGAL
#						DATE MODIFIED		:		JANUARY 13, 2015
#

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
  event_typeId = RadioField("EventType")
  event_description = TextAreaField("EventDescription")
  event_techId = CheckboxInput("EventTechId")
  event_GPLusLink = TextField("GooglePlusEventLink")
  #event_points = DropdownField("EventPoints")
  #event_dev_registered = TextField("EventDevRegistered")
  #event_dev_attended = TextField("EventDevAttended")
  
  
  submit = SubmitField("CreateEvent")

class SignUpEventForm(Form):
  signup_email = TextField("SingUpEmail")
  #signup_phone = TextField("SingUpPhone")

  submit = SubmitField("Attend")

class AttendeeEventForm(Form):
  signup_email = TextField("AttendeeEmail")
  #signup_phone = TextField("AttendeePhone")

  submit = SubmitField("Attend")

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
        event_type_var = request.form["event_typeId"]
        event_description_var = request.form["event_description"]
        event_techId_var = request.form.getlist("event_techId")
        event_GPLusLink_var = request.form["event_GPLusLink"]
        event_points_var = request.form["event_points"]
        #event_dev_registered_var = request.form["event_dev_registered"]
        #event_dev_attended_var = request.form["event_dev_attended"]
  
        #print event_name_var, event_date_var, event_venue_var, event_type_var, event_description_var, event_techId_var
        #print event_GPLusLink_var, event_points_var, event_dev_registered_var, event_dev_attended_var

	techid_var_str = ""
	for techid in event_techId_var:
		techid_var_str = techid_var_str + techid + ", "
		print techid
  
	# MODIFIED BY ANUJ:

	# TODO: CREATE NEW EVENT:
	o_pravesh = pravesh()
	o_pravesh.createEvent(event_name_var, event_date_var, event_venue_var, event_type_var, event_description_var, techid_var_str, event_GPLusLink_var, event_points_var)


  return render_template('event.html', form=form)

#Sign Up for an Event
@app.route('/signup/', methods=('GET', 'POST'))
def signUpEvent():
  form = SignUpEventForm()
  if request.method == 'POST':
        signup_email_var = request.form["signup_email"]
        #signup_phone_var = request.form["signup_phone"]        
  
        print signup_email_var

	# SIGNUP DEVELOPER FOR EVENT:
	o_pravesh = pravesh()

	# DEFAULT VALUE FOR EVENT_ID, NEEDS TO BE UPDATED - DISCUSS WITH KARTIK:
	event_id = int(11)
	o_pravesh.signUpDeveloperForEvent(event_id, str(signup_email_var))

  return render_template('signup.html', form=form)

#Return Event List
@app.route('/eventList/', methods=('GET', 'POST'))
def eventList():
  return render_template('eventList.html')

#Attendee Form
@app.route('/attendee/', methods=('GET', 'POST'))
def attendeeForm():
  form = AttendeeEventForm()
  if request.method == 'POST':
        attendee_email_var = request.form["attendee_email"]
        #attendee_phone_var = request.form["attendee_phone"]        
  
        print attendee_email_var

  return render_template('attendee.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()
