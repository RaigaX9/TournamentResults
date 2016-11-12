#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    # Delete query
    query = 'DELETE FROM Game;'
    # Execute query
    c2.execute(query)
    # Commit the query
    c1.commit()
    # Closes connection
    c1.close()

def deletePlayers():
    """Remove all the player records from the database."""
    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    # Delete query
    query = 'DELETE FROM Player;'
    # Execute query
    c2.execute(query)
    # Commit the query
    c1.commit()
    # Closes connection
    c1.close()

def countPlayers():
    """Returns the number of players currently registered."""
    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    query = 'SELECT count(*) FROM Player;'
    # Execute query
    c2.execute(query)
    # Retrieve alls of the items for the query
    x1 = c2.fetchall()
    # Returns the result
    x2 = x1[0][0]
    # print x2
    return x2


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    query = 'INSERT INTO Player (pname) VALUES (%s);'
    x = (name,)
    # Execute query
    c2.execute(query, x)
    c1.commit()
    # Closes connection
    c1.close()


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
    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    query = 'SELECT * FROM Ranks;'
    # Execute query
    c2.execute(query)
    # Retrieve alls of the items for the query
    x1 = c2.fetchall()
    return x1

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Connect and execute command
    c1 = connect()
    c2 = c1.cursor()
    query = 'INSERT INTO Game (win, lost) VALUES (%s, %s);'
    x = (winner, loser)
    # Execute query
    c2.execute(query, x)
    c1.commit()
    # Closes connection
    c1.close()
 
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
    x = 0
    arr1 = []
    # Generate swiss pairs of id and name
    # print len(playerStandings())/2
    for i in range(0, len(playerStandings())/2):
        #print len(playerStandings())/2
        n = playerStandings()[2*i]
        #print n
        m = playerStandings()[2*i+1]
        # print m
        # print playerStandings()
        # sp = n[0]
        # sp2 = n[1]
        # sp3 = m[0]
        # sp4 = m[1]
        # print sp
        # arr1.append(sp)
        # arr1.append(sp2)
        # arr1.append(sp3)
        # arr1.append(sp4) # Getting 16 for some reason
        sp = (n[0], n[1], m[0], m[1])
        arr1.append(sp)
        # print arr1

    # Returns resulting array
    # print arr1
    return arr1

