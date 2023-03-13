from application_logging.logger import App_Logger
from Data_Ingestion.data_loader import Data_Getter
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

class Model_Finder():
    """This class shall  be used to find the model with best accuracy and AUC score"""

    def __init__(self):
        self.log = App_Logger()
        self.rf = RandomForestClassifier()

    def get_best_params_for_rf(self,train_x,train_y):
        """Use best parameter for best accuracy with hyperparameter tuning."""
        try:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Entered the get_best_params_for_rf method of the Model_Finder class")
            # initializing with different combination of parameters
            """self.param_grid = {'max_depth': [90,100],'max_features': [3,4],'min_samples_leaf': [3,4],
                                            'min_samples_split': [12,13],'n_estimators': [200,300]}
            #creating object for gridsearchcv
            self.grid = GridSearchCV(estimator=self.rf,param_grid = self.param_grid, cv = 3, n_jobs = -1, verbose = 2)
            #finding the best parameters
            self.grid.fit(train_x, train_y)
            #extracting best parameters 
            self.max_depth = self.grid.best_params_['max_depth']
            self.max_features = self.grid.best_params_['max_features']
            self.min_samples_leaf = self.grid.best_params_['min_samples_leaf']
            self.min_samples_split = self.grid.best_params_['min_samples_split']
            self.n_estimators = self.grid.best_params_['n_estimators']"""
            #creating a new model with the best parameters
            self.rf = RandomForestClassifier(n_estimators=200,max_depth=90,max_features=3,min_samples_leaf=3,min_samples_split=12)
            #train new model
            self.rf.fit(train_x,train_y)
            self.log.log(file,"Exited the get_best_params_for_rf method of the Model_Finder class")
            file.close()
            return self.rf
        except Exception as e:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Exception occured in get_best_params_for_svm method of the Model_Finder class. Exception message:" + "str(e)")
            file.close()
            raise e
    
    def get_best_model(self,train_x,train_y,test_x,test_y):
        """Predict the values and accuracy of the model."""
        try:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Entered the get_best_model method of the Model_Finder class")
            #create prediction model
            self.randomforest = self.get_best_params_for_rf(train_x,train_y)
            # prediction using the Random Forest Algorithm
            self.prediction_rf = self.randomforest.predict(test_x)
            #accuracy score
            self.rf_score = accuracy_score(test_y,self.prediction_rf)
            self.log.log(file,'Accuracy for random forest:' + str(self.rf_score))
            file.close()
            return 'Randomforest',self.randomforest
        except Exception as e:
            file = open("Training_Logs/ModelTrainingLog.txt","a+")
            self.log.log(file,"Exception occured in get_best_model method of the Model_Finder class. Exception message:" + "str(e)")
            file.close()
            raise e

        

