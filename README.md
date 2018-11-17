# CompSci Catalog

A log analyzer that queries a database containing newspaper articles. The log has a database row for each time a reader loaded a web page. Using that information, this analyzer answers the following questions about user activity:

## Before running the CompSci Catalog

* [Install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Install Vagrant](https://www.vagrantup.com/downloads.html)
* This project is meant to be ran with Python 3.4 or higher

## Running CompSci Catalog

* Clone CompSci Catalog repo.
* Once cloned, change into the directory for the CompSci Catalog project and run the command `cd vagrant`.
* Inside the `vagrant` directory, run the command `vagrant up` to bring the virtual machine online.
* Next, you'll need to log into the virtual machine. Do this by running the command `vagrant ssh`. Once logged in, you'll be in the home directory -- run `cd ../../vagrant` to get into the correct directory.
* In the `catalog` directory, run the command `python3 main.py`.

## Technical Details
This project utilizes the following technologies:

* Python 3
* Flask
* SQLite
* OAuth
* SQLAlchemy