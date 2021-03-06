from flask import Flask,request,jsonify
import numpy as np
import pickle
from dateutil import parser

app=Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to Covid prediction API"
@app.route("/predict",methods=["POST"])
def predict():
    with open("CWY.pickle","rb") as f:
        model=pickle.load(f)
    try:
      date=parser.parse(request.form['date']).toordinal()
      if(date):
       cases=round(abs((model.predict(np.array([[date]]))[0][0])))
      else:
        cases=None
    except:
        cases=None
    response=jsonify({
        "cases":cases
    })

    response.headers.add("Access-Control-Allow-Origin","*")

    return response
if __name__=="__main__":
    app.run(debug=True)