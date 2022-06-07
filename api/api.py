from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    #Allows all origins
    allow_credentials=True,
    allow_methods=["*"],    #Allows all methods
    allow_headers=["*"],    #Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.get("/predict")
def predict(league_option:float, bet_option:float, odds:float):
    #Predict BET or NO BET based on the values inputed by the user

    X_pred = {"league_option": league_option,
               "bet_option": bet_option,
                "odds": odds
                }

    X_pred_df = pd.DataFrame(X_pred, index=[0])
    model = joblib.load('model.joblib')
    bet_no_bet = model.predict(X_pred_df)
    return {'result': f'{bet_no_bet[0]}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
