import json
import os
from datetime import datetime, timedelta
from time import sleep
from typing import Optional

import pandas as pd
import pytz
from ics import Calendar, Event

from local_paths import PARENT, PATH_TO_TEAMS
from logger import logger

##########

COLUMNS_TO_WRITE = ["DATE", "START (ET)", "CALENDAR_EST", "CALENDAR_UTC", "OPPONENT"]


class NBASchedule:
    """
    This class scrapes the web for team_dataule data,
    wraps it in an ICS calendar object, and writes to your
    local machine
    """

    def __init__(self, team: str, year: Optional[int] = None):
        self.team_abbreviation = team

        if not year:
            self.year = (
                int(datetime.now(pytz.timezone("US/Eastern")).strftime("%Y")) + 1
            )
        else:
            self.year = year

        ###

        team_data = self.load_team_data()

        self.team_name = team_data["team_name"]
        self.url = team_data["url"].format(self.year)
        self.nickname = team_data["nickname"]

    def load_team_data(self):
        """
        Load local JSON file with team data
        """

        with open(PATH_TO_TEAMS) as incoming:
            try:
                temp = json.load(incoming)[self.team_abbreviation]
            except KeyError:
                raise KeyError(
                    f"Whoops! {self.team_abbreviation} is an invalid team abbreviation"
                )

        return temp

    def get_team_schedule(self, columns_to_write=COLUMNS_TO_WRITE) -> pd.DataFrame:
        """
        Scrapes basketball reference team_dataule
        """

        # Scrape HTML data from BasketballReference
        team_data = pd.read_html(self.url)[0]

        team_data = self.clean_team_data(team_data)

        team_data = team_data.loc[:, columns_to_write]

        return team_data

    def clean_team_data(self, team_data: pd.DataFrame) -> pd.DataFrame:
        """
        Performs several important preprocessing steps including:
        * Standardizing column names
        * Removing filler rows from the scraped data
        * Standardizing data types
        """

        def military_time(x):
            x = x.replace("p", " PM")

            time_in = datetime.strptime(x, "%I:%M %p")
            time_out = datetime.strftime(time_in, "%H:%M")

            return time_out

        def localize_est(x):
            return pytz.timezone("US/Eastern").localize(x)

        def localize_utc(x):
            return x.astimezone(pytz.utc)

        # Cast all column names to uppercase
        team_data.columns = [x.upper() for x in team_data.columns]

        # Remove fill rows
        team_data = team_data[team_data["DATE"] != "Date"].reset_index(drop=True)

        # Cast DATE column to datetime
        team_data["DATE"] = pd.to_datetime(team_data["DATE"])

        team_data["START (ET)"] = team_data["START (ET)"].apply(
            lambda x: military_time(x)
        )

        team_data["DATE"] = team_data["DATE"].astype(str)

        team_data["CALENDAR_EST"] = pd.to_datetime(
            team_data["DATE"] + " " + team_data["START (ET)"]
        )
        team_data["CALENDAR_EST"] = team_data["CALENDAR_EST"].apply(
            lambda x: localize_est(x)
        )

        team_data["CALENDAR_UTC"] = team_data["CALENDAR_EST"].apply(
            lambda x: localize_utc(x)
        )

        return team_data

    def write_team_schedule_to_ics(
        self, write_file: bool = True, return_file: bool = False, dev: bool = False
    ):
        """
        Reads in team team_dataule, push to ics Calendar object,
        and write locally as .ics file
        """

        def endtime(x):
            return x + timedelta(hours=2)

        team_schedule = self.get_team_schedule()

        if dev:
            team_schedule = team_schedule.iloc[:1]

        output_calendar = Calendar()
        logger.info(f"Writing the {self.nickname} schedule...")
        sleep(2.5)

        for ix, opponent in enumerate(team_schedule["OPPONENT"]):
            game = Event()

            game.name = f"{self.team_name} vs. {opponent}"
            game.begin = team_schedule["CALENDAR_UTC"][ix]
            game.end = endtime(game.begin)

            output_calendar.events.add(game)

            sleep(0.05)

        ###

        if write_file:
            output_filename = f"{self.nickname.upper()}_{self.year}_SCHEDULE.ics"
            output_filename = output_filename.replace(" ", "_")

            output_path = os.path.join(PARENT, output_filename)

            with open(output_path, "w") as outgoing:
                outgoing.writelines(output_calendar.serialize_iter())

        if return_file:
            return output_calendar
