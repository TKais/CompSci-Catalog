# CompSci Catalog

A catalog of computer science tutorials, resources, and general information categorized by principal areas of study within computer science, including artificial intelligence, human computer interaction, database systems, programming languages, computer systems and networks, software engineering, vision and graphics, numerical analysis, theory of computing, and bioinformatics. 

## Before running the CompSci Catalog

* [Install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* This project is meant to be ran with Python 3.4 or higher

## Running CompSci Catalog

* Clone CompSci Catalog repo.
* Once cloned, change into the directory for the CompSci Catalog project and run the command `cd vagrant`.
* Inside the `vagrant` directory, run the command `vagrant up` to bring the virtual machine online.
* Next, you'll need to log into the virtual machine. Do this by running the command `vagrant ssh`. Once logged in, you'll be in the home directory in the virtual machine -- run `cd ../../vagrant` to get into the correct directory.
* Make sure you're in the `vagrant` folder. You can find out if you're in the right place by running the command `pwd` and making sure you're in `vagrant/`. Running the command `ls` should show a `catalog` folder, a `README.md` file, and `Vagrantfile`).
* Run the command `bash config.sh` to install all necessary dependencies and set up the database with dummy data.
* Run the command `cd catalog` to change into the catalog directory.
* Run the command `python3 main.py` to start the flask server.
* Navigate to http://localhost:5000 in your browser to see the application.

## Technical Details
This project utilizes the following technologies:

* Python 3
* Flask
* SQLite
* OAuth 2.0
* SQLAlchemy