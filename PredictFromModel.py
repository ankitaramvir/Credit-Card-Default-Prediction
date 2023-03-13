import pandas as pd
import os
from application_logging.logger import App_Logger
import File_Operations.file_method
import Training_Validation_Insertion
import training_model

class Prediction:
    """This class is used to predict the output"""

    def __init__(self):
        self.log = App_Logger()

    def ModelTrainingForPrediction(self):
        try:
            file = open("PredictFromModel.txt","a+")
            self.log.log(file,'Train the model for prediction')
            train_valObj = Training_Validation_Insertion.train_validation() #object initialization
            train_valObj.train_validation() #calling the training_validation method
            #training model
            train_modelobj = training_model.Model_Selection() #object initialization
            train_modelobj.TrainModel() #calling the trainmodel method
            self.log.log(file,"Training of model for prediction finished")
            file.close()
            return "success"
        except Exception as e:
            file = open("PredictFromModel.txt","a+")
            self.log.log(file,'Error in TrainModelforPrediction method in Prediction class' + str(e))
            file.close()
            raise e

    def PredictionFromModel(self,data):

        try:
            file = open("PredictFromModel.txt","a+")
            self.log.log(file,'Start of Prediction')
            file_met = File_Operations.file_method.File_Operation()
            load_model = file_met.load_model()
            pred_rf = load_model.predict(data)
            if pred_rf == 1:
                result = "The credit card holder will be Defaulter in the next month"
            if pred_rf == 0:
                result = "The Credit card holder will not be Defaulter in the next month"
            self.log.log(file,'End of Prediction')
            file.close()
            return result
        except Exception as e:
            file = open("PredictFromModel.txt","a+")
            self.log.log(file,'Error occured while running the prediction!! Error:: %s' %e)
            file.close()
            raise e


            
        

