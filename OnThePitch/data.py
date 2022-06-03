import pandas as pd

GCP_BUCKET_PATH = "gs://onthepitch869/"
GCP_FOLDER_NAME = "data/"
filename = 'belgium_2019_2020.csv'


def get_data(nrows=10_000):
    '''returns a DataFrame with nrows from GCP bucket'''
    df = pd.read_csv(GCP_BUCKET_PATH + GCP_FOLDER_NAME + filename, nrows=nrows)
    return df


if __name__ == '__main__':
    df = get_data()
