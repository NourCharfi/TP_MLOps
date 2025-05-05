from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import warnings
from sklearn.exceptions import DataConversionWarning

# Supprimer les avertissements de conversion de données
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# Charger le modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Route GET pour vérifier si l'API fonctionne
@app.get("/")
def home():
    return {"message": "API MLOps fonctionne !"}

# Définition des données d'entrée pour la prédiction
class InputData(BaseModel):
    features: list

# Route POST pour effectuer des prédictions
@app.post("/predict")
def predict(data: InputData):
    # Convertir les features en numpy array
    features_array = np.array(data.features).reshape(1, -1)
    
    # Effectuer la prédiction
    prediction = model.predict(features_array)
    
    return {"prediction": int(prediction[0])}
