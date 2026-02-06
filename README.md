# EDUwise – Machine Learning API

## Project Overview

EDUwise is an AI-powered educational support system designed to assist students by:

* Predicting academic performance
* Recommending appropriate study materials

This project represents an **initial functional prototype (MVP)** developed as part of an academic software/ML course. The focus is on demonstrating correct understanding of requirements, appropriate tool usage, and a complete ML-to-API pipeline.

---

## Objectives

* Build a simple machine learning model for student performance prediction
* Expose the model through a REST API
* Add a recommendation endpoint for study materials
* Demonstrate the system using Swagger UI and a lightweight frontend mockup

---

## Machine Learning Component

### Dataset

* Source: UCI Student Performance Dataset
* Features used include:

  * Study time
  * Absences
  * Previous grades
  * Family and academic-related attributes

### Model

* Algorithm: **Logistic Regression**
* Library: `scikit-learn`
* Task: Classification (Pass / Fail)

The trained model is saved and loaded by the API for inference.

---

## Backend (API)

### Framework

* **FastAPI** – for building RESTful APIs
* **Uvicorn** – ASGI server

### Available Endpoints

#### `/predict` (POST)

Predicts student performance based on input features.

**Input:**

```json
{
  "study_time": 2,
  "absences": 4,
  "previous_grade": 12
}
```

**Output:**

```json
{
  "prediction": "Pass"
}
```

---

#### `/recommend` (POST)

Provides study material recommendations based on predicted performance.

**Input:**

```json
{
  "prediction": "Fail"
}
```

**Output:**

```json
{
  "recommendations": [
    "Basic revision notes",
    "Introductory video tutorials",
    "Extra practice exercises"
  ]
}
```

---

### API Documentation

* Swagger UI available at:

  ```
  http://127.0.0.1:8000/docs
  ```

---

## Frontend Mockup

A simple HTML/CSS/JavaScript interface is included to:

* Collect user inputs
* Send requests to the API
* Display predictions and recommendations

The frontend focuses on **clarity and usability**, not advanced styling.

---

## Development Environment Setup

### Requirements

* Python 3.9+

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/irakozej/EDUwise-MVP.git
cd eduwise-api


# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --reload
```

---

## Project Structure

```
eduwise-api/
│── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│
│── frontend/
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│
│── notebooks/
│   ├── model_training.ipynb
│
│── requirements.txt
│── README.md
```

---

## Alignment with Rubric

* Correct understanding of project requirements
* Appropriate tool selection (ML + API + UI)
* Proper environment setup using virtual environments
* Clear navigation via Swagger UI and frontend mockup

---

## Future Improvements

* Use multi-class or regression models
* Add authentication and user profiles
* Personalize recommendations using user history
* Deploy to cloud infrastructure

---

## Author

**Student Name:** *Jean Paul IRAKOZE*

**Project:** EDUwise – AI-powered Educational Support System

---

## License

This project is for academic purposes only.
