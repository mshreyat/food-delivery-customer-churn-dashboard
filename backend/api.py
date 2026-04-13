from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from schemas import ChurnInput, ChurnResponse

app = FastAPI(title="Food Delivery Customer Churn API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/random_forest.pkl")

# Same ordinal mapping used in training
likert_map = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly agree": 5
}


@app.get("/")
def home():
    return {"message": "Food Delivery Churn API Running"}


@app.post("/predict-churn", response_model=ChurnResponse)
def predict_churn(data: ChurnInput):
    feature_columns = joblib.load("models/feature_columns.pkl")

    input_df = pd.DataFrame(
        [[0] * len(feature_columns)],
        columns=feature_columns
    )

    mapping = {
        "Age": data.Age,
        "Family size": data.Family_size,
        "Late Delivery": likert_map[data.Late_Delivery],
        "Poor Hygiene": likert_map[data.Poor_Hygiene],
        "Bad past experience": likert_map[data.Bad_past_experience],
        "Long delivery time": likert_map[data.Long_delivery_time],
        "More Offers and Discount": likert_map[data.More_Offers_and_Discount],
        "Good Food quality": likert_map[data.Good_Food_quality],
        "Ease and convenient": likert_map[data.Ease_and_convenient]
    }

    for col, value in mapping.items():
        input_df[col] = value

    pred = model.predict(input_df)[0]

    return {
    "prediction": "Likely to Stay" if str(pred).lower() == "yes" else "Likely to Churn"
}