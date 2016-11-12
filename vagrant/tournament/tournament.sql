-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE Player (id SERIAL PRIMARY KEY, pname TEXT);

CREATE TABLE Game (id SERIAL PRIMARY KEY, lost INTEGER REFERENCES Player (id), win INTEGER REFERENCES Player (id));

CREATE VIEW Ranks AS
  SELECT Player.id as id, Player.pname as pname, (SELECT count(*)
      FROM Game
      WHERE Player.id = Game.win) AS wins,
    (SELECT count(*)
      FROM Game
      WHERE Player.id = Game.lost OR Player.id = Game.win) AS Game
    FROM Player
    ORDER BY wins DESC;