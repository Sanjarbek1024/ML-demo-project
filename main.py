from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
from sklearn.datasets import fetch_20newsgroups

# Load model
model = joblib.load("models/news_classifier_pipeline.pkl")
categories = fetch_20newsgroups(subset="train").target_names

# FastAPI app
app = FastAPI(
    title="20 Newsgroups Classifier API",
    description="A simple web app that classifies news text",
    version="1.0.0"
)

# Templates & static
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text: str = Form(...)):
    prediction = model.predict([text])[0]
    category = categories[prediction]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": category,
            "text": text
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
