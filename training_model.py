import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from Data_Ingestion import data_loader
from application_logging.logger import App_Logger
from Data_preprocessing.preprocessing import Preprocessor
from Best_model_finder.tuner import Model_Finder
from File_Operations import file_method

class Model_Selection:

    def __init__(self):
        self.log = App_Logger()
        self.model_directory = 'models/'

    def TrainModel(self):
        """This method will train the model."""
        try:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Start of Training")
            # Get data
            data_getter = data_loader.Data_Getter()
            data = data_getter.get_data()
            """Doing data preprocessing"""
            preprocessor =  Preprocessor()
            #remove columns
            data = preprocessor.Remove_columns(data,'ID')
            #replace column names
            data = preprocessor.Replace_columnnames(data,'default_payment_next_month','Defaulter')
            data = preprocessor.Replace_columnnames(data,'PAY_0','PAY_1')
            
            #seperate label feature
            X,Y = preprocessor.separate_label_feature(data,'Defaulter')
            #balance label column
            X,Y = preprocessor.Balance_label_column()
        
            #split data in train and test data
            x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size = 0.30,random_state=42)
            
            #Model selection
            model_finder = Model_Finder()
            best_model_name,final_model = model_finder.get_best_model(x_train,y_train,x_test,y_test)
           
            #saving the best model to the directory
            file_op = file_method.File_Operation()
            file_op.dump_model(final_model,best_model_name)
            self.log.log(file,"End of Training")
            file.close()
        except Exception as e:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Unsuccessful End of Training"+str(e))
            file.close()
            raise e
    




    