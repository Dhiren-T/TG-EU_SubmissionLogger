# TG-EU-SubmissionCountLog
Logs the number of remaining submissions in TG at the Org Level at the time of running.  Save data to monthly separated log files for submission trending. 

# Options:
Run with args username and apikey from command line
Run wihtout args,  user will be prompted for credentials

Example Usage:  EU_threatgrid_submission_logger.py <userid> <Apikey>

On execution a file named:  <month>/<year>.csv is created in the working directory;  logs the number of samples left from TG org level at the time of running.

Deployment:
Run via Cron at an interval of every 30 minutes or 1 hour (user preference. no need to set any lower).  Data files are generated in working directory and seperated into monthly files.

Currently set for the EU system.  Feel free to add additional useful info to the log as needed.
