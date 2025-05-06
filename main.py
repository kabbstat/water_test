from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import water
app = FastAPI(
    title ='water potability prediction',
    description = 'This is a water potability prediction API.'
)

with open('D:\ML PROJECT\ml_pipeline\model.pkl','rb') as file :
    model = pickle.load(file)

@app.get('/')
def index():
    return {'message': 'Welcome to the water potability prediction FastAPI!'}

@app.post('/predict')
def model_predict(water: water):
    sample = pd.DataFrame({
        'ph': [water.ph],
        'Hardness': [water.Hardness],
        'Solids': [water.Solids],
        'Chloramines': [water.Chloramines],
        'Sulfate': [water.Sulfate],
        'Conductivity': [water.Conductivity],
        'Organic_carbon': [water.Organic_carbon],
        'Trihalomethanes': [water.Trihalomethanes],
        'Turbidity': [water.Turbidity]
    })
    prediction_value  = model.predict(sample)
    if prediction_value == 1:
        return {'prediction': 'The water is potable.'}
    else:
        return {'prediction': 'The water is not potable.'}