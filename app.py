from flask import Flask, render_template, request
import mysql.connector
import pickle
import datacheck as dc

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def login():
    # return {"hi":"I'm shalini"}
    return render_template('login.html')
@app.route('/auth', methods=['POST'])
def auth():
    user     = request.form['username']
    password = request.form['password']


    result = dc.getcred(user, password)
    if result == True:
        return render_template('home.html')
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route("/predict", methods=['post'])
def pred():
    
    Pregnancies= int(request.form['pregnancies'])
    Glucose= float(request.form['glucose'])
    BP= float(request.form['BP'])
    Insulin= float(request.form['insulin'])
    BMI= float(request.form['BMI'])
    Age= int(request.form['age'])
    prediction=model.predict([[Pregnancies,Glucose,BP,Insulin,BMI,Age]])[0]
    if(prediction==1):
        result="YOU HAVE DIABETES"
        return render_template("success.html",
                           data=result)
    else:
        result="YOU DO NOT HAVE DIABETES"
        return render_template("success.html",
                           data=result)
    


if __name__ == '__main__':
    app.run(debug = True, port=6789)

