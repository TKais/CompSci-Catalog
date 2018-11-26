apt-get -qqy update
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
apt-get -qqy install python-sqlalchemy
apt-get -qqy install python-pip
pip3 install --upgrade pip
pip3 install werkzeug --user
pip3 install flask --user
pip3 install Flask-Login==0.1.3 --user
pip3 install oauth2client --user
pip3 install requests --user
pip3 install httplib2 --user
pip3 install sqlalchemy --user
python3 db.py
python3 db_data.py