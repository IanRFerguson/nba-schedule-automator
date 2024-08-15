from utilities import setup
from nba_schedule import NBASchedule

##########


def run():
    team, year = setup()

    nba = NBASchedule(team=team, year=year)

    nba.write_team_schedule_to_ics()

    print(f"Schedule written!\n\nLET'S GO {nba.nickname.upper()}!")


#####


if __name__ == "__main__":
    run()
