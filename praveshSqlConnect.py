#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       JANUARY 9, 2015
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

    # SIGNUP THE REGISTERED DEVELOPER FOR AN EVENT: UPDATE dev_registered field of tbl_event:
    def signUpDeveloperForEvent():
	print "Test"



    # ------------------------------DURING EVENT SQL CALLS------------------------------------:
    def whoAttendedEvent():
	print "Test"

    def assignPoints():
	print "Test"

    # UPDATE DEVELOPER PROFILE WITH EVENTS HE HAS ATTENDED: UPDATE event_id field in tbl_developer:
    def updateDeveloperProfile():
	print "Test"

