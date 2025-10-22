# NBA SCHEDULE AUTOMATOR
 This program automatically generates a calendar for your favorite NBA team's schedule.

## Usage Notes

The only software you need running locally is the Docker daemon - this source code will do the rest.

* Update the environment values hardcoded in the [Docker compose file](./docker-compose.yml)
  
```bash
environment:
  - TEAM_ABBREVIATION=NYK
  - LEAGUE_YEAR=2026
```

* Run `make schedule` at the command line - this will spin up a local Docker image and run the source code to generate a calendar file
* The resulting `.ics` file can be double-clicked and populated in any popular Calendar client (Apple Calendar, GCalendar, etc.)
