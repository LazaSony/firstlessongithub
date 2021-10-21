from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
import numpy as np
import pandas as pd

class PredictionCharges():
    MODEL_SAVE_LOCATION = "data/"

    def __init__(self):
        self.df = self.load_data()
        scaled_X, y = self.preprocessing()
        self.train_best_model(scaled_X, y)
        self.save_model()
        
    def load_data(self):
        return pd.read_csv(self.MODEL_SAVE_LOCATION + "insurance.csv")

    def preprocessing(self):
        X=self.df.drop(["charges"],axis = 1)
        y=self.df["charges"]
        self.ct = ColumnTransformer(transformers=[
                                            ('one_hot_encoder', OneHotEncoder(), [1, 4, 5])], 
                                            remainder='passthrough')
        # self.ct.fit(X)
        # X = np.array(self.ct.transform(X))                                    
        X = np.array(self.ct.fit_transform(X))
        
        self.scaler = StandardScaler()
        # self.scaler.fit(X)
        # scaled_X = self.scaler.transform(X)
        scaled_X = self.scaler.fit_transform(X)
        return scaled_X, y

    def train_best_model(self, scaled_X, y):
        self.model = RandomForestRegressor(max_depth=6)
        self.model.fit(scaled_X, y)
    
    def save_model(self):
        pickle.dump(self.model,  open(self.MODEL_SAVE_LOCATION +"classification_model.joblib", 'wb'))
        pickle.dump(self.ct,  open(self.MODEL_SAVE_LOCATION + "col_transformer.joblib", 'wb'))
        pickle.dump(self.scaler,  open(self.MODEL_SAVE_LOCATION + "scaler.joblib", 'wb'))

    def predict(self, value_to_predict):
        df= pd.DataFrame([value_to_predict],columns=["age", "sex", "bmi", "children", "smoker", "region"])

        loaded_ct = pickle.load(open(self.MODEL_SAVE_LOCATION + "col_transformer.joblib", 'rb'))
        loaded_scaler = pickle.load(open(self.MODEL_SAVE_LOCATION + "scaler.joblib", 'rb'))
        loaded_model = pickle.load(open(self.MODEL_SAVE_LOCATION + "classification_model.joblib", 'rb'))

        X = np.array(loaded_ct.transform(df))
        X = loaded_scaler.transform(X)

        prediction = loaded_model.predict(X)[0]
        return round(prediction,2)

