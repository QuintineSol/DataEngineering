import logging
import os

from flask import jsonify
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics
from sklearn.model_selection import train_test_split
import joblib


def train(dataset):
    # split into input (X) and output (Y) variables
    X = dataset[:, 0:6]
    Y = dataset[:, 6]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    # define model
    model = GradientBoostingRegressor()
    # Fit the model
    model.fit(X_train, Y_train)
    # predict values
    Y_pred = model.predict(X_test)
    # evaluate the model
    scores_1 = metrics.r2_score(Y_test, Y_pred)
    scores_2 = metrics.mean_absolute_error(Y_test, Y_pred)
    text_out = {
        "R^2": scores_1,
        "Mean absolute error": scores_2,
    }
    logging.info(text_out)
    # Saving model in a given location provided as an env. variable
    model_repo = os.environ['MODEL_REPO']
    if model_repo:
        file_path = os.path.join(model_repo, "insurance_pred")
        joblib.dump(model, file_path)
        logging.info("Saved the model to the location : " + model_repo)
        return jsonify(text_out), 200
    else:
        joblib.dump(model, file_path)
        return jsonify({'message': 'The model was saved locally.'}), 200