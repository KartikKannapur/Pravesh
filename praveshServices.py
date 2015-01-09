#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       JANUARY 9, 2015
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


	def signUpDeveloperForEvent():
		# WE NEED TO ASSIGN SOME IDENTITY/QR CODE, ETC.. WHICH WILL BE SCANNED DURING THE EVENT
                o_praveshSqlConnect = praveshSqlConnect()

                o_praveshSqlConnect.signUpDeveloperForEvent()

                o_praveshSqlConnect.free()


	# TODO: ------ DURING EVENT TASKS -------:
	def developerAttended():
                o_praveshSqlConnect = praveshSqlConnect()

		o_praveshSqlConnect.whoAttendedEvent()
                o_praveshSqlConnect.assignPoints()
		o_praveshSqlConnect.updateDeveloperProfile()

                o_praveshSqlConnect.free()





	# TODO: ------ POST EVENT TASKS ------:




# TODO: 
# 1. LINK THE BELOW FUNCTIONALITY WITH FRON END (REGISTRATYION FORM) - THE BELOW CODE IS ONLY FOR TESTING 

# CREATE AN OBJECT FOR THE CLASS: pravesh
#o_pravesh = pravesh()

# CREATING DEVELOPER PROFILE IN PRAVESH PORTAL:
#o_pravesh.createDeveloperProfile("Anuj", "Duggal", "er.anujduggal@gmail.com", "9980962767", "21/12/1988", "male", "Intel", "anujduggal88", "anujduggal21", "", "Polymer, Android")

o_pravesh = pravesh()
#o_pravesh.createEvent("TestName", "Test Date", "Test Venue", "Meetup", "Test Desc", "Android, Chrome", "Test Link", 2)

#o_pravesh.updateEventDetails()

