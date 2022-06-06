import pandas as pd

GCP_BUCKET_PATH = "gs://onthepitch869/"
GCP_FOLDER_NAME = "data/"
filename = 'temp_data_set.csv'


def get_data(nrows=10_000):
    '''returns a DataFrame with nrows from GCP bucket'''
    df = pd.read_csv(GCP_BUCKET_PATH + GCP_FOLDER_NAME + filename, nrows=nrows)
    return df


if __name__ == '__main__':
    df = get_data(nrows=100)
    print(df)
