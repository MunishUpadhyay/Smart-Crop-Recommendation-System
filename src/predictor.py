import joblib
import os

MODEL_PATH = os.path.join("saved_models", "crop_model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_crop(model, features: list):
    """
    Predicts the crop using the given features.

    Parameters:
    - model: Trained model object.
    - features: List of inputs [N, P, K, temperature, humidity, ph, rainfall].

    Returns:
    - The predicted crop name.
    """
    return model.predict([features])[0]