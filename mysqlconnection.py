from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from sqlalchemy import Table, Column, MetaData, Text
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASS'] = ''
app.config['MYSQL_DB'] = 'mars'
mysql = MySQL(app)
db = SQLAlchemy(app)

class Addd():
    __tablename__ = 'addd' 
    p_id = db.Column(db.String(255), nullable = False)
    p_type = db.Column(db.String(255), nullable = False)
    p_content = db.Column(db.String(255), nullable = False)
    calories = db.Column(db.String(255), nullable = False)
    s_date = db.Column(db.String(255), nullable = False)
    e_date = db.Column(db.String(255), nullable = False)
    qty = db.Column(db.String(255), nullable = False)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    
    if (request.method == 'POST'):
        p_id = request.form.get('p_id')
        p_type = request.form.get('p_type')
        p_content = request.form.get('p_content')
        calories = request.form.get('calories')
        s_date = request.form.get('s_date')
        e_date = request.form.get('e_date')
        qty = request.form.get('qty')
        entry = Addd(p_id=p_id, p_type=p_type, p_content=p_content, calories=calories, s_date=s_date, e_date=e_date, qty=qty)
        db.session.add(entry)
        db.session.commit()
        
    return render_template('home.html')

@app.route('/a')
def a():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `addd`")
    data= cur.fetchall() 
    return render_template('a.html',   dddd=data)



@app.route('/del_view')
def del_view():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `addd`")
    data= cur.fetchall() 
    return render_template('deleteview.html',  dddd=data)

@app.route('/sch_view')
def sch_view():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM addd")
    data= cur.fetchall()  
    return render_template('scheduleview.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)