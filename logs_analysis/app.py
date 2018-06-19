#!/usr/bin/env python3

import psycopg2


fname = open('result.txt', 'w')


def connect_to_db(q):
    '''connect to database and
    execute a query'''

    conn = psycopg2.connect(database='news')
    cur = conn.cursor()
    cur.execute(q)

    res = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return res


def get_popular_articles():
    '''Get first 3 popular articles'''

    q = '''SELECT title, views
    FROM article_views ORDER BY views DESC LIMIT 3'''
    res = connect_to_db(q)

    return res


def get_popular_authors():
    '''Get most popular authors'''

    q = '''SELECT authors.name, SUM(article_views.views) AS total_views
    FROM authors JOIN article_views ON authors.id = article_views.author
    GROUP BY authors.id ORDER BY total_views DESC
    '''
    res = connect_to_db(q)

    return res


def get_most_errors():
    '''Get days where are more than 1% errors'''

    q = '''SELECT * FROM daily_error_date WHERE error_rate > 1'''

    res = connect_to_db(q)

    return res


popular_articles = get_popular_articles()
fname.write('1. What are the most popular three articles of all time?\n')
for article in popular_articles:
    fname.writelines('{}--{}\n'.format(article[0], article[1]))

popular_authors = get_popular_authors()
fname.writelines('\n2.Who are the most popular article authors of all time?')
for author in popular_authors:
    fname.writelines('{}--{}\n'.format(author[0], author[1]))

most_errors = get_most_errors()
fname.writelines('''\n3. On which days did more than
1% of requests lead to errors?\n''')
for error in most_errors:
    fname.writelines('{}--{}% errors'.format(error[0], error[1]))
