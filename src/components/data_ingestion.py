import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass # can directly define class variables
class DataIngestionConfig:
   train_data_path:str=os.path.join('artifacts','train.csv')# train data will be saved here
   test_data_path:str=os.path.join('artifacts','test.csv')# test data will be saved here
   raw_data_path:str=os.path.join('artifacts','raw.csv')
class DataIngestion:
   def __init__(self):
      self.ingestion_config=DataIngestionConfig()
   def initiate_data_ingestion(self):
      logging.info("entered the data ingestion method or components")
      try:
         df=pd.read_csv('notebook/data/stud.csv')
         logging.info('dataframe made')
         os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
         df.to_csv(self.ingestion_config.raw_data_path)
         logging.info("train test split initiated")
         train_set,test_set=train_test_split(df,test_size=0.2,random_state=43)
         train_set.to_csv(self.ingestion_config.train_data_path)
         test_set.to_csv(self.ingestion_config.test_data_path)
         logging.info("ingestion of data is completed")
         return(
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path

         )
      except Exception as e:
         raise CustomException(e,sys)
if __name__=="__main__":
   obj=DataIngestion()
   obj.initiate_data_ingestion()