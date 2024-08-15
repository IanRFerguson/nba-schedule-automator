import os
import pathlib

##########

HERE = pathlib.Path(__file__).parents[0]
PARENT = pathlib.Path(HERE).parents[0]
PATH_TO_TEAMS = os.path.join(HERE, "teams.json")
