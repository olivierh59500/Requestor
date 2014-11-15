Requestor
=========

Python tool to make and reiew http requests using argparse.

I was teaching some friends some argparse things, and they wondered how to use python's requests lib.

After a bit, I made them this as a quick example of both. I'll keep modifying it and whatnot :D

Example:
./req.py -s http://google.com -p 80 --agent lol

usage: req.py [-h] -s SITE [-p PORT] [--agent AGENT] [--path PATH] [--headers]
              [--header HEADER]

optional arguments:

  -h, --help            show this help message and exit
  
  -s SITE, --site SITE  site to send request
  
  -p PORT, --port PORT  server port to send request to
  
  --agent AGENT         specify user agent
  
  --path PATH           set the url path. ex: store/b/
  
  --headers             display headers
  
  --header HEADER       display one value from header
  
