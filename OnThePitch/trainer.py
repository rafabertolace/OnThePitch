#Custom functions
from OnThePitch.data import get_data_X, get_data_y
from OnThePitch.utils import save_model
#XGBoost functions
import xgboost as xgb


if __name__ == "__main__":
    #Step 1: Get the data from the GCP
    N = 13000
    df_X_train = get_data_X(nrows=N)
    df_y_train = get_data_y(nrows=N)

    #Step 2: Define our train and test dataframes (based on the seasons)
    #df_train = df[df['season_21_22']==False][['country_div_1','country_div_2','country_div_3','country_div_4',
                                                #'%vig_p_bool','Market_consensus','year_number','game_starts_after_4pm_2',
                                                #'game_starts_after_4pm_1','1.0_to_1.5','1.5_to_2.0','2.0_to_3','3_to_10',
                                                #'payout_under_2.5_pinacle_closing']]

    #df_test = df[df['season_21_22']==True]

    #Step 3: Define our X_train and y_train
    X_train = df_X_train.drop(columns='Unnamed: 0')
    y_train = df_y_train.drop(columns='Unnamed: 0')

    #Step 4:Train the model
    m = xgb.XGBRegressor()
    m.fit(X_train, y_train)

    #Step 7: Save the trained model
    save_model(m)
