import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass
    def makePredictions(self, sex_flag, BMI, SmokerStatus, GeneralHealth, AgeCategory, PhysicalHealthDays, MentalHealthDays, RaceEthnicityCategory, AlcoholDrinkers):
        
        
    
   
     # create dataframe of one row for inference
        df = pd.DataFrame()
        df["PhysicalHealthDays"] = [PhysicalHealthDays]
        df["SleepHours"]=[SleepHours]
        df["BMI"]= [BMI]
        df["MentalHealthDays"]=[MentalHealthDays]
        df["AgeCategory"]=[AgeCategory]
        df["Sex"]=[Sex]
        df["RaceEthnicityCategory"]=[RaceEthnicityCategory]
        df["SmokerStatus"]=[SmokerStatus]
        df["AlcoholDrinkers"]=[AlcoholDrinkers]
        df["GeneralHealth"]=[GeneralHealth]


        # Encoding, separate out features
        meta = ['HadHeartAttack']
        num_features = ['PhysicalHealthDays', 'SleepHours', 'BMI', 'MentalHealthDays','AgeCategory']
        cat_features = ['Sex', 'RaceEthnicityCategory','SmokerStatus','AlcoholDrinkers','GeneralHealth']
        
        # model
        model = pickle.load(open("heartattack_version2.h5", 'rb'))
        scaler = pickle.load(open('heartattack_scaler_version_2.h5', 'rb'))





        # columns in order
        df = df.loc[:, ['Sex', 'BMI', 'SmokerStatus', 'GeneralHealth', 'AgeCategory']]

        preds = model.predict_proba(df)
        return(preds[0][1])
        