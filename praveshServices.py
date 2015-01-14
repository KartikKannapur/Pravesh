#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       JANUARY 12, 2015
#                       VERSION                 :                       1.0
#                       DESCRIPTION             :                       Services exposed as APIs for Pravesh functionality
#

from praveshSqlConnect import *

class pravesh:
	def __init__(self):
		try:
			print "[DEBUGGING]: Object iniitalized successfully."
		except:
			print "[DEBUGGING]: Object initalization Failed."
	
        #Create GDG Developer Profile:
        def createDeveloperProfile(self, fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology):

                # TODO: CREATE A DEVELOPER PROFILE BY ENTERING THE DETAILS IN DATABASE:

                # BY DEFAULT, RUNNING ON LOCALHOST, ELSE MENTION THE IP ADDRESS WHERE THE SERVER IS RUNNING
		o_praveshSqlConnect = praveshSqlConnect() 

                # PUSHING DEVELOPER  DETAILS TO DATABASE - FIRST TIME REGISTRATION:
                print "[TESTING]: Calling function from praveshSqlConnect to register new developer..."
                o_praveshSqlConnect.pushDeveloperDetails(fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology)

                # FREE THE OBJECT AND CLOSE THE CONNECTION
                o_praveshSqlConnect.free()

        # TODO: POST EVENT 
        # 1. UPDATE tbl_event --> WHO ALL ATTENDED THE EVENT
        # 2. UPDATE tbl_developerPoints --> ASSIGN POINTS TO DEVELOPER FOR AN EVENT (ON SOME TECHNOLOGY)
        # 3. UPDATE tbl_developer --> UPDATE event_id field (APPEND event_id to already existing event_id's)

	#TODO:  ------ PRE-EVENT TASKS ------:

	# CREATE NEW EVENT:
	def createEvent(self, name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points):
		print "Creating New Event..."
		o_praveshSqlConnect = praveshSqlConnect()
		
		# PUSH EVENT DETAILS TO DATABASE:
		o_praveshSqlConnect.createEvent(name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points)

		o_praveshSqlConnect.free()


	def updateEventDetails(self, event_id, name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points):
                o_praveshSqlConnect = praveshSqlConnect()

		# UPDATE ALREADY EXISTING EVENT INFORMATION:
                o_praveshSqlConnect.updateEventDetails(event_id, name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points)

                o_praveshSqlConnect.free()


	def signUpDeveloperForEvent(self, event_id, developer_emailId):
		# WE NEED TO ASSIGN SOME IDENTITY/QR CODE, ETC.. WHICH WILL BE SCANNED DURING THE EVENT
                o_praveshSqlConnect = praveshSqlConnect()

		# FIND IF THE DEVELOPER PROFILE ALREADY EXIST:
		isAlreadyExist = str(o_praveshSqlConnect.isDeveloperAlreadyExist(developer_emailId))

		# SOME INTEGER RETURNED:
		if isAlreadyExist:
			# DEVELOPER ALREADY REGISTERED, HENCE SIGN HIM UP FOR THE EVENT.
			print "Developer Exists with developer id: ..." + isAlreadyExist
			o_praveshSqlConnect.signUpDeveloperForEvent(event_id, isAlreadyExist)
		else:
			# DEVELOPER DOES NOT EXIST, REDIRECT HIM TO REGISTRATION PAGE.
			print "Developer doesn't exist!"

                o_praveshSqlConnect.free()


	# TODO: ------ DURING EVENT TASKS -------:
	def developerAttended():
                o_praveshSqlConnect = praveshSqlConnect()

		o_praveshSqlConnect.whoAttendedEvent()
                o_praveshSqlConnect.assignPoints()
		o_praveshSqlConnect.updateDeveloperProfile()

                o_praveshSqlConnect.free()





	# TODO: ------ POST EVENT TASKS ------:


	# TODO: SOME MORE SERVICES:
	# 1. FETCH ALL EVENTS
	# 2. FETCH EVENT DETAILS

	# FETCH ALL EVENTS (TO BE DISPAYED AS A LIST):
	def fetchAllEvents(self):
		o_praveshSqlConnect = praveshSqlConnect()
		
		# Fetch All Events:
		listOfEvents = o_praveshSqlConnect.fetchAllEvents()
	
		print "Printing List of Events..."
		for event in listOfEvents:
			print event[0]

		o_praveshSqlConnect.free()


	# FETCH EVENT DETAILS BASED ON event_id:
	def fetchEventDetails(self, event_id):
		o_praveshSqlConnect = praveshSqlConnect()

                # Fetch Event Details:
                eventDetails = o_praveshSqlConnect.fetchEventDetails(event_id)

		# Fetch Event details from Cursor:
		event = eventDetails.fetchone()
	
		# Printing individual Details:
                print "Printing Event Details..."
		print "Event Id: " + str(event_id)
		print "Event Name: " + event[1]
		print "Event Date: " + event[2]
		print "Event Type: " + event[4]

		# TODO: THESE DETAILS HAS TO BE LOADED TO RESPECTIVE PLACES IN FRONT END: 
		# KARTIK TO FOLLOW WITH ME

                o_praveshSqlConnect.free()




# TODO: 
# 1. LINK THE BELOW FUNCTIONALITY WITH FRON END (REGISTRATYION FORM) - THE BELOW CODE IS ONLY FOR TESTING 

# CREATE DEVELOPER PROFILE IN PRAVESH PORTAL:
#o_pravesh = pravesh()
#o_pravesh.createDeveloperProfile("Anuj", "Duggal", "er.anujduggal@gmail.com", "9980962767", "21/12/1988", "male", "Intel", "anujduggal88", "anujduggal21", "", "Polymer, Android")


# CREATE EVENT:
#o_pravesh = pravesh()
#o_pravesh.createEvent("TestName", "Test Date", "Test Venue", "Meetup", "Test Desc", "Android, Chrome", "Test Link", 2)


# FETCH LIST OF ALL EVENTS:
#o_pravesh = pravesh()
#o_pravesh.fetchAllEvents()


# FETCH EVENT DETAILS:
#o_pravesh = pravesh()
#o_pravesh.fetchEventDetails(6)

# SIGN UP DEVELOPER FOR AN EVENT:
#o_pravesh = pravesh()
#o_pravesh.signUpDeveloperForEvent(7, "er.anujduggal@gmail.com")
