
# Create venv and install dependencies.
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Export relevant environment vars.
export FLASK_APP=./de_identification/app.py
export ZIP_CODE_TO_POPULATION_CSV=./population_by_zcta_2010.csv

# Start app.
flask run
