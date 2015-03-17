====================================
  ___        _       _____ 
 / __|_ __ _(_)_____|_   _|
 \__ \ V  V / (_-<_-< | |  
 |___/\_/\_/|_/__/__/ |_|  
                          
====================================

Swiss Tournament Rankings Generator

Implemented by 	: 	Raj Prasad
Date		:	17/03/2015

Introduction:
A Swiss-system tournament is a tournament which uses a non-elimination format. There are several rounds of competition, but considerably fewer rounds than in a round-robin tournament, so each competitor (team or individual) does not play every other competitor. Competitors meet one-to-one in each round and are paired using a predetermined set of rules designed to ensure that as far as possible a competitor plays competitors with the same current score, subject to not playing the same opponent more than once. The winner is the competitor with the highest aggregate points earned in all rounds. (Wikipedia)

Files Included:

tournament.sql : PSQL commands used to create database structure
tournament.py  : python code which interfaces with the database
tournament_test.py : test files used to test functionality of the tournament.py file 

Running the Program:
First of all make sure you have python and Postgres installed into the computer
You will need to open Postgres and import the SQL commands in tournament.sql file
Next use python to run the tournament_test.py file to test tournamenament.py
It will test for eight conditions and if does not pass will throw an error

Note: Please ensure all your files are in the same directory
