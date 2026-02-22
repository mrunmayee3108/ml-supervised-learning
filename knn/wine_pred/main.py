from fastapi import FastAPI
import pickle 
import numpy as np

app = FastAPI()

with open("wine_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    values = list(data.values())
    features = np.array(values).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)
    return {"prediction":prediction[0]}