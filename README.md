# Covid19-prediction-API
A RESTful API built over Python flask to predict the number of positive cases which may be reported on a a particular day. Used linear regression model on a kaggle provided dataset. Deployed on heroku sever.


Heroku API: https://covid19mlapi.herokuapp.com/

Method: POST on https://covid19mlapi.herokuapp.com/predict
using form data with parameter 'date'.
Response: A JSON object with a predicted value of number of cases on the specified date as passed to the API
