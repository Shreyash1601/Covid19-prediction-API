from flask import Flask,request,jsonify
import numpy as np
import pickle
from dateutil import parser

app=Flask(__name__)
@app.route("/",methods=["POST"])
def predict():
    with open("CWY.pickle","rb") as f:
        model=pickle.load(f)
    date=parser.parse(request.form['date']).toordinal()
    cases=round(abs((model.predict(np.array([[date]]))[0][0])))
    response=jsonify({
        "cases":cases
    })

    response.headers.add("Access-Control_Allow-Origin","*")

    return response
if __name__=="__main__":
    app.run(debug=True)