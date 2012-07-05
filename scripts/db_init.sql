CREATE USER 'codestewdbuser'@'localhost' IDENTIFIED BY 'c0d3st3w1ns3cur3';
CREATE DATABASE IF NOT EXISTS codestew;
GRANT ALL PRIVILEGES ON codestew.* TO 'codestewdbuser'@'localhost' WITH GRANT OPTION;
