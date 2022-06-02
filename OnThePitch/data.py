import pandas as pd

GCP_BUCKET_PATH = "gs://onthepitch869/data/"
filename = 'belgium_2019_2020.csv'


def get_data(nrows=10_000):
    '''returns a DataFrame with nrows from GCP bucket'''
    df = pd.read_csv(GCP_BUCKET_PATH+filename, nrows=nrows)
    return df


#Função de exemplo! Avaliar a necessidade de limpar o data set!
'''def clean_data(df, test=False):
    df = df.dropna(how='any', axis='rows')
    df = df[(df.dropoff_latitude != 0) | (df.dropoff_longitude != 0)]
    df = df[(df.pickup_latitude != 0) | (df.pickup_longitude != 0)]
    if "fare_amount" in list(df):
        df = df[df.fare_amount.between(0, 4000)]
    df = df[df.passenger_count < 8]
    df = df[df.passenger_count >= 0]
    df = df[df["pickup_latitude"].between(left=40, right=42)]
    df = df[df["pickup_longitude"].between(left=-74.3, right=-72.9)]
    df = df[df["dropoff_latitude"].between(left=40, right=42)]
    df = df[df["dropoff_longitude"].between(left=-74, right=-72.9)]
    return df'''


get_data(nrows=50)

#if __name__ == '__main__':
    #df = get_data()
