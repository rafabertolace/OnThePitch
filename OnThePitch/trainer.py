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

    #Step 3: Define X and y
    y = df['Payout Under PC']
    X = df.drop(columns = ['Bin Odds Under PC', 'Payout Under PC'])

    #Step 4: Split the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    #Step 5:Train the model
    m = xgb.XGBRegressor(n_estimators = 500, max_depth = 16)
    m.fit(X_train, y_train)

    #Step 6: Save the trained model
    save_model(m)
