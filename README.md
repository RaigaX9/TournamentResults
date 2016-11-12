# TournamentResults

## Introduction

This project is done from Udacity's Full Stack Web Developer Nanodegree where we have to create a 
tournament result using Python and PostgreSQL.

## Instructions

1. Download Python 2.7.x
2. Download and install Vagrant and Virtual Box
3. After installing both, clone/download repository
4. Open command prompt, and navigate to the respository all the way to
the tournament folder
5. Run `vagrant up` to import and start up Vagrant
6. Run `vagrant ssh` to get into Vagrant
7. Navigate to `/vagrant/tournament`
8. Run `psql` to run PostgreSQL
9. Run `\i tournament.sql` to import the queries from `tournament.sql`
10. Run `\c tournament` to test if you are able to connect to the database.
11. Do `\q` to get out of `psql`
12. Run `python tournament-test.py` to run the test cases

## References

Udacity - Intro to Relational Database

[TutorialsPoint - PostgreSQL - Python Interface](https://www.tutorialspoint.com/postgresql/postgresql_python.htm)

[PostgreSQL Python tutorial](http://zetcode.com/db/postgresqlpythontutorial/)

[PostgreSQL Tutorial](http://www.postgresqltutorial.com/)