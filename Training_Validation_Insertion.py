from application_logging.logger import App_Logger
from Data_Insertion_db_trainingdata.data_insertion import dboperation

class train_validation():
    
    def __init__(self):
        self.log = App_Logger()
        self.dBOperation = dboperation("CCD_Training_Data_F")
    
    def train_validation(self):
        try:
            file = open("Training_Logs/Training_Main_Log.txt","a+")
            self.log.log(file,"Creating Training_Database")
            #create database with given name, if present open the connection! 
            self.dBOperation.Createdb("CCD_Training_Data_F")
            self.log.log(file,"Creating Training_Database completed")
            #Create table with columns
            self.dBOperation.Createtable("CCD_Training_Data_F","good_raw_data")
            self.log.log(file,"Table creation completed")
            #Insert data into table
            self.dBOperation.Insertdata("CCD_Training_Data_F","good_raw_data")
            self.log.log(file,"Insertion of csv file data into db table completed!")
            # export data in table to csvfile
            self.dBOperation.selectingDatafromtableintocsv("CCD_Training_Data_F","good_raw_data")
            self.log.log(file,"csv file successfully created")
            file.close()

        except Exception as e:
            file=open("Training_Logs/Training_Main_Log.txt","a+")
            self.log.log(file,"Something went wrong while performing db operation" + str(e))
            raise e
        
