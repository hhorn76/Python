#!/usr/bin/python

import xml.etree.ElementTree as ET

strXml = '\
<?xml version="1.0"?>\
<data>\
	<country name="Liechtenstein">\
		<rank>1</rank>\
		<year>2008</year>\
		<gdppc>141100</gdppc>\
		<neighbor name="Austria" direction="E"/>\
		<neighbor name="Switzerland" direction="W"/>\
	</country>\
	<country name="Singapore">\
		<rank>4</rank>\
		<year>2011</year>\
		<gdppc>59900</gdppc>\
		<neighbor name="Malaysia" direction="N"/>\
	</country>\
	<country name="Panama">\
		<rank>68</rank>\
		<year>2011</year>\
		<gdppc>13600</gdppc>\
		<neighbor name="Costa Rica" direction="W"/>\
		<neighbor name="Colombia" direction="E"/>\
	</country>\
#</data>'
#from file
#tree = ET.parse('country_data.xml')
#root = tree.getroot()

#from string
root = ET.fromstring(strXml)

#for child in root:
#	print (child.tag, child.attrib)
#	for subchild in child:
#		print (subchild.tag)
#		print (subchild.attrib)
#		print (subchild.text)

for child in root:
	print ('Tag: ' + child.tag)
	#print (child.attrib)
	print ('Attribute [name] ' + child.attrib['name'])
	for subchild in child:
		print ('Tag: ' + subchild.tag)
		if subchild.attrib:
			#print (subchild.attrib)
			print ('Attribute [direction]: ' + subchild.attrib['direction'])
			print ('Attribute [name]: ' + subchild.attrib['name'])
		if subchild.text:
			print ('Text: ' + subchild.text)