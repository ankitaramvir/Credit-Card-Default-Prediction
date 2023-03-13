import pandas as pd
from application_logging.logger import App_Logger

class Data_Getter:
    """This class shall  be used for obtaining the data from the source for training."""
    def __init__(self):
        self.log = App_Logger()
        #self.training_file='Training_FileFromDB/InputFile.csv'

    def get_data(self):
        """This method reads the data from source."""
        try:
            file = open("Training_logs/DataloadingLog.txt",'a+')
            self.log.log(file,'Entered the get_data method of the Data_Getter class')
            self.data= pd.read_csv('Training_FileFromDB/InputFile.csv',) # reading the data file
            self.log.log(file,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            file.close()
            return self.data

        except Exception as e:
            file = open('Training_logs/DataloadingLog.txt','a+')
            self.log.log(file,'Exception occured in get_data method of the Data_Getter class. Exception message:'  + str(e))
            file.close()
            raise e
    