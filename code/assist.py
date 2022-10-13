#!/bin/python3
import argparse
from datetime import datetime
import pytz
import json
from paths import *


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
        help="Three-letter abbreviation (e.g., NYK, GSW)"
    )

    ###

    parser.add_argument(
        "--year",
        type=int,
        required=False,
        default=None,
        help="Year that season will end ... 2022-2023, input 2023"
    )

    return parser.parse_args()



def validate_user_input(user_input: str) -> bool:
    """
    Ensures that user has supplied valid team initials

    Parameters
        user_input: String abbreviation of team name (e.g., NYK, GSW)
    """

    with open(path_to_teams) as incoming:
        all_abbreviations = list(json.load(incoming).keys())

    if user_input not in all_abbreviations:
        raise ValueError(f"{user_input} invalid team abbreviation")

    return True



def double_check_year(user_input: int) -> int:
    """
    We need to make sure that NO year argument will
    still produce the relevant schedule ... i.e., I am writing
    this in the year 2022 (current year) but I want to see the 2022-2023
    schedule

    Parameters
        user_input: Integer representation of the year
    """

    right_now = datetime.now(pytz.utc)

    current_month = int(right_now.strftime("%m"))

    if current_month >= 6:
        return int(right_now.strftime("%Y")) + 1

    else:
        return int(right_now.strftime("%Y"))



def setup() -> tuple:
    """
    Command line + validation wrapper
    """

    arguments = get_command_line_arguments()

    team_ = arguments.team
    year_ = arguments.year

    ###

    try:
        validate_user_input(team_)
    except Exception as e:
        raise e

    ###

    if year_ is None:
        year_ = double_check_year(year_)
        
    ###

    return team_, year_