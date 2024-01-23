# Warning 

This uses GitHub Actions, which may impose charges. (In my case it looks like it should always be well under my usage tier and "free").

I am not responsible for any charges that others incur through use/misuse. Be sure you review the billing/usage details that apply to you, set any budget limits, etc.: https://docs.github.com/en/billing/managing-billing-for-github-actions 

# Overview

When run this will:

1. Iterate through all assignments
2. If: a) the assignment has a Due Date set and b) it allows any form of `online` Canvas submission (submitted through Canvas, like a file submission or an online quiz), and c) the due date is within 24-hours of the script's start
   1. Check each student for a missing submission.
   2. Email a generic message to all students who haven't submitted anything.

# GitHub Actions

This repo includes a GitHub action to run the script daily.  It requires environment variables to get access to the Canvas instance and course.

**WARNING: This runs daily and will accrue minutes of cloud access.  Be sure to disable the action at the end of the semester!!!**  
* It may be best to only have one version of this on GitHub and update the `CANVAS_COURSE_ID` each semester (rather than create a new version each semester).
* Workflows (actions) can be disabled when not in use.  See https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow .  Disable the "send-alerts" workflow when not in use.

## Required Environment Variables

Add the three "secrets" described below.  Go to the GitHub repo's Settings, then select "Secrets and variables", then "Actions". Finally, do a "New repository secret" for each.

* `CANVAS_URL` : URL of the Canvas Instance, like SCHOOL.instructure.com
* `CANVAS_KEY`: API Key for Canvas. Created via the "+ New Access Token" button at http://CANVAS_URL/profile/settings .
* `CANVAS_COURSE_ID`: Canvas Course ID number (the number in the URL for a specific course)

## Scheduling

Update the .github/workflows/send-alerts.yml as needed.  The cron format specifies the time the script will run in UTC time.  The cron format is described at https://www.ibm.com/docs/en/db2oc?topic=task-unix-cron-format.  

20 7 would be 7:20am UTC time.  7:00 PM in St. Louis Missouri during standard time is 00 1. 
