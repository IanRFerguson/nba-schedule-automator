from logger import logger
from nba_schedule import NBASchedule
from utilities import setup

##########


def run():
    team, year = setup()

    nba = NBASchedule(team=team, year=year)

    nba.write_team_schedule_to_ics()

    logger.info("Schedule written!")
    logger.info(f"LET'S GO {nba.nickname.upper()}!")


#####


if __name__ == "__main__":
    run()
