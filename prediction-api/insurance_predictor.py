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
        blob.download_to_filename('local_insurance_pred')
        self.model = joblib.load('local_insurance_pred')
        return jsonify({'message': " the model was downloaded"}), 200

    def predict_single_record(self, prediction_input):
        logging.debug(prediction_input)
        if self.model is None:
            try:
                self.download_model()
                # model_repo = os.environ['MODEL_REPO']
                # file_path = os.path.join(model_repo, "insurance_pred")
                # self.model = joblib.load(file_path)
            except KeyError:
                print("MODEL_REPO is undefined")
                self.model = joblib.load('insurance_pred')
                # self.model = load_model('insurance_pred')

        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        y_pred = self.model.predict(df)
        logging.info(y_pred[0])
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(y_pred[0])}), 200