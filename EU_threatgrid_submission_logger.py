import csv
import json
from urllib import urlopen
import time
import sys

__copyright__ = "author - Dhiren Tailor - tailor.dhiren@gmail.com"

# Always use command line arguemnts for UserID &  API key.  Designed to work with version 3 of the TG api.

try:
    user = str(sys.argv[1])
    apikey = str(sys.argv[2])
except IndexError as e:
    user = raw_input("Please enter your ThreatGrid UserID \n")
    apikey = raw_input("Please enter your ThreatGrid ApiKey \n")

if user == "" or apikey == "":
    exit()
else:
    fn = "%s.csv" % (time.strftime("%m-%Y")) 

    raw = urlopen('https://panacea.threatgrid.eu/api/v3/users/%s/rate-limit?apikey=%s' % (user, apikey) ).read()
    js = json.loads(raw)
    subs = js["data"]["organization"]["submissions-available"]

    fields=[time.strftime("%d/%m/%Y"),time.strftime("%H:%M:%S"),subs]
    with open(fn, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

