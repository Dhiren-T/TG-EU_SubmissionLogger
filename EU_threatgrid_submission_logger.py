import csv
import json
from urllib import urlopen
import time
import sys

__copyright__ = "author - Dhiren Tailor - tailor.dhiren@gmail.com"

# Always use command line arguemnts for UserID, API key and Region Domain.  Designed to work with version 3 of the TG api.

try:
    user = str(sys.argv[1])
    apikey = str(sys.argv[2])
    region = str(sys.argv[3])
except IndexError as e:
    user = raw_input("Please enter your ThreatGrid UserID \n")
    apikey = raw_input("Please enter your ThreatGrid ApiKey \n")
    region = raw_input("Please enter EU|COM for the threatgrid system being used \n")

if user == "" or apikey == "" or region=="":
    exit()
else:
    fn = "%s.csv" % (time.strftime("%m-%Y")) 

    raw = urlopen('https://panacea.threatgrid.%s/api/v3/users/%s/rate-limit?apikey=%s' % (region, user, apikey) ).read()
    js = json.loads(raw)
    subs = js["data"]["organization"]["submissions-available"]

    fields=[time.strftime("%d/%m/%Y"),time.strftime("%H:%M:%S"),subs]
    with open(fn, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

