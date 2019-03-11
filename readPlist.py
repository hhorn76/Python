#!/usr/bin/python

import plistlib

strPlist = '/Library/Preferences/com.jamfsoftware.jamf.plist'
strKey = 'jss_url'
strJamfUrl = plistlib.readPlist(strPlist)[strKey] + '/JSSResource'

print (strJamfUrl)