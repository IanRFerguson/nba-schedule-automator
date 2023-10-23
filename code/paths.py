#!/bin/python3
import os
import pathlib

##########


here = pathlib.Path(__file__).parents[0]
parent = pathlib.Path(here).parents[0]

path_to_teams = os.path.join(here, "teams.json")
