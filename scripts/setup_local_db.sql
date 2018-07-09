DROP DATABASE IF EXISTS :db_name;
CREATE DATABASE :db_name;

DROP ROLE IF EXISTS :db_user;
CREATE ROLE :db_user LOGIN PASSWORD :'db_password';
GRANT ALL PRIVILEGES ON DATABASE :db_name to :db_user;

\connect :db_url;
DROP SCHEMA IF EXISTS :db_schema CASCADE;
CREATE SCHEMA :db_schema;
