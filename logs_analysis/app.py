import psycopg2


fname = open('result.txt','w')

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

    q = '''SELECT title, views FROM article_views ORDER BY views DESC LIMIT 3'''
    res = connect_to_db(q)

    return res

def popular_author():
    '''Get most popular authors'''

    q = '''SELECT authors.name, SUM(article_views.views) AS total_views FROM authors JOIN article_views ON authors.id = article_views.author GROUP BY authors.id ORDER BY total_views DESC
    '''
    res = connect_to_db(q)

    return res


popular_articles = get_popular_articles()
fname.write('1. What are the most popular three articles of all time?\n')
for article in popular_articles:
    fname.writelines('{}-{}\n'.format(article[0], article[1]))

popular_authors = popular_author()
fname.writelines('\n2.Who are the most popular article authors of all time?')
for author in popular_authors:
    fname.writelines('{}-{}\n'.format(author[0], author[1]))