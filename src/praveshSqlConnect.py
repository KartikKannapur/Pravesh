#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       DECEMMBER 31, 2014
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

    def pushDeveloperDetails(self, fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology):
	print "[TESTING]: Pushing Developer Details to Database..."
	self.cur.execute("INSERT INTO tbl_developer(firstname, lastname, email, phone, dateOfBirth, sex, organization, github_link, linkedin_link, googlePlus_link, technology_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (fname, lname, email, phone, dob, sex, organization, github, linkedin, googleplus, technology))
	self.conn.commit()
	print "[TESTING]: Pushed the details."


