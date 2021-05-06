import uvicorn   #  ASGI Request
from fastapi import FastAPI
from input import promote
import numpy as np
import pickle
import pandas as pd
import os

app = FastAPI()
pickle_in = open("Pickle_RL_Model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def base_route():
  return {'message': 'Welcome to Praxis'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

@app.post('/predict')
def predict_promotion(data: promote):
  data = data.dict()
  gender = data['gender']
  no_of_trainings = data['no_of_trainings']
  age = data['age']
  previous_year_rating = data['previous_year_rating']
  length_of_service = data['length_of_service']
  KPIs_met = data['KPIs_met']
  awards_won = data['awards_won']
  avg_training_score = data['avg_training_score']
  department_Analytics = data['department_Analytics']
  department_Finance = data['department_Finance']
  department_HR = data['department_HR']
  department_Legal = data['department_Legal']
  department_Operations = data['department_Operations']
  department_Procurement = data['department_Procurement']
  department_RD = data['department_RD']
  department_Sales_Marketing = data['department_Sales_Marketing']
  department_Technology = data['department_Technology']
  region_region_1 = data['region_region_1']
  region_region_10 = data['region_region_10']
  region_region_11 = data['region_region_11']
  region_region_12 = data['region_region_12']
  region_region_13 = data['region_region_13']
  region_region_14 = data['region_region_14']
  region_region_15 = data['region_region_15']
  region_region_16 = data['region_region_16']
  region_region_17 = data['region_region_17']
  region_region_18 = data['region_region_18']
  region_region_19 = data['region_region_19']
  region_region_2 = data['region_region_2']
  region_region_20 = data['region_region_20']
  region_region_21 = data['region_region_21']
  region_region_22 = data['region_region_22']
  region_region_23 = data['region_region_23']
  region_region_24 = data['region_region_24']
  region_region_25 = data['region_region_25']
  region_region_26 = data['region_region_26']
  region_region_27 = data['region_region_27']
  region_region_28 = data['region_region_28']
  region_region_29 = data['region_region_29']
  region_region_3 = data['region_region_3']
  region_region_30 = data['region_region_30']
  region_region_31 = data['region_region_31']
  region_region_32 = data['region_region_32']
  region_region_33 = data['region_region_33']
  region_region_34 = data['region_region_34']
  region_region_4 = data['region_region_4']
  region_region_5 = data['region_region_5']
  region_region_6 = data['region_region_6']
  region_region_7 = data['region_region_7']
  region_region_8 = data['region_region_8']
  region_region_9 = data['region_region_9']
  education_Bachelor = data['education_Bachelor']
  education_Below_Secondary = data['education_Below_Secondary']
  education_Master = data['education_Master']
  recruitment_channel_other = data['recruitment_channel_other']
  recruitment_channel_referred = data['recruitment_channel_referred']
  recruitment_channel_sourcing = data['recruitment_channel_sourcing']
  prediction = classifier.predict([[gender, no_of_trainings, age, previous_year_rating,length_of_service, KPIs_met, awards_won, avg_training_score,
department_Analytics,department_Finance,department_HR,department_Legal,department_Operations,department_Procurement,department_RD,department_Sales_Marketing,
department_Technology,region_region_1,region_region_10,region_region_11,region_region_12,region_region_13,region_region_14,region_region_15,
region_region_16,region_region_17,region_region_18,region_region_19,region_region_2,region_region_20,region_region_21,region_region_22,region_region_23,
region_region_24,region_region_25,region_region_26,region_region_27,region_region_28,region_region_29,region_region_3,region_region_30,region_region_31,
region_region_32,region_region_33,region_region_34,region_region_4,region_region_5,region_region_6,region_region_7,region_region_8,region_region_9,
education_Bachelor,education_Below_Secondary,education_Master,recruitment_channel_other,recruitment_channel_referred,recruitment_channel_sourcing]])
  if(prediction==1):
    prediction="Promoted"
  else:
    prediction="Not Promoted"
  return {'Prediction': prediction}

if __name__=="__main__": 
  port = int(os.environ.get("PORT",8000))
  uvicorn.run(app, host='0.0.0.0', port=port)
#uvicorn main:app --reload