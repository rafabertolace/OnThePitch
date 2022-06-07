import joblib
from google.cloud import storage


BUCKET_NAME = 'onthepitch869/'
STORAGE_LOCATION = 'models/onthepitch869_pipeline/model.joblib'


def upload_model_to_gcp():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(STORAGE_LOCATION)
    blob.upload_from_filename('model.joblib')


def save_model(model):
    """Save the model into a .joblib format"""
    joblib.dump(model, 'model.joblib')
    #upload_model_to_gcp()
