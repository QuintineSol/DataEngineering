import json
import os

import pandas as pd
from flask import jsonify
from keras.models import load_model
import logging
from io import StringIO
import joblib
from google.cloud import storage
from keras.models import load_model


class InsurancePredictor:
    def __init__(self):
        self.model = None

    # download the model
    def download_model(self):
        project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
        model_repo = os.environ.get('MODEL_REPO', 'Specified environment variable is not set.')
        model_name = os.environ.get('MODEL_NAME', 'Specified environment variable is not set.')
        client = storage.Client(project=project_id)
        bucket = client.bucket(model_repo)
        blob = bucket.blob(model_name)
        blob.download_to_filename('local_insurance_model')
        self.model = joblib.load('local_insurance_model')
        return jsonify({'message': " the model was downloaded"}), 200

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        if self.model is None:
            self.download_model()

        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        print(df)
        y_pred = self.model.predict(df)
        print(y_pred[0])
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(y_pred[0])}), 200