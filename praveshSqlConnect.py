#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       JANUARY 12, 2015
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

	self.cur.execute("INSERT INTO tbl_developer(firstname, lastname, email, phone, dateOfBirth, sex, organization, github_link, linkedin_link, googlePlus_link, technology_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology))

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
    def isDeveloperAlreadyExist(self, emailId):
	print "[TESTING]: CHECKING IF DEVELOPER PROFILE ALREADY EXIST..."
	self.cur.execute("SELECT id FROM tbl_developer WHERE email=%s;", (emailId))

	# RETURNING DEVELOPER ID:
	return self.cur.fetchone()[0]



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

    def assignPoints():
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
	return self.cur
