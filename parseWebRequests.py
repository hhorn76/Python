#!/usr/bin/python

# define a 
strApiUrl = 'http://ip.jsontest.com'

# get info of auth module using urllib2 module
import urllib2
request = urllib2.Request(strApiUrl)
#request.add_header('Authorization', 'Basic ' + base64Auth)
#request.add_header('Accept', 'application/xml')
result = urllib2.urlopen(request).read()
print result

# get info of auth module using requests module, available for macOS 10.13 and higer
import requests
result = requests.get(strApiUrl).content
print result

## get info of auth module using urllib3 module, available for macOS 10.14 and higer
import urllib3, certifi
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
result = http.request('GET', strApiUrl).data
print result
