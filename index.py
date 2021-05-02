import json
from flask import abort, Flask, Blueprint, jsonify, request
from flask_cors import cross_origin
from src.data_manager import DataManager
from src.const import PREFECTURES
from src.swagger_settings import set_config


data_manager = DataManager()

app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')


@app.route('/')
def index():
    return jsonify({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/total')
@cross_origin(apiv1)
def total():
    """ Get the total number of infected people and deaths in Japan
    ---
    parameters:
      - in: query
        name: history
        type: boolean
      - in: query
        name: predict
        type: boolean
    responses:
      200:
        description: Success to get total
    """
    if 'history' in request.args and request.args['history'] == 'true':
        return data_manager.history_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    elif 'predict' in request.args and request.args['predict'] == 'true':
        return data_manager.prediction_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    return data_manager.today_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/prefectures')
@cross_origin(apiv1)
def prefectures():
    """Get the COVID-19(coronavirus) information of each prefecture in Japan
    ---
    responses:
      200:
        description: Success to get the information of each prefecture
    """
    return data_manager.prefectures_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/positives')
@cross_origin(apiv1)
def positives():
    """ Get the total number of infected people and deaths in Japan
    ---
    parameters:
      - in: query
        name: prefecture
        description: Specify the Japanese name. example - 千葉県
        type: string
        required: true
    responses:
      200:
        description: Success to get positives
      400:
        description: The prefecture parameter is required
      404:
        description: Does not find the prefecture
    """
    if 'prefecture' in request.args:
        prefecture = request.args['prefecture']
        if prefecture in PREFECTURES:
            return [], 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return abort(404, {'prefecture': f'Does not find {prefecture}'})
    message = 'The prefecture parameter is required.\
    ex: https://covid19-japan-web-api.now.sh/api/v1/positives?prefecture=東京都'
    response_json = json.dumps({'message': message}, ensure_ascii=False)
    return response_json, 400, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/statistics')
@cross_origin(apiv1)
def statistics():
    """Get the COVID-19(coronavirus) statistics of each prefecture in Japan
    ---
    responses:
      200:
        description: Success to get the statistics of each prefecture
    """
    return data_manager.statistics_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


app.register_blueprint(apiv1)
set_config(app)
