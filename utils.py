import pickle
import pandas as pd
import config

class HousePricePrediction():

    def __init__(self, data):
        self.data = data

    def load_data(self):
        self.model = pickle.load(open(config.MODEL_PATH, 'rb'))

    def get_prediction(self):

        location   =  self.data['location']
        bhk        =  int(self.data['bhk'])
        total_sqft =  int(self.data['total_sqft'])
        bath       =  int(self.data['bath'])

        test_df= pd.DataFrame([[location, bhk, total_sqft, bath]], 
                            columns = ['location', 'bhk', 'total_sqft', 'bath'])

        self.load_data()        

        prediction = self.model.predict(test_df)[0]

        return int(prediction*1e5)