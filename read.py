#


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


