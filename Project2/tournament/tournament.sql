-- Project 2 Full Stack 9/3/15 written by :Raj Prasad

-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id SERIAL, name VARCHAR(32), PRIMARY KEY (id));

CREATE TABLE matches (id SERIAL primary key, Winner SERIAL references players(id), Loser SERIAL references players(id));

