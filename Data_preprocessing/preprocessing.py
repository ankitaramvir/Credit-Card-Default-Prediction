from imblearn.combine import SMOTETomek
from application_logging.logger import App_Logger
from Data_Ingestion import data_loader
import pandas as pd
class Preprocessor:
    """This class is used to preprocess the data before training"""

    def __init__(self):
        self.log = App_Logger()

    def Remove_columns(self,data,column):
        """This method will remove columns from the dataframe"""

        try:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Removing columns from dataframe started")
            data.drop(columns =column,axis=1,inplace = True)
            self.log.log(file,"Columns removed successfully")
            file.close()
            return data
        except Exception as e:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,'Exception occured in remove_columns method of the Preprocessor class. Exception message:  '+str(e))
            raise e
    def Replace_columnnames(self,data,column,new_columnname):
        """This method will replace column names in the dataframe"""
        try:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Replacing column name in dataframe started")
            data.rename(columns={column:new_columnname},inplace=True)
            self.log.log(file,"Replacing column name in dataframe completed")
            file.close()
            return data
        except Exception as e:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,'Exception occured in replace_columnnames method of the Preprocessor class. Exception message:  '+str(e))
            raise e
        
    def separate_label_feature(self,data,label_column_name):
        """This method separates the features and a Label Coulmns."""
        try:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Entered the separate_label_feature method of the Preprocessor class")
            self.X=data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y=data[label_column_name] # Filter the Label columns
            self.log.log(file,"Label Separation Successful. Exited the separate_label_feature method of the Preprocessor class")
            file.close()
            return self.X,self.Y
        except Exception as e:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e)")
            file.close()
            raise e
            
    
    def Balance_label_column(self):
        """This method is used to balance the label column"""
        try:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Entering Balance_label_column method.")
            
            smk = SMOTETomek(random_state=42)
            self.X_res,self.Y_res = smk.fit_resample(self.X,self.Y)
            file.close()
            return self.X_res,self.Y_res
        except Exception as e:
            file = open('Training_logs/PreprocessingLog.txt','a+')
            self.log.log(file,"Exception occured in Balance_label_column method of the Preprocessor class. Exception message:  ' + str(e)")
            file.close()
            raise e


