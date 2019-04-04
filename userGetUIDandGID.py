#!/usr/bin/python

import pwd, grp
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

currentUser = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
currentUser = [currentUser,""][currentUser in [u"loginwindow", None, u""]]

uid = pwd.getpwnam(currentUser).pw_uid
gid = grp.getgrnam('staff').gr_gid

print ('Username: ' + currentUser)
print ('UID: ' + str (uid))
print ('Group: ' + 'staff')
print ('GID: ' + str (gid))