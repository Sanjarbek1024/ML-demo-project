from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sklearn.datasets import fetch_20newsgroups

# Load the saved model
model = joblib.load("models/news_classifier_pipeline.pkl")

# Load category names (20 newsgroups target names)
categories = fetch_20newsgroups(subset="train").target_names

# Define request body
class NewsInput(BaseModel):
    text: str

# Create FastAPI app
app = FastAPI(
    title="20 Newsgroups Classifier API",
    description="A simple API that classifies text into one of the 20 newsgroups categories",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "20 Newsgroups Classifier API is running 🚀"}

@app.post("/predict")
def predict_news(data: NewsInput):
    prediction = model.predict([data.text])[0]
    category = categories[prediction]
    return {
        "prediction": int(prediction),
    
        "category": category
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)