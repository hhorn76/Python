#!/usr/bin/python

import os, pwd, grp

# get current username
currentUser = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
currentUser = [currentUser,""][currentUser in [u"loginwindow", None, u""]]

# get uid and gid from current user
uid = pwd.getpwnam(currentUser).pw_uid
gid = grp.getgrnam('staff').gr_gid

strFile = '/Users/' + currentUser '/Desktop/test.txt'

# change the user and group permission for the file
os.chown(strFile, uid, gid)