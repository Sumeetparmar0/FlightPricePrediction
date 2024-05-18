import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self): 
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 airline:str,
                 source_city:str,
                 departure_time:str,
                 stops:str,
                 arrival_time:str,
                 destination_city:str,
                 class_type:str,
                 duration:float,
                 days_left:int
                 ):
        
        self.airline=airline
        self.source_city=source_city
        self.departure_time=departure_time
        self.stops=stops
        self.arrival_time=arrival_time
        self.destination_city=destination_city
        self.class_type=class_type
        self.duration=duration
        self.days_left=days_left

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'airline':[self.airline],
                'source_city':[self.source_city],
                'departure_time':[self.departure_time],
                'stops':[self.stops],
                'arrival_time':[self.arrival_time],
                'destination_city':[self.destination_city],
                'class_type':[self.class_type],
                'duration':[self.duration],
                'days_left':[self.days_left]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
