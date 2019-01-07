apt-get -qqy update
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
apt-get -qqy install python-sqlalchemy
apt-get -qqy install python-pip
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
sudo apt install nodejs
pip3 install --upgrade pip
pip3 install werkzeug --user
pip3 install flask --user
pip3 install Flask-Login==0.1.3 --user
pip3 install oauth2client --user
pip3 install requests --user
pip3 install sqlalchemy --user
pip3 install --upgrade google-auth --user
pip3 install pycodestyle --user
npm rebuild node-sass
npm run build
python3 db.py
python3 db_data.py