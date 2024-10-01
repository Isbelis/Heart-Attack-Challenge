import pandas as pd
import pickle

class ModelHelper():
    def __init__(self):
        pass

    def prediction(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,
               Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer):
    
        model = pickle.load(open("heart_model.h5", 'rb'))
        scaler = pickle.load(open('heart_scaler.h5', 'rb'))

        df = pd.DataFrame()
        df['BMI'] = [BMI]
        df['Smoking'] = [Smoking]
        df['AlcoholDrinking'] = [AlcoholDrinking]
        df['Stroke'] = [Stroke]
        df['PhysicalHealth'] = [PhysicalHealth]
        df['MentalHealth'] = [MentalHealth]
        df['DiffWalking'] = [DiffWalking]
        df['Sex'] = [Sex]
        df['AgeCategory'] = [AgeCategory]
        df['Race'] = [Race]
        df['Diabetic'] = [Diabetic]
        df['PhysicalActivity'] = [PhysicalActivity]
        df['GenHealth'] = [GenHealth]
        df['SleepTime'] = [SleepTime]
        df['Asthma'] = [Asthma]
        df['KidneyDisease'] = [KidneyDisease]
        df['SkinCancer'] = [SkinCancer]
        
        num_columns = ['BMI', 'PhysicalHealth','MentalHealth','SleepTime','AgeCategory']
        #heart_disease = df.HeartDisease.apply(lambda x: 1 if x == "Yes" else 0)
        num_feats = df.loc[:,num_columns]
        cat_feats = df.loc[:,['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex',
            'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth',
            'Asthma', 'KidneyDisease', 'SkinCancer']]
        cat_feats.Smoking = cat_feats.Smoking.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.AlcoholDrinking = cat_feats.AlcoholDrinking.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.Stroke = cat_feats.Stroke.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.DiffWalking = cat_feats.DiffWalking.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.Sex = cat_feats.Sex.apply(lambda x: 1 if x == "Male" else 0)
        cat_feats.Diabetic = cat_feats.Diabetic.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.PhysicalActivity = cat_feats.PhysicalActivity.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.Asthma = cat_feats.Asthma.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.KidneyDisease = cat_feats.KidneyDisease.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.SkinCancer = cat_feats.SkinCancer.apply(lambda x: 1 if x == "Yes" else 0)
        cat_feats.Race.replace({
            "White": 0,
            "Hispanic": 1,
            "Black": 2,
            "Other": 3,
            "Asian": 4,
            "American Indian/Alaskan Native":5}, inplace=True)
        cat_feats.GenHealth.replace({
            "Excellent": 0,
            "Very good": 1,
            "Good": 2,
            "Fair": 3,
            "Poor": 4}, inplace=True)
        num_feats.AgeCategory.replace({
            "18-24": 21,
            "25-29": 27,
            "30-34": 32,
            "35-39": 37,
            "40-44": 42,
            "45-49": 47,
            "50-54": 52,
            "55-59": 57,
            "60-64": 62,
            "65-69": 67,
            "70-74": 72,
            "75-79": 77,
            "80 or older":83}, inplace=True)
        scaler.fit(num_feats)
        
        # predict/transform
        scaled_data = scaler.transform(num_feats)
        df_scaled = pd.DataFrame(scaled_data, columns=num_columns)
        
        df_final = pd.concat([df_scaled, cat_feats], axis=1)

        prediction = model.predict(df_final)

        if prediction == 0:
            return 'You are not considered to be at a high risk for heart disease'
        else:
            return 'You are considered to be at high risk of heart disease'
