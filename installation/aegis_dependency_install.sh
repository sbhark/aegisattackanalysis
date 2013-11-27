#!/bin/bash 

printf "Install script for dependencies for aegisiattackanalysis"

printf "\nInstalling sudo";
apt-get install sudo;

printf "\nPerforming apt-get update"; 
sudo apt-get update;

printf "\nInstalling MongoDB";
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10;

echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" >> /etc/apt/sources.list;

sudo apt-get update;

sudo apt-get install mongodb-10gen;

printf "\nInstalling python-dev / build-essential";
sudo apt-get install build-essential python-dev -y;

printf "\nInstalling python-pip";
sudo apt-get install python-pip -y;

printf "\nInstalling PyMongo";
sudo pip install pymongo;

printf "\nInstalling requests";
sudo pip install requests; 

printf "\nInstalling GIT";
sudo apt-get install git-core -y;

printf "\nPlease configure GIT";

printf "\naegisattackanalysis package dependencies installation complete! ";
