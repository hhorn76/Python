#!/usr/bin/python

import subprocess

sudoPassword = 'password\n'

def passSudoPassword(sudoPassword):
	p = subprocess.Popen(["sudo", "-S", "whoami"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print p.communicate(sudoPassword)
	
passSudoPassword(sudoPassword)