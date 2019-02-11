#!/usr/bin/python
# written by Heiko 11.02.2019

from SystemConfiguration import SCDynamicStoreCopyConsoleUser

def getCurrentUserSysConfig ():
	currentUser = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
	currentUser = [currentUser,""][currentUser in [u"loginwindow", None, u""]]
	print('Current user: '+currentUser)

################################################################

import getpass
def getCurrentUserGetpass ():
	currentUser = getpass.getuser()
	print('Current user: '+currentUser)
	
getCurrentUserSysConfig ()
getCurrentUserGetpass ()