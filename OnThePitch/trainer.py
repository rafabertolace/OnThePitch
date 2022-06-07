#Custom functions
from OnThePitch.data import get_data
from OnThePitch.utils import save_model
#Scikit Learn functions
from sklearn.model_selection import train_test_split
#XGBoost functions
import xgboost as xgb


if __name__ == "__main__":
    #Step 1: Get the data from the GCP
    N = 1000
    df = get_data(nrows=N)

    #Step 2: Select which league the user chose
    #df = df[df['league'] == 'inserir a opção do usuário']

    #Step 3: Define our train and test dataframes (based on the seasons)
    df_train = df[df['season_21_22']==False]
    #df_test = df[df['season_21_22']==True]

    #Step 4: Define our X_train and y_train
    #X_train = df_train.drop(columns='payout_under_2.5_pinacle_closing')
    X_train = df_train[['year_number', 'year_number_ratio', 'month_number']] #Delete this line
    y_train = df_train['payout_under_2.5_pinacle_closing']

    #Step 5: Split the data set
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0)

    #Step 6:Train the model
    m = xgb.XGBRegressor()
    m.fit(X_train, y_train)

    #Step 7: Save the trained model
    save_model(m)
