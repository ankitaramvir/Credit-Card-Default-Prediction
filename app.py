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
        print(data_for_prediction.ndim)
        
        
        """df2 = pd.DataFrame(feature_list,columns=['LIMIT_BAL','SEX','EDUCATION',
                                             'MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1',
                                             'BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1',
                                             'PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'])"""
    
    model_training = PredictFromModel.Prediction()
    model_training.ModelTrainingForPrediction()

    prediction = PredictFromModel.Prediction()
    predict = prediction.PredictionFromModel(data_for_prediction)
    return render_template('index.html',prediction_text = predict)

if __name__=='__main__':
    app.run(debug=True)