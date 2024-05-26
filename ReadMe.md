
# Activate Env
source .venv/bin/activate

# Install Requirements
pip install -r requirements.txt

# Make Migrations
python3 manage.py makemigrations

# Migrate
python3 manage.py migrate
