import pickle
from application_logging.logger import App_Logger
import os
import shutil

class File_Operation:
       """This class shall be used to save the model after training and load the saved model for prediction."""

       def __init__(self):
             self.log = App_Logger()

       def dump_model(self,model,filename):
        try:
            file = open("Training_Logs/filemethod.txt","a+")
            self.log.log(file,"Start of dump model method")
            path = 'models'
            #remove previously existing models
            if os.path.isdir(path):
                shutil.rmtree('models')
                os.makedirs(path)
            else:
                os.makedirs(path)
            #dump file in pickle format
            with open(path +'/' + filename +'.pkl', 'wb') as fp:
                pickle.dump(model, fp)
            self.log.log(file,"End of dump model method")
            file.close()
            return 'success'
                
        except Exception as e:
            file = open("Training_Logs/filemethod.txt","a+")
            self.log.log(file,'Exception occured in dump_model method of the Model_Selection class. Exception message:  ' + str(e))
            file.close()
            raise e
        
       def load_model(self):
        try:
            file = open("Training_Logs/filemethod.txt","a+")
            self.log.log(file,"Start of load model method")
            
            load_model = pickle.load(open('models/Randomforest.pkl','rb'))
            self.log.log(file,"End of load model method")
            file.close()
            return load_model             
        except Exception as e:
            file = open("Training_Logs/filemethod.txt","a+")
            self.log.log(file,'Exception occured in load_model method of the Model_Selection class. Exception message:  ' + str(e))
            file.close()
            raise e