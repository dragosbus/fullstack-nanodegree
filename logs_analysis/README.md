# Logs Analysis

## About

This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## How to run?

### You will need:

1. Python3
2. Postgres

### Setup(For Linux)

1. Clone this repository
2. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. From command line go to this repository folder
4. Create a new user with name vagrant(```sudo -u postgres createuser vagrant```)
5. Create a new database with name news(```createdb news```)
6. Import data drom sql file in news database(```psql -d db_name -f query_file.sql```)
