from application_logging.logger import App_Logger
import mysql.connector as connection
import pandas as pd
from sqlalchemy import create_engine

class dboperation:
    """This class will handle all the database operations"""

    def __init__(self,DatabaseName):
        self.log = App_Logger()
        self.DatabaseName = DatabaseName

    
    def DatabaseConnection(self):
        """ This method will create connection with mysql database"""
        try:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Attempting to connect with mysql")
            
            #establishing connection with mysql
            conn = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)
            # check if the connection is established
            print(conn.is_connected())
            self.log.log(file,"Connection successful")
            file.close()
            
        except ConnectionError:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Error while connecting to database: %s" %ConnectionError)
            file.close()
            raise ConnectionError
        return conn

    def Createdb(self,DatabaseName):
        """This method creates database with given name and if the database already exists then open the connection to the db."""
        try:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Creating database in mysql")
            conn = self.DatabaseConnection()
            cur = conn.cursor() #create a cursor to execute queries
            cur.execute("SHOW DATABASES")
            result = cur.fetchall()
            #creating database if it doesn't exist in mysql
            for i in result:
                if i[0] == DatabaseName:
                    print("Database exists")
                else:
                    cur.execute("CREATE DATABASE IF NOT EXISTS %s" %DatabaseName)
            self.log.log(file,"Created database in mysql")
            file.close()
            conn.close()
        except Exception:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Error while creating database: %s" %Exception)
            file.close()
            conn.close()
            raise Exception
        cur.close()

    def Createtable(self,DatabaseName,Tablename):
        """This method will create table inside the database"""

        try:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Create table method initialised")
            conn = self.DatabaseConnection()
            cur = conn.cursor() #create a cursor to execute queries
            cur.execute("USE %s" %DatabaseName)
            cur.execute("DROP TABLE IF EXISTS %s"%Tablename)
            cur.execute("FLUSH TABLES %s"%Tablename)
            cur.execute("CREATE TABLE %s(ID INTEGER, LIMIT_BAL INTEGER,SEX INTEGER, EDUCATION INTEGER, MARRIAGE INTEGER, AGE INTEGER,PAY_0 INTEGER,PAY_2 INTEGER,PAY_3 INTEGER,PAY_4 INTEGER,PAY_5 INTEGER,PAY_6 INTEGER,BILL_AMT1 INTEGER,BILL_AMT2 INTEGER,BILL_AMT3 INTEGER,BILL_AMT4 INTEGER,BILL_AMT5 INTEGER,BILL_AMT6 INTEGER, PAY_AMT1 INTEGER,PAY_AMT2 INTEGER, PAY_AMT3 INTEGER,PAY_AMT4 INTEGER,PAY_AMT5 INTEGER,PAY_AMT6 INTEGER, default_payment_next_month INTEGER)" %Tablename)
            file.close()
            conn.close()
        except Exception as e:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Error while creating table in database: %s" %e)
            file.close()
            conn.close()
            raise Exception
        cur.close()

    def Insertdata(self,DatabaseName,Tablename):
        """Insert Data to Table"""
        try:
            data = pd.read_csv('UCI_Credit_Card.csv')   
            df = pd.DataFrame(data)
            
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Inserting data into sql table method initialised")
            conn = self.DatabaseConnection()
            cur = conn.cursor() #create a cursor to execute queries
            cur.execute("USE %s" %DatabaseName)
            engine = create_engine("mysql://root:mysql@localhost:3306/%s" %DatabaseName)
            
            df.to_sql(name=Tablename,con=engine,if_exists='append',index=False)
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
            self.log.log(file,"Data inserted into table")
            file.close()
            conn.close()
        except Exception as e:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Error while inserting data in database: %s" %e)
            file.close()
            conn.close()
            raise e
        cur.close()
    
    def selectingDatafromtableintocsv(self,DatabaseName,Tablename):
        """This method exports the data in GoodData table as a CSV file. in a given location above created."""
        self.fileFromDb = 'Training_FileFromDB/'
        self.fileName = 'InputFile.csv'
        try:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Exporting data into csv file")
            conn = self.DatabaseConnection()
            cur = conn.cursor() #create a cursor to execute queries
            cur.execute("USE %s"%DatabaseName)
            sqlSelect = pd.read_sql("SELECT *  FROM good_raw_data",conn)
            df1=pd.DataFrame(sqlSelect,columns = ['ID','LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6','default_payment_next_month'])
            df1.to_csv(self.fileFromDb+self.fileName,index=False)
            file.close()
            conn.close()
        except Exception as e:
            file = open('Training_logs/DataBaseConnectionLog.txt','a+')
            self.log.log(file,"Error while exporting data into csv file: %s" %e)
            file.close()
            conn.close()
            raise Exception
        cur.close()
