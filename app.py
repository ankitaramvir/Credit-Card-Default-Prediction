from flask import Flask,jsonify,request,render_template
import PredictFromModel
import os
import numpy as np
import pandas as pd
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():       
    if request.method == 'POST':

        features = [int(x) for x in request.form.values()]
        feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
        
        data_for_prediction = np.array(feature_list).reshape(1,23)
    
    model_training = PredictFromModel.Prediction()
    model_training.ModelTrainingForPrediction()

    prediction = PredictFromModel.Prediction()
    predict = prediction.PredictionFromModel(data_for_prediction)
    return render_template('index.html',prediction_text = predict)

if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)