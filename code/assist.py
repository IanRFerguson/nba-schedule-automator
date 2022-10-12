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
        default=datetime.now(pytz.timezone("US/Eastern")).strftime("%Y"),
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



def setup() -> tuple:
    """
    Command line + validation wrapper
    """

    arguments = get_command_line_arguments()

    ###

    try:
        validate_user_input(arguments.team)
    except Exception as e:
        raise e

    ###

    return arguments.team, arguments.year