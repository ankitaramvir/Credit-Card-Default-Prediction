from datetime import datetime

class App_Logger():
    def __init__(self):
        pass
    
    def log(self,file_name,log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_name.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")

