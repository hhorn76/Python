#!/usr/bin/python
# written by Heiko 11.02.2019

import base64, subprocess

strPassword='8yaThaDCTGHxG8fu'

##########################################################
print ('Password: ' + strPassword)
print ('')

##########################################################
## Using base64
## Function to encrypt password
def encryptPw (strPassword):
	return base64.b64encode(strPassword)

# Function to decrypt password
def decryprPw (strPassword):
	return base64.b64decode(strPassword)

strEncrypted = encryptPw (strPassword)
print ('Base64 encrypted password: ' + strEncrypted)

strDecrypted = decryprPw (strEncrypted)
print ('Base64 decrypted password: ' + strDecrypted)
print ('')

##########################################################
## Using openssl
# Function to encrypt password
def encryptPwOpenSSL(inputString):
	salt = subprocess.check_output(['/usr/bin/openssl', 'rand', '-hex', '8']).rstrip()
	passphrase = subprocess.check_output(['/usr/bin/openssl', 'rand', '-hex', '12']).rstrip()
	p = subprocess.Popen(['/usr/bin/openssl', 'enc', '-aes256', '-a', '-A', '-S', salt, '-k', passphrase], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	encrypted = p.communicate(inputString)[0]
	return encrypted, salt, passphrase
	print("Encrypted String: %s" % encrypted)
	
# Function to decrypt password
def decryptPwOpenSSL(inputString, salt, passphrase):
	p = subprocess.Popen(['/usr/bin/openssl', 'enc', '-aes256', '-d', '-a', '-A', '-S', salt, '-k', passphrase], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	return p.communicate(inputString)[0]
	
arrEncrypt = encryptPwOpenSSL(strPassword)
print('OpenSSL encrypted password: ' + arrEncrypt[0])
print('Salt: %s | Passphrase: %s' % (arrEncrypt[1], arrEncrypt[2]))

strDecypted = decryptPwOpenSSL(arrEncrypt[0], arrEncrypt[1], arrEncrypt[2])
print('OpenSSL encrypted password: ' + strDecypted)