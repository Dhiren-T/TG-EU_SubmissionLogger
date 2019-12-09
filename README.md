# ThreatGrid Submissions Remaining Logger

This script was designed to locally log the number of remaining submissions avaialble with ThreatGrid at the time of running attached to the user credntials provided at execution. The resulting CSV data saves Date, Time stamp & number of remaining submissions. CSV log files are seperated into monthly log files for trending analysis. 


## Use Case Description

The script was designed to assist in visualising useage thorugh a day, week, month basis to view submission perfrormance and capacity.

## Installation

The script has been coded to use the EU ThreatGrid API.  
Copy the .py file to a new working directory.

## Usage

Recommended execution of the script is via CRON:

   - Long term data logging on a 2-3 hour run interval
   - Verbose short term logging on a 30 minute run interval.
   *Be sure to run at a sensible interval*   

To execute with CLI argument:   
run the .py file passing CLI arguments username and apikey at execution:  

Syntax: 
EU_threatgrid_submission_logger.py <ThreatGrid UserName> <ThreatGrid User API Key>.

If script is run without CLI args,  prompts will be displayed on screen.
