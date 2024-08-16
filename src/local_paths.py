import os
import pathlib
from logger import logger

##########


if os.environ["LEAGUE"] == "NBA":
    logger.debug("Loading NBA JSON map...")
    JSON = "nba.json"

elif os.environ["LEAGUE"] == "WNBA":
    logger.debug("Loading WNBA JSON map...")
    JSON = "wnba.json"

else:
    raise ValueError(f"Invalid LEAGUE env variable {os.environ['LEAGUE']}")


HERE = pathlib.Path(__file__).parents[0]
PARENT = pathlib.Path(HERE).parents[0]
PATH_TO_TEAMS = os.path.join(HERE, "teams", JSON)
