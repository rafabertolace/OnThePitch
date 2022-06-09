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
def predict(D1:float, D2:float, D3:float, D4:float, vig_rate:bool, market_consensus:bool,
            year:int, match_time_after_4_pm:float, match_time_before_4_pm:float,
            odds_1_to_1_5:float, odds_1_5_to_2_0:float, odds_2_0_to_3:float, odds_3_to_10:float):
    #Predict BET or NO BET based on the values inputed by the user

    X_pred = {
            'D1': D1,
            'D2': D2,
            'D3': D3,
            'D4': D4,
            'vig_rate': vig_rate,
            'market_consensus': market_consensus,
            'year': year,
            'match_time_after_4_pm': match_time_after_4_pm,
            'match_time_before_4_pm': match_time_before_4_pm,
            'odds_1_to_1_5': odds_1_to_1_5,
            'odds_1_5_to_2_0': odds_1_5_to_2_0,
            'odds_2_0_to_3': odds_2_0_to_3,
            'odds_3_to_10': odds_3_to_10
            }

    X_pred_df = pd.DataFrame(X_pred, index=[0])
    model = joblib.load('model.joblib')
    bet_no_bet = model.predict(X_pred_df)
    return {'return': f'{bet_no_bet[0]}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
