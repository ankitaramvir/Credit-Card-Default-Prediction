"""@app.route('/predict', methods=['POST'])
def predict():
    '''for rendering results on HTML'''
    #training validation
    if request.method == 'POST':

        features = [int(x) for x in request.form.values()]
        feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
        
        features_arr = np.array(feature_list).reshape(-1,24)
    df2 = pd.DataFrame(feature_list,columns=['LIMIT_BAL','SEX','EDUCATION',
                                             'MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1',
                                             'BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1',
                                             'PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'])
    
    
    if os.path.exists('Prediction_FileFromDB/InputFile.csv'):
        os.remove('Prediction_FileFromDB/InputFile.csv')
    
    
    if request.method == 'POST':
        'Gender=request.form[features[0]],
        'Education'=request.form[features[1]],
        'Marrital Status'=features[2],
        'Age'=features[3],
        'Limit Balance':features[4],
        'PAY_1':features[5],
        'PAY_2':features [6],
        'PAY_3':features [7],
        'PAY_4':features [8],
        'PAY_5':features [9],
        'PAY_6':features [10],
        'BILL_AMT1':features [11],
        'BILL_AMT2':features [12],
        'BILL_AMT3':features [13],
        'BILL_AMT4':features [14],
        'BILL_AMT5':features [15],
        'BILL_AMT6':features [16],
        'PAY_AMT1':features[17],
        'PAY_AMT2':features[18],
        'PAY_AMT3':features [19],
        'PAY_AMT4':features[20],
        'PAY_AMT5':features[21],
        'PAY_AMT6':features[22],
        'Defaulter':default_payment[0]
        
    prediction = Prediction.PredictionFromModel(features_arr)
    default_payment=prediction.tolist()
    return render_template("index.html",prediction)"""
