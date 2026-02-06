from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load

# Initialize FastAPI
app = FastAPI(
    title="EDUwise Academic Risk API",
    description="Predicts whether a student is academically at risk",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (OK for demo)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load model and scaler
model = load("app/models/eduwise_model.joblib")
scaler = load("app/scalers/scaler.joblib")

# Input schema
class StudentInput(BaseModel):
    attendance_rate: float
    average_grade: float
    study_hours_per_week: float
    engagement_score: float
    previous_failures: int

# Root route
@app.get("/")
def root():
    return {"message": "EDUwise API is running"}

# Prediction route
@app.post("/predict")
def predict_risk(data: StudentInput):
    features = np.array([[
        data.attendance_rate,
        data.average_grade,
        data.study_hours_per_week,
        data.engagement_score,
        data.previous_failures
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

@app.post("/recommend")
def recommend_resources(data: StudentInput):
    # Prepare input
    features = np.array([[
        data.attendance_rate,
        data.average_grade,
        data.study_hours_per_week,
        data.engagement_score,
        data.previous_failures
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    recommendations = []

    if prediction == 1:
        risk_status = "At Risk"

        if data.average_grade < 50:
            recommendations.append("Basic Mathematics & Core Subject Video Tutorials")

        if data.study_hours_per_week < 7:
            recommendations.append("Time Management & Study Skills Guide")

        if data.previous_failures > 0:
            recommendations.append("One-on-One Peer Tutoring Program")

        if not recommendations:
            recommendations.append("General Academic Support Resources")

    else:
        risk_status = "Not At Risk"
        recommendations.append("Advanced Learning & Enrichment Materials")

    return {
        "risk_status": risk_status,
        "recommended_resources": recommendations
    }

    return {
        "at_risk": int(prediction)
    }
