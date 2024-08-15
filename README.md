# NBA SCHEDULE AUTOMATOR
 This program automatically generates a .ics calendar file for your favorite team

## Requirements

* You need Docker installed on your machine, but that's about it!
* Fill out the `team.env` file with the abbreviations for your favorite team
  * See all the accepted values in `src/teams.json`

## Usage Notes

* Fill out the `team.env` file 
* Run `make schedule` at the command line - this will spin up a local Docker image and run the source code to generate a calendar file
* The resulting `.ics` file can be double-clicked and populated in any popular Calendar client (Apple Calendar, GCalendar, etc.)
