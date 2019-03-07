#!/usr/bin/env python

# Make sure to create the views defined in README.md file
# before running this program


import psycopg2
import sys


DBNAME = "news"


def get_result(query):
    """return the result of the query."""

    db = None
    rows = []
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
    except psycopg2.Error as e:
        print(" Error !\n {}".format(e))
        if db is not None:
            db.close()
        sys.exit(1)
    else:
        db.close()
    return rows


def print_result(question, answer, op):
    """print the result of each query"""

    print('\n' + '-' * 60)
    print(question)
    print('-' * 60 + '\n')
    for a in answer:
        print('\t {} - {}{}'.format(a[0], a[1], op))


q1 = "1- The most popular three articles of all time"
q2 = "2- The most popular article authors of all time"
q3 = "3- The days that more than 1% of requests lead to errors"


query1 = """SELECT title, views
            FROM viewstab
            ORDER BY views DESC
            LIMIT 3;"""

query2 = """SELECT name, sum(views) AS views
            FROM viewstab, authors
            WHERE viewstab.author = authors.id
            GROUP BY author, authors.name
            ORDER BY views DESC;"""

query3 = """SELECT TO_CHAR(errortab.date, 'FMMonth DD, YYYY'),
                   (error::real/total*100)::decimal(4, 2)
            FROM errortab, totaltab
            WHERE errortab.date = totaltab.date
            AND (error::float/total) >= 0.01;"""

r1 = get_result(query1)
r2 = get_result(query2)
r3 = get_result(query3)

if __name__ == "__main__":
    print('\n\n' + ' '*20 + 'News Log Report')
    print_result(q1, r1, ' views')
    print_result(q2, r2, ' views')
    print_result(q3, r3, '% errors')
    print('\n\n' + ' '*26 + 'End \n')
