import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass
    def makePredictions(self, sex_flag, BMI, SmokerStatus, GeneralHealth, AgeCategory):
        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Sex"] = [sex_flag]
        df["BMI"] = [BMI]
        df["SmokerStatus"]=[SmokerStatus]
        df["GeneralHealth"]= [GeneralHealth]
        df["AgeCategory"]= [AgeCategory]
       
        # model
        model = pickle.load(open("heartattack_version2.h5", 'rb'))

        # columns in order
        df = df.loc[:, ['Sex', 'BMI', 'SmokerStatus', 'GeneralHealth', 'AgeCategory']]

        preds = model.predict_proba(df)
        return(preds[0][1])
