#
#                       AUTHOR                  :                       ANUJ DUGGAL
#                       DATE CREATED            :                       DECEMBER 31, 2014
#                       DATE MODIFIED           :                       DECEMBER 31, 2014
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

# TODO: 
# 1. LINK THE BELOW FUNCTIONALITY WITH FRON END (REGISTRATYION FORM) - THE BELOW CODE IS ONLY FOR TESTING 

# CREATE AN OBJECT FOR THE CLASS: pravesh
o_pravesh = pravesh()

# CREATING DEVELOPER PROFILE IN PRAVESH PORTAL:
o_pravesh.createDeveloperProfile("Anuj", "Duggal", "er.anujduggal@gmail.com", "9980962767", "21/12/1988", "male", "Intel", "anujduggal88", "anujduggal21", "", "Polymer, Android")
