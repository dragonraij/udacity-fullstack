-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- Project 2 Full Stack 9/3/15 written by :Raj Prasad

CREATE TYPE outcomes AS ENUM ('P1 Win', 'P2 Win', 'Draw', 'Unplayed');

CREATE TABLE players (id SERIAL, name VARCHAR(32), PRIMARY KEY (id));
CREATE TABLE matches (id SERIAL primary key, Player1 SERIAL references players(id), Player2 SERIAL references players(id), Outcome outcomes);