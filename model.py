from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Test(db.Model):
      __tablename__="goodreads"
      username=db.Column(db.String(80),primary_key=True, nullable=False)
      
      password = db.Column(db.String(500), unique=True, nullable=False)

      email = db.Column(db.String(80),unique=True, nullable=False)

      phone=db.Column(db.String(80),unique=True, nullable=False)

      dob=db.Column(db.String(80),unique=True, nullable=False)

      timestamp = db.Column(db.DateTime, nullable=False)



      def __init__(self,username,password,email,phone,dob,timestamp):
          self.username=username
          self.password=password
          self.email=email
          self.phone=phone
          self.dob=dob
          self.timestamp = timestamp


class Admin(db.Model):
      __tablename__="books"
      isbn=db.Column(db.String(80),unique=False, nullable=False)
      
      title = db.Column(db.String(500), primary_key=True, nullable=False)

      author = db.Column(db.String(500), unique=False, nullable=False)

      year = db.Column(db.String(80), unique=False, nullable=False)
      def __init__(self,isbn,title,author,year):
          self.isbn=isbn
          self.title=title
          self.author=author
          self.year=year


class Review(db.Model):
      __tablename__="review"
      use=db.Column(db.String(80),primary_key=True, nullable=False)
      
      isbn = db.Column(db.String(500), primary_key=True, nullable=False)

      rating = db.Column(db.String(500), unique=False, nullable=False)

      review = db.Column(db.String(80), unique=False, nullable=False)

      def __init__(self,use,isbn,rating,review):
          self.use=use
          self.isbn=isbn
          self.rating=rating
          self.review=review
class shelf(db.Model):
      __tablename__="book_shelf"
      use=db.Column(db.String(80),primary_key=True, nullable=False)
      
      title = db.Column(db.String(500), primary_key=True, nullable=False)

      def __init__(self,use,title):
          self.use=use
          self.title=title
          
          

            