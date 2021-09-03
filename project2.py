from model import *
import os


from flask import Flask, session, render_template, request, session, flash, redirect, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:samswaroop@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "1c488f4b4a21cd7fbc5007664656985c2459b2362cf1f88d44b97e750b0c14b2cf7bc7b792d3f45db"

db.init_app(app)


@app.route("/")
def index():

    return render_template('search.html')


@app.route("/api/search", methods=['GET', 'POST'])
def search():
    keyword=request.form.get('search')
    s = Admin.query.all()
    print(keyword)
    r = []
    
    # data=request.get_json()
    # keyword=data.get("search")
    # code=keyword.status_codes
    # print(code)
    # if code==404:
    #     return jsonify({"error":"no books info found"}), 404


    flag=0
    # for j in s:
    #     if keyword==None or keyword=="":
    #         return jsonify({"no books found":"no books info found"}),404 
    # if  keyword=="":
    #     return jsonify({"error":"Invalid input"}),404 
    for i in s:
        g = {}

        # if i.isbn != keyword or i.title != keyword or i.author != keyword or i.year != keyword:
        #     print("Hello2")
        #     # return jsonify({"error":"no books info found"}), 404
        #     g['error']="No books found"
        #     r.append(g)
            


        if i.isbn == keyword or i.title == keyword or i.author == keyword or i.year == keyword:
            g['isbn'] = i.isbn
            g['title'] = i.title
            g['author'] = i.author
            g['year'] = i.year
            r.append(g)
            flag=1
            # print("Hello1")
            

        # if flag==0:
        #     return jsonify({'books': r}), 200
    # if flag==0:
    #     return jsonify({"error":"no books info found"}), 404


    f=len(r)
    return render_template('results.html',results=r,flag=flag,f=f)

@app.route("/api/reviews", methods=['GET', 'POST'])
def reviews():
    usr=request.form.get('username')
    d=Review.query.all()
    g=[]
    flag=0
    for i in d:
        h={}
        if i.user==usr:
            h["isbn"]=i.isbn
            h["rating"]=i.rating
            h["review"]=i.review
            flag=1
            g.append(h)
    l=len(g)
    
    return render_template('review.html',usr=usr,l=l,flag=flag,results=g)
    # return jsonify({"reviews":g}),200



