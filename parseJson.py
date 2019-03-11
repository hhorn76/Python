#!/usr/bin/python

import json

strJson  = '\
{\
	"id": 1,\
	"name": "Foo",\
	"price": 123,\
	"tags": [\
		"Bar",\
		"Eek"\
	],\
	"stock": {\
		"warehouse": 300,\
		"retail": 20\
	}\
}'

objJson=json.loads(strJson)

#print the json objects with keys and values
print objJson
print ('')

# print the values of each key
print objJson['stock']
print objJson['price']
print objJson['tags']
print objJson['id']
print objJson['name']
print ('')

# print each key in the string with its value
for item in objJson:
	print ('Key: ' + item)
	print ('Value: ' + str(objJson[item]))
	print (type(objJson[item]))
	if isinstance(objJson[item], dict) or isinstance(objJson[item], list):
		for subItem in objJson[item]:
			print ('Value: ' + subItem)
	print ('')
print ('')

# pretty print Json string
print json.dumps(objJson, sort_keys=True, indent=4, separators=(',', ': '))