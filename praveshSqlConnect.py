#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       JANUARY 14, 2015
#                       VERSION                 :                       1.0
#                       DESCRIPTION             :                       DATABASE CONNECTION, SQL QUERIES
#


import MySQLdb as mdb
import sys
import time, os

class praveshSqlConnect:
    def __init__(self, host='localhost'):
        try:
            self.conn = mdb.connect(host, 'root', 'root123', 'pravesh_web')
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT VERSION()")
            ver = self.cur.fetchone()
	    print "[DEBUGGING]: Pravesh Sql Connection Initialized successfully."
        except mdb.Error, e:
	    print "[DEBUGGING]: Sql Connection failed."
            sys.exit(1)

    def free(self):
        if self.conn:
            self.conn.close()

    # SIGNUP DEVELOPER FOR THE FIRST TIME:
    def pushDeveloperDetails(self, fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology):

	# PUSHING POINTS = 0 FOR THE DEVELOEPR REGISTERING FIRST TIME:
	total_points = int(0)

	self.cur.execute("INSERT INTO tbl_developer(firstname, lastname, email, phone, dateOfBirth, sex, organization, github_link, linkedin_link, googlePlus_link, technology_id, total_points) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology, total_points))

	self.conn.commit()

    # CREATE A NEW EVENT:
    def createEvent(self, name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points):

	print "[TESTING]: CREATING NEW EVENT..."
	self.cur.execute("INSERT INTO tbl_event(name, event_date, venue, type, description, technology_id, googlePlusLink, event_points) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);", (name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points))

	self.conn.commit()
	print "[TESTING]: NEW EVENT CREATED SUCCESSFULLY!"

    # UPDATE ALREADY EXISTING EVENT DETAILS (EXCEPT WHO ALL ATTENDED):
    def updateEventDetails(self, event_id, name, event_date, venue, event_type, description, technology_id, googlePlus_link, event_points):

	print "[TESTING]: UPDATING ALREADY EXISTING EVENT..."
	self.cur.execute("UPDATE tbl_event SET venue=%s, description=%s, technology_id=%s, event_points=%s WHERE id=%s", (name, event_id))

	self.conn.commit()
	print "[TESTING]: EVENT UPDATED SUCCESSFULLY!"


    # FIND IF THE DEVELOPER PROFILE ALREADY EXIST IN PRAVESH PORTAL:
    def getDeveloperId(self, emailId):
	print "[TESTING]: CHECKING IF DEVELOPER PROFILE ALREADY EXIST..."
	print "Email Id: " + str(emailId)
	self.cur.execute("SELECT id FROM tbl_developer WHERE email=%s;", (emailId))
	dev_id = str(self.cur.fetchone()[0])
	print "The id for the abobe Email-Id is: " + dev_id
	# RETURNING DEVELOPER ID:
	return int(dev_id)



    # SIGNUP THE REGISTERED DEVELOPER FOR AN EVENT: UPDATE dev_registered field of tbl_event:
    def signUpDeveloperForEvent(self, event_id, developerId):
	print "[TESTING]: Signing Up Developer for Event..."

	# GET THE LIST OF DEVELOPERS ALREADY REGISTERED FOR THIE EVENT AND APPEND NEW DEVELOPER ID:
	self.cur.execute("SELECT dev_registered FROM tbl_event WHERE id=%s;", (event_id))
	developerIDs = str(self.cur.fetchone()[0])

	print "Developer Ids already registered are:  " + developerIDs

	if (developerIDs):
		print "Some developers were already registered earlier for this event."
		developerIDs = str(developerIDs) + ", " + str(developerId)
	else:
		print "No developer is registerd for this event."
		developerIDs = str(developerId)

	print "Updated Developers Ids are: " + developerIDs

	# UPDATE tbl_event WITH dev_registered:
	self.cur.execute("UPDATE tbl_event SET dev_registered=%s WHERE id=%s;", (developerIDs, event_id))

	self.conn.commit()
	print "[TESTING]: Updated Developer Registered for the event successfully!"

    # ------------------------------DURING EVENT SQL CALLS------------------------------------:
    def whoAttendedEvent():
	print "Test"

    # GET EVENT POINTS:
    def getEventPoints(self, event_Id):
	print "[TESTING]: Fetching Event Points..."
	self.cur.execute("SELECT event_points FROM tbl_event WHERE id=%s;", (event_Id))

	event_points = int(self.cur.fetchone()[0])
	
	print "Event Points are: " + str(event_points)

	# RETURNING EVENT POINTS:
	return event_points


    # GET TECHNOLOGY LIST OF EVENT:
    def getTechnologyListOfEvent(self, event_Id):
	print "[TESTING]: FECTHING LIST OF TECHNOLOGIES USED.."
	self.cur.execute("SELECT technology_id FROM tbl_event WHERE id=%s;", (event_Id))

	# RETURNING LIST OF TECHNOLOGIES FOR THIS EVENT:
	technologies = str(self.cur.fetchone()[0])

	print "Technologies in the Event are: " + technologies
	
	return technologies


    # UPDATE tbl_event WITH DEVELOPERS WHO ATTEND THE EVENT:
    def setDeveloperAttendance(self, event_Id, developerId):
	print "[TESTING]: Setting Developer Attendance..."
	
	self.cur.execute("SELECT dev_attended FROM tbl_event WHERE id=%s;", (event_Id))
	dev_attended = str(self.cur.fetchone()[0])

	print "List of developers already attending: " + dev_attended

	dev_attended = dev_attended + ", " + str(developerId)

	print "List of Developers already attending now: " + dev_attended	

	self.cur.execute("UPDATE tbl_event SET dev_attended=%s WHERE id=%s;", (dev_attended, event_Id))
	self.conn.commit()


    # UPDATE DEVELOPER PROFILE WITH THE EVENT ID HE ATTENDS:
    def setDeveloperProfile(self, event_Id, developerId):
	print "[TESTING]: Updating Developer Profile..."
	self.cur.execute("SELECT event_id FROM tbl_developer WHERE id=%s;", (developerId))

	event_attended = str(self.cur.fetchone()[0])
	
	print "List of events attended so far: " + event_attended
	event_attended = event_attended + ", " + str(event_Id)
	print "List of Events attended now: " + event_attended

	self.cur.execute("UPDATE tbl_developer SET event_id=%s WHERE id=%s", (event_attended, developerId))
	self.conn.commit()

    # UPDATE tbl_developer WITH EVENT POINTS:
    def setDeveloperPoints(self, developerId, event_points):
	print "[TESTING]: Updating tbl_Developer..."
	
	# GET TOTAL POINTS DEVELOPER HAS:
	self.cur.execute("SELECT total_points FROM tbl_developer WHERE id=%s;", (developerId))
	total_points = int(self.cur.fetchone()[0])

	print "Developer has total points: " + str(total_points)
	updated_total_points = total_points + event_points
	print "Updated Points: " + str(updated_total_points)

	# UPDTAE QUERY:
	self.cur.execute("UPDATE tbl_developer SET total_points=%s WHERE id=%s;", (updated_total_points, developerId))
	self.conn.commit()

    def assignPoints(self, developer_emailId, points):
	print "Test"

    # UPDATE DEVELOPER PROFILE WITH EVENTS HE HAS ATTENDED: UPDATE event_id field in tbl_developer:
    def updateDeveloperProfile():
	print "Test"


    # SOME MORE SQL QUERIES:
    
    # FETCH THE LIST OF EVENTS:
    def fetchAllEvents(self):
	print "[TESTING]: Fetching list of events..."
	self.cur.execute("SELECT name FROM tbl_event;")
	return self.cur.fetchall()

    # FETCH EVENT DETAILS BASED ON event_id:
    def fetchEventDetails(self, event_id):
	print "[TESTING]: Fetching Event Details based on event_id..."
	self.cur.execute("SELECT * FROM tbl_event WHERE id=%s;", (event_id))
	return self.cur.fetchone()
