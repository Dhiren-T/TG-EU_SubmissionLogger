# ThreatGrid Remaining Submissions Logger

This script has been designed to locally log the number of remaining submissions available with ThreatGrid at the time of running attached to the user credentials provided at execution. The resulting CSV data saves Date, Time stamp & number of remaining submissions. CSV log files are seperated into monthly log files for trending analysis.   You must have a valid login and API key for the Cisco Threatgrid Platform to use the code. 

## Use Case Description

Objective is to provide local logging & visibility of the remaining api submissions from their licensed submission entlement during a day, week or monthly basis. Ideally used when deploying ESA, WSA and FMC ThreatGrid integrations.

## Cisco ThreatGrid Credentals

* Login to the portal and click "My Account" from the top Right of the GUI
* Retrieve your API key

## Installation

The script has been coded to use the EU ThreatGrid API.

- Copy the .py file to a new working directory.
- Ensure execute permissions are applied using CHMOD
- Execute the EU_threatgrid_submission_logger.py as per Usage section.

## Usage

Recommended execution of the script is via CRON:

- Long term data logging on a 2-3 hour run interval
- Verbose short term logging on a 30 minute run interval.
- Be sure to run at a sensible interval  

To execute with CLI argument:   
- run the .py file passing CLI arguments username and apikey at execution:  

Syntax: 
- EU_threatgrid_submission_logger.py 'ThreatGrid UserName' 'ThreatGrid User API Key'

If script is run without CLI args,  prompts will be displayed on screen for username and TG API key.

## Script Output

- Upon execution of the script a new file will be created in the working directory where the script was executed.
- File name: 'month'-'year'.csv (if the file already exists it will be appended with the result)
- CSV column headings: System DATE | System Time | Number of remaining API Submission

## Example

````
DEMO>pwd
/home/demo

DEMO>ls
EU_threatgrid_submission_logger_v1.1.py

DEMO>python EU_threatgrid_submission_logger_v1.1.py <username> <Api Key>

DEMO>ls
12-2019.csv  EU_threatgrid_submission_logger_v1.1.py

DEMO>cat 12-2019.csv
10/12/2019,11:58:16,100

````

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/DT-dev1/TG-EU-SubmissionCountLog)
