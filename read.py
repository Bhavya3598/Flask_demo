# import psycopg2
# conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=samswaroop")
# cur = conn.cursor()
# with open('books.csv', 'r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f) # Skip the header row.
#     cur.copy_from(f, 'administrator', sep=',')

# conn.commit()


from model import *

from app import app,db

import csv


# db.create_all()

def main():
    data=open('books.csv')
    r=csv.reader(data)
    
    for i in r:
        s=Admin(isbn=i[0],title=i[1],author=i[2],year=i[3])
        db.session.add(s)
    db.session.commit()






if __name__=='__main__':
    with app.app_context() :
        main()


