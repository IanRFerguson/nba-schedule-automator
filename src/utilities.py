import argparse
import json
import os
from datetime import datetime

import pytz

from local_paths import PATH_TO_TEAMS
from logger import logger

##########


def get_command_line_arguments():
    """
    Reads in user-supplied command line arguments
    """

    parser = argparse.ArgumentParser()

    ###

    parser.add_argument(
        "--team",
        type=str,
        required=True,
        help="Three-letter abbreviation (e.g., NYK, GSW)",
    )

    ###

    parser.add_argument(
        "--year",
        type=int,
        required=False,
        default=None,
        help="Year that season will end ... 2022-2023, input 2023",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        required=False,
        default=False,
        help="Activate debugger",
    )

    return parser.parse_args()


def validate_user_input(user_input: str) -> bool:
    """
    Ensures that user has supplied valid team initials

    Parameters
        user_input: String abbreviation of team name (e.g., NYK, GSW)
    """

    with open(PATH_TO_TEAMS) as incoming:
        all_abbreviations = list(json.load(incoming).keys())

    if user_input not in all_abbreviations:
        raise ValueError(f"{user_input} invalid team abbreviation")


def infer_league_year() -> int:
    """
    We need to make sure that NO year argument will
    still produce the relevant schedule ... i.e., I am writing
    this in the year 2022 (current year) but I want to see the 2022-2023
    schedule
    """

    right_now = datetime.now(pytz.utc)

    current_month = int(right_now.strftime("%m"))

    # NOTE - This is when the season ends
    if current_month >= 6:
        return int(right_now.strftime("%Y")) + 1

    return int(right_now.strftime("%Y"))


def setup() -> tuple:
    """
    Command line + validation wrapper
    """

    arguments = get_command_line_arguments()

    team_ = arguments.team
    year_ = arguments.year

    if arguments.debug:
        logger.setLevel(level=10)
        logger.debug("** Debugger active **")

    validate_user_input(team_)

    if not year_:
        year_environ = os.environ.get("LEAGUE_YEAR")

        if year_environ:
            year_ = year_environ
        else:
            year_ = infer_league_year()

    return team_, year_
