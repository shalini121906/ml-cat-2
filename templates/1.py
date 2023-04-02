from flask import Flask, render_template, request
import pymysql as pms
import pickle

model = pickle.load(open('model.pkl','rb'))

conn = pms.connect(host="localhost", 
                   port=3006,
                   user="root",
                   password="Fa$T@NdFur1ou$7",
                   db="login")
cur = conn.cursor()
app = Flask(_name_)

@app.route("/")
def start():
    return render_template("index.html")
    
@app.route("/login", methods=['post'])
def login():
    u=request.form["uname"]
    p=request.form["pswd"]
    d="select * from credentials where username=%s and password=%s"
    cur.execute(d,(u,p))
    r=cur.fetchall()
    if (not r)==False:
        return render_template("model.html")        
    else:
        return render_template("index.html", error="Invalid Login")
    
@app.route("/class", methods=["post"])
def classif():
    features = [float(i) 
                for i in 
                (request.form.values())]
    print(features)
    pred = model.predict([features])
    print(pred)
    if(pred==1):
        result="YOU MAY SUFFER HEART ATTACK"
        return render_template("success.html",data=result)
    else:
        result="YOU HAVE LESS CHANCES OF HEART ATTACK"
        return render_template("success.html",data=result)

    
if _name=='main_':
    app.run(host='localhost',port=5000)