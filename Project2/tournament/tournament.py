#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
#Edited By: Raj Prasad 3/3/15
#Project 2: Udacity FullStack
## This program contains methods to interface with a back end Database. It is an
## implementation for managing Swiss Tournament. It implements methods to register players
# count players, update match results and to update player standings in addition to deleting
# the for managing new tournament
##

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()
    


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM players")
    numb = c.rowcount
    DB.close()
    return numb

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c=DB.cursor()
    SQL = "INSERT INTO players (name) VALUES (%s);"
    content = (bleach.clean(name, strip=True),)
    c.execute(SQL, content)
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c=DB.cursor()
    #Creates a number of views to simplify select query
    c.execute("DROP VIEW IF EXISTS combined")
    c.execute("DROP VIEW IF EXISTS winners")
    c.execute("DROP VIEW IF EXISTS losers")
    c.execute("CREATE VIEW winners AS SELECT id, name, winner, loser FROM players p1 \
        LEFT OUTER JOIN matches m1 ON p1.id=m1.winner ")

    c.execute("CREATE VIEW losers AS SELECT id, name, winner, loser FROM players \
         JOIN matches ON players.id=matches.loser ")          

    c.execute("CREATE VIEW combined AS SELECT * FROM winners\
                UNION\
                SELECT * FROM losers")

    #From existing data contains a table containing player id, name, wins and matches
    c.execute ("SELECT id, name, SUM(CASE WHEN id = winner THEN 1 ELSE 0 END) AS Wins, \
                SUM(CASE WHEN id = winner OR id = loser THEN 1 ELSE 0 END) AS Matches \
                FROM combined GROUP BY id, name ORDER BY Wins DESC")

    rows = c.fetchall()
    DB.commit()
    DB.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c=DB.cursor()
    c.execute('INSERT INTO matches (winner, loser) VALUES (%s, %s)', (winner, loser))
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    swissList =[]

    DB = connect()
    c=DB.cursor()
    c.execute ("SELECT id, name, SUM(CASE WHEN id = winner THEN 1 ELSE 0 END) AS Wins, \
                SUM(CASE WHEN id = winner OR id = loser THEN 1 ELSE 0 END) AS Matches \
                FROM combined GROUP BY id, name ORDER BY Wins DESC")
    # while there is valid rows of data in the query result, pairs of player details
    # are extracted. Player ID and name is extracted and the players are paired together
    # and added to swissList. Once finished iterating through, the list is returned
    
    while True:
        playerA=c.fetchone()
        if playerA == None:
            break
        playerB = c.fetchone()
        truple = playerA[0], playerA[1], playerB[0], playerB[1]
        swissList.append(truple)
    c.close()
    return swissList
