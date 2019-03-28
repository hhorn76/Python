#!/usr/bin/python
# Written by Heiko Horn 2019.03.28

import sqlite3, os, subprocess
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

# Get the current user
currentUser = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
currentUser = [currentUser,""][currentUser in [u"loginwindow", None, u""]]

# Set variables
db = '/Users/' + currentUser + '/Library/Application Support/Dock/desktoppicture.db'
key = 1
strImg = '/Library/Desktop Pictures/MIS-2018.jpg'

# Close System preferences, if open
subprocess.call('killall System\ Preferences > /dev/null 2>&1', shell=True)

# Check if databes exists and connect.
exists = os.path.isfile(db)
if exists:
	connection = sqlite3.connect(db)
	cursor = connection.cursor()
else:
	exit(1)
	
if cursor.connection == connection:
	# Delete all rows in the `data` and `preferences` tables.
	cursor.execute("DELETE FROM data;")
	cursor.execute("DELETE FROM preferences;")	
	# Insert a new row into the `data` and `preferences` tables.
	cursor.execute("INSERT INTO data(rowid,value) VALUES(?,?);",(1,strImg))
	cursor.execute("INSERT INTO preferences(rowid,key,data_id,picture_id) VALUES(1,1,1,3);")
	cursor.execute("INSERT INTO preferences(rowid,key,data_id,picture_id) VALUES(2,1,1,4);")
	cursor.execute("INSERT INTO preferences(rowid,key,data_id,picture_id) VALUES(3,1,1,2);")
	cursor.execute("INSERT INTO preferences(rowid,key,data_id,picture_id) VALUES(4,1,1,1);")
	connection.commit()
	#connection.close()
	subprocess.call('killall Dock', shell=True)
	print 'The Desktop image has been set to \'' + strImg + '\'.'

## Test to see the values that were set.
#cursor.execute("SELECT * FROM preferences;")
#print cursor.description
#print cursor.fetchall()
#cursor.execute("SELECT * FROM data;")
#print cursor.description
#print cursor.fetchall()

#Close the sqlite connection
if cursor.connection == connection:
	connection.close()