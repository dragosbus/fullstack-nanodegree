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

## Create views for project

1. ```articles_views``` view contains article title and view

```
drop view article_views;
create view article_views as
    select articles.author, articles.title, paths_views.views
    from (
        select path, count(*) as views
        from log
        where status = '200 OK'
        group by path
    ) as paths_views
    right join articles
        on paths_views.path like ('/article/' || articles.slug);
```

2. ```daily_error_date``` view to support "On which days did more than 1% of requests lead to errors?"

```
drop view daily_error_date;
create view daily_error_date as
    select daily_request.date, round(daily_error.error_request * 100.0 / daily_request.total_request, 2) as error_rate
    from (
        select time::date as date, count(*) as total_request
        from log
        group by date
    ) as daily_request
        join (
        select time::date as date, count(*) as error_request
        from log
        where status != '200 OK'
        group by date
    ) as daily_error
        on daily_request.date = daily_error.date;
```

## How to run the app?

```python3 app.py```
