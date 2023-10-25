#!/bin/bash

read -p "Team Abbreviation (e.g., NYK):    " TEAM
echo " "
sleep 2;

#####

echo "Setting up virtual environment..."
sleep 2;

# Activate virtual environment
python3 -m venv ./virtual

# Work on virtual env
source ./virtual/bin/activate

# Upgrade pip
python3 -m pip -q install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Bonus depends
python3 -m pip install --upgrade setuptools && python3 -m pip -q install lxml

#####

python3 code/main.py --team $TEAM