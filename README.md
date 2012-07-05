codestew
========

Codestew: a Code Review Tool


MySQL Note: I obviously don't want to make my root password available to everyone given this will be hosted
in a public github repo. I have therefore created a specific development user for this project that can only
work on the codestew db. So, to make things easy for you if you wish to use my same setup I have included 
a really short SQL script to create the DB, DB user and grant the correct permissions. Use it as follows:

mysql -u root -p < $REPOHOME/scripts/db_init.sql
