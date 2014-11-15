#!/usr/bin/env python

import requests
import argparse

# Establish the parser
parser = argparse.ArgumentParser()
# Require the -s/--site arg, as this will be the site/ip 
parser.add_argument("-s", "--site", help = "site to send request", required=True)
# Require -p/--port arg, as this will be used to set the port to connect to
parser.add_argument("-p", "--port", help = "server port to send request to", required=True)
parser.add_argument("--agent", help = "specify user agent")
parser.add_argument("--path", help = "set the url path. ex: store/b/")
parser.add_argument("--headers", help = "display headers", action = "store_true")
parser.add_argument("--header", help = "display one value from header")
args = parser.parse_args()

# Build full url with the path if the --path argument is used
if args.path:
    full = args.site + ":" + args.port+"/"+args.path
# If the --path arg isn't used, just default to site:port/
else:
    full = args.site + ":" + args.port+"/"


print "Going to: ",full
print "\n"

#Set user-agent parameters for requests
try:
    head = {'User-Agent': args.agent}
except:
    #If a user-agent isn't specified, then use a static one
    head = {'User-Agent': "python requestor v1 -- ninjasl0th"}

#Send the get request to the url. Allow redirects. This can always be changed
a = requests.get(full, allow_redirects=True, headers=head)

#Print the return code. ex: 200, 404, 500
print "Status: ", a.status_code

#Print the response headers from the server is --headers is used 
if args.headers:
    print a.headers

#Select which header value to to view. ex: server, location, etc...
if args.header:
    print a.headers[args.header]
    
print "\nYou Sent:\n",a.request.headers
    
