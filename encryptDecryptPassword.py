#!/usr/bin/python

import base64

strPassword='8yaThaDCTGHxG8fu'

## Function to encrypt password
def encryptPw (strPassword):
	return base64.b64encode(strPassword)

# Function to encrypt password
def decryprPw (strPassword):
	return base64.b64decode(strPassword)

myEncryptedPassword = encryptPw (strPassword)
print ('My Encrypted Password is: ' + myEncryptedPassword)

myDecryptedPassword = decryprPw (myEncryptedPassword)
print ('My Decrypted Password is: ' + myDecryptedPassword)