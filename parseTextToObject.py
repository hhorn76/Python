#!/usr/bin/python

strList = """\
0,test0,TEST0
1,test1,TEST1
2,test2,TEST2
3,test3,TEST3
4,test4,TEST4
5,test5,TEST5
"""

# create a python class objects for the child nodes 
class objChild:
	def __init__(self, id=None, name=None, description=None):
		self.id = id
		self.name = name
		self.description = description

# create a list of python child class objects
listArray = []
for lines in strList.splitlines():
		arrline = lines.split(',')
		listArray.append(objChild(arrline[0], arrline[1], arrline[1]))
		
for item in listArray:
	print ('ID: ' + item.id)
	print ('Name: ' + item.name)
	print ('Description: ' + item.description + '\n')