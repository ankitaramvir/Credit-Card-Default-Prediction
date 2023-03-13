import pandas as pd
from application_logging.logger import App_Logger
import os

class Data_Getter_Pred:
    """This class shall  be used for obtaining the data from the source for prediction."""

    def __init__(self):
        self.log = App_Logger()
        self.prediction_file='Prediction_FileFromDB/InputFile.csv'

    def get_data(self):
        """This method reads the data from source."""
        try:
            file = open("Prediction_Logs/DataloaderPrediction.txt","a+")
            self.log.log(file,"Entered the get_data method of the Data_Getter class")
            # reading the data file
            csv_data = pd.read_csv(self.prediction_file)
            self.data = pd.Series(csv_data)
            self.log.log(file,"Data Load Successful.Exited the get_data method of the Data_Getter class")
            file.close()
            return self.data
        except Exception as e:
            file = open("Prediction_Logs/DataloaderPrediction.txt","a+")
            self.log.log(file,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            file.close()
            raise e
    