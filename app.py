from datetime import timedelta,date
import psycopg2
import hashlib, uuid
from flask import Flask,render_template,request,session,flash,redirect,url_for
from flask_session import Session
from datetime import datetime
from markupsafe import escape






from model import *



app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "1c488f4b4a21cd7fbc5007664656985c2459b2362cf1f88d44b97e750b0c14b2cf7bc7b792d3f45db"
app.permanent_session_lifetime = timedelta(minutes=30)






db.init_app(app)

# @app.route('/')
# def index():
#     now=datetime.datetime.now()
#     new_year=now.month == 1 and now.day == 1
#     return render_template("index.html",new_year=new_year)


# @app.route('/index')
# def first():
#     name="Sam"
#     return render_template("index.html",headline=name)


# @app.route('/first')
# def first1():
#     return "Goodbye"

# @app.route('/second')
# def second1():
#     d=['Sam','Vishal','Mohan','Sai Kiran']
#     return render_template("second1.html",name=d)

# @app.route('/URL1')
# def Nav1():
#     return render_template("URLnav1.html")

# @app.route('/URL2')
# def Nav2():
#     return render_template("URLnav2.html")

# @app.route('/nav1')
# def navigation1():
#     return render_template("navigation1.html")

# @app.route('/nav2')
# def navigation2():
#     return render_template("navigation2.html")



# @app.route('/')
# def Nav1():
#     return render_template("index1.html")

# @app.route('/URL1')
# def Nav2():
#     return render_template("demo.html")
@app.route('/')
def first() :
    # db.create_all()
    return render_template("index1.html")

# def last():
#     j=shelf(user=sname,title=details)
#     db.session.add(j)
#     db.session.commit()
    
        



@app.route('/form1')
def form1():
    return render_template("form1.html")

@app.route('/form2',methods=["POST"])
def form2():
    session['name']=request.form.get("name")
    salt = uuid.uuid4().hex
    password=request.form.get("password")
    #PASS=hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    emailid=request.form.get("emailid")
    phoneNo=request.form.get("phonenumber")
    dob=request.form.get("birthday")
    # today=date.today()
    # now = datetime.now()

    f=datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    m=Test(username=session['name'],password=password,email=emailid,phone=phoneNo,dob=dob,timestamp=f)
    db.session.add(m)
    db.session.commit()

    # s=Session()
    
    

    return render_template("hello.html",names=session['name'])

    # m=Test("Sam","123","samswaroop97@gmail.com","9515226365","18-11-1997")
    # db.session.add(m)
    # db.session.commit()

@app.route('/form3')
def form3():
    return render_template("form2.html")

@app.route('/login',methods=["POST"])
def login():
    #name=request.form.get("name")
    session['name']=request.form.get("name")
    salt = uuid.uuid4().hex
    password=request.form.get("password")
    # PASS=hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    users=Test.query.all()
    for user in users:
        j=user.username
        k=user.password
        if 'name' in session and k==password:
            return render_template("hello.html",names=session['name'])
        else:
            # flash('Invalid user')
            continue
    flag=1
    return render_template("form1.html",flag=flag)
    # return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop("name", None)


    return render_template("first.html")


# @app.route('/index')
# def index():
    
#     if 'name' in session:
#         return 'Logged in as %s' % escape(session['name'])
#     return 'You are not logged in'


# @app.route('/logout')
# def logout():
#     session.pop('name',None)
#     return redirect(url_for('index'))


@app.route('/admin')
def admin():
    
    return render_template("admin.html",users=Test.query.all())



    
    # current_time = now.strftime("%H:%M:%S")
    
    # return render_template("hello.html",users=Test.query.all(),names=name,passwords=password)


@app.route('/search',methods=["POST"])
def search():
    name=request.form.get("search")
    # usr=Admin.query.filter(Admin.isbn.like(f'{name}%'))
    # print(usr)
    return render_template('hello.html',users=Admin.query.all(),name=name,n=session['name'])


@app.route('/details/<string:id>')
def details(id):
    print(id)
    # details=Admin.query.get(f'{id}')
    usr=Admin.query.all()
    for i in usr:
        if id == i.isbn:
            s=i.isbn
            p=i.author
            d=i.year
            e=i.title

    return render_template('details.html',details=e,s=s,p=p,d=d)

@app.route('/details1/<string:s>/<string:details>/<string:sname>', methods=['POST'])
def details1(s,details,sname):
    #usr=request.form.get('user')
    flag1=0
    flag=0
    star=request.form.get('stars')
    name=request.form.get('review')
    response= request.form.get('shelf')
    a=Review.query.all()
    for i in a:
        if i.use==sname and i.isbn==s:
            return render_template('hello.html',flag=1)
   
    g=Review(use=sname,isbn=s,rating=star,review=name)
    db.session.add(g)
    db.session.commit()
    if response=="Yes":
        j=shelf(use=sname,title=details)
        db.session.add(j)
        db.session.commit()
        return render_template('rating.html',s=s,details=details,sname=sname)
    else:
        return render_template('rating.html',s=s,details=details,sname=sname)

    
    return render_template('rating.html',s=s,details=details,sname=sname)


@app.route('/last/<string:title>')
def last(title):
    f=shelf.query.all()
    for i in f:
        if i.use==session['name'] and i.title==title:
            a="Book already present in bookshelf"
            return render_template('hello.html',u=shelf.query.all(),n=session['name'],a=a)
    j=shelf(use=session['name'],title=title)
    db.session.add(j)
    db.session.commit()
    return render_template('hello.html',u=shelf.query.all(),n=session['name'])




# @app.route('/last')
# def last():
#     j=shelf(user=sname,title=details)
#     db.session.add(j)
#     db.session.commit()






@app.route('/bookshelf/<string:names>', methods=['POST'])
def bookshelf(names):
    s=shelf.query.all()

    return render_template("hello.html",n=names,u=s)


# @app.route('/delete/<string:id>')
# def delete(id):
#     print(id)
#     s=shelf.query.all()
#     for i in s:
#         if i.user==session['name'] and i.title==id:
#             shelf.query.filter(shelf.user==session['name'],shelf.title==id).delete()
#             db.session.commit()
#     return render_template('hello.html',u=s,n=session['name'])

@app.route("/delete/<string:book>")
def delete(book):
    print(book)
    # title_delete = shelf.query.get_or_404(book)
    
    try:
        shelf.query.filter(shelf.use==session['name'],shelf.title==book).delete()
        db.session.commit()
        return render_template("hello.html",u=shelf.query.all(),n=session['name'])
    except:
        return render_template("hello.html",u=shelf.query.all(),n=session['name'])





@app.route('/home')
def home():
    d=shelf.query.all()
    return render_template('hello.html')

# @app.route('/last/<string:sname>/<string:details>')
# def last(sname,details):
#     j=shelf(user=sname,title=details)
#     db.session.add(j)
#     db.session.commit()
#     redirect('details')
    






if __name__ == "__main__" :

    with app.app_context() :
        main()



    



