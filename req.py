#!/usr/bin/env python

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--site", help = "site to send request", required=True)
parser.add_argument("-p", "--port", help = "server port to send request to", required=True)
parser.add_argument("--agent", help = "specify user agent")
parser.add_argument("--path", help = "set the url path. ex: store/b/")
parser.add_argument("--headers", help = "display headers", action = "store_true")
parser.add_argument("--header", help = "display one value from header")
args = parser.parse_args()

if args.path:
    full = args.site + ":" + args.port+"/"+args.path
else:
    full = args.site + ":" + args.port+"/"


print "Going to: ",full
print "\n"
try:
    head = {'User-Agent': args.agent}
except:
    head = {'User-Agent': "python requestor v1 -- ninjasl0th"}

a = requests.get(full, allow_redirects=True, headers=head)

print "Status: ", a.status_code

if args.headers:
    print a.headers
if args.header:
    print a.headers[args.header]
    
print "\nYou Sent:\n",a.request.headers
    
