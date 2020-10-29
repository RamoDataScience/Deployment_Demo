from flask import Blueprint, request, render_template, jsonify
from classification_model.predict import make_prediction
from classification_model import __version__ as _version
from classification_model.config import config
import pandas as pd
import numpy as np
import json


from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/')
def home():
    return render_template("index3.html")


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version, 'api_version': api_version})


@prediction_app.route('/v1/predict/classification', methods=['POST'])
def predicttest():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data, label='test')

        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})


#To use the predict button in our web-app
@prediction_app.route('/predict', methods=['POST'])
def predict():
    # Step 1: Reads the input from our ‘index.html’
    features = [x for x in request.form.values()]

    # Step 2: Convert the list to json object
    json_data = pd.DataFrame(np.array(features).reshape(1, len(config.FEATURES)), columns=config.FEATURES).to_json(orient='records')
    _logger.debug(f'Inputs: {json_data}')

    # Step 3: Validate the input using marshmallow schema
    input_data, errors = validate_inputs(input_data=json.loads(json_data), label='api')

    # Step 4: Model prediction
    result = make_prediction(input_data=input_data)
    _logger.debug(f'Outputs: {result}')

    # Step 5: Convert numpy ndarray to list
    predictions = result.get('predictions').tolist()

    if predictions[0] == 0:
        predicted_value = 'good customer'
    else:
        predicted_value = 'bad costumer'

    # Step 6: Rendering results on HTML GUI
    return render_template('index2.html', prediction_text=f'Our client is a {predicted_value}')

# return render_template('index1.html', predicted_value=f'Our client is a {predicted_value}')