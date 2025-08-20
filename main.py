from dotenv import load_dotenv
import os

load_dotenv('.env')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

from fastapi import FastAPI

app = FastAPI()

{
    "petal length": 4.5,
    "petal width": 0.0,
    "sepal length": 0.0,
    "sepal width": 0.0
}

@app.get("/iris")
async def iris_predict():
    return {
        "message": "Iris prediction endpoint success"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', reload=True)