import joblib
import os

MODEL_PATH = os.path.join(
    "models",
    "tuned_xgboost_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict(data):

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    return prediction, probability