from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)


@app.route('/')
def home():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        ssql="select * from task"
        cus.execute(ssql)
        data=cus.fetchall()
        db.commit()
        print(data)
        return render_template('dashboard.html',d=data)
    except Exception:
        print("The error is",Exception)

@app.route('/form')
def fm():
    return render_template('form.html')
    
@app.route('/store',methods=['POST'])
def store():
    t=request.form['firstname']
    t1=request.form['lastname']
    dt=request.form['gender']
    d1=request.form['countryname']
    d2=request.form['PhoneNumber']
    d=request.form['date']
    #return t+t1+dt+d1+d2+d3+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        insql="insert into task (FirstName,LastName,Gender,CountryName,PhoneNumber,date) values('{}','{}','{}','{}','{}','{}')".format(t,t1,dt,d1,d2,d)
        cus.execute(insql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)

@app.route('/edit/<rid>')
def edit(rid):
    # return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cur=db.cursor()
        esql="select * from task where id= '{}'".format(rid)
        cur.execute(esql)
        data=cur.fetchone()
        return render_template('editform.html',d=data)
        
    except Exception as e:
        print("Error:",e)


@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    # return "ID to be  update in db is:"+rid
    t=request.form['firstname']
    t1=request.form['lastname']
    dt=request.form['gender']
    d1=request.form['countryname']
    d2=request.form['PhoneNumber']
    d=request.form['date']
    #return t+t1+dt+d1+d2+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cur=db.cursor()
        usql="update task SET FirstName='{}',Lastname='{}',Gender='{}',CountryName='{}',PhoneNumber='{}',date='{}' where id='{}'".format(t,t1,dt,d1,d2,d,rid)
        cur.execute(usql)
        db.commit()
        return redirect('/')
        
    except Exception as e:
        print("Error:",e)

@app.route('/delete/<rid>')
def delete(rid):
    # return "Id is"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todoapp")
        cus=db.cursor()
        dsql="delete from task where id={}".format(rid)
        cus.execute(dsql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)        



app.run(debug=True)

