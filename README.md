# ThreatGrid Remaining Submissions Logger

This script has been designed to locally log the number of remaining submissions avaialble with ThreatGrid at the time of running attached to the user credntials provided at execution. The resulting CSV data saves Date, Time stamp & number of remaining submissions. CSV log files are seperated into monthly log files for trending analysis.   You must have a valid login and API key for the Cisco Threatgrid Platform to use the code. 


## Use Case Description

Objective is to provide local logging & visability of the remaining api submissions from their licenced submission entlement during a day, week or monthly basis. Ideally used when deploying ESA, WSA and FMC ThreatGrid integrations.

## Installation

The script has been coded to use the EU ThreatGrid API.   Its easily modified to use the US system if needed.
  - Copy the .py file to a new working directory.
  - Ensure execute permissions are applied using CHMOD
  - Execute the EU_threatgrid_submission_logger.py as per Usage section.

## Usage

Recommended execution of the script is via CRON:

   - Long term data logging on a 2-3 hour run interval
   - Verbose short term logging on a 30 minute run interval.
   *Be sure to run at a sensible interval*   

To execute with CLI argument:   
  - run the .py file passing CLI arguments username and apikey at execution:  

Syntax: 
  - EU_threatgrid_submission_logger.py 'ThreatGrid UserName' 'ThreatGrid User API Key'

If script is run without CLI args,  prompts will be displayed on screen for username and TG API key.

## Script Output

  - Upon execution of the script a new file will be created in the working directory where the script was executed.
  - File name will be 'month'-'year'.csv (if the file already exists it will be appended with the result)
  - CSV column headings: System DATE | System Time | Number of remaining API Submission


[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/DT-dev1/TG-EU-SubmissionCountLog)
