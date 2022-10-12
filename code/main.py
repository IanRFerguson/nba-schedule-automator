#!/bin/python3
from assist import setup
from corner_three import NBA_Schedule


##########


def run():

    team, year = setup()

    nba = NBA_Schedule(
        team=team,
        year=year
    )

    nba.write_team_schedule()

    print(f"Schedule written!\n\nLET'S GO {nba.nickname.upper()}!")


##########


if __name__ == "__main__":
    run()