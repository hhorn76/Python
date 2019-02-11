#!/usr/bin/python
# written by Heiko 11.02.2019

import subprocess

sudoPassword = 'password\n'

def passSudoPassword(sudoPassword):
	p = subprocess.Popen(["sudo", "-S", "whoami"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print p.communicate(sudoPassword)
	
passSudoPassword(sudoPassword)