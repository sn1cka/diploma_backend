set -e
rm -f ./backend/db.sqlite3
./manage.py migrate
./manage.py loaddata users.json
./loadfakedata.sh