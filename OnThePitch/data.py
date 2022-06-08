import pandas as pd

GCP_BUCKET_PATH = "gs://onthepitch869/"
GCP_FOLDER_NAME = "data/"


def get_data_X(nrows=20_000):
    '''returns a DataFrame with nrows from GCP bucket'''
    df = pd.read_csv(GCP_BUCKET_PATH + GCP_FOLDER_NAME + 'X_train.csv', nrows=nrows)
    return df

def get_data_y(nrows=20_000):
    '''returns a DataFrame with nrows from GCP bucket'''
    df = pd.read_csv(GCP_BUCKET_PATH + GCP_FOLDER_NAME + 'y_train.csv', nrows=nrows)
    return df


if __name__ == '__main__':
    df = get_data_X(nrows=10)
    print(df)

    df = get_data_y(nrows=10)
    print(df)
