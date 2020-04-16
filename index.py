import textwrap
import json
from flask import abort, Flask, Blueprint, jsonify, request
from flask_cors import cross_origin


PREFECTURES_JSON_PATH = './data/created_json/prefectures.json'
TODAY_TOTAL_JSON_PATH = './data/created_json/today_total.json'
HISTORY_TOTAL_JSON_PATH = './data/created_json/history_total.json'
PREDICTION_TOTAL_JSON_PATH = './data/created_json/prediction_total.json'
POSITIVE_DETAIL_JSON_PATH = './data/created_json/positive_detail.json'
STATISTICS_JSON_PATH = './data/created_json/statistics_positive_detail.json'
PREFECTURES = textwrap.dedent('''\
北海道,青森県,岩手県,宮城県,秋田県,山形県,福島県,茨城県,栃木県,群馬県,埼玉県,千葉県,東京都,神奈川県,新潟県,富山県,\
石川県,福井県,山梨県,長野県,岐阜県,静岡県,愛知県,三重県,滋賀県,京都府,大阪府,兵庫県,奈良県,和歌山県,鳥取県,島根県,\
岡山県,広島県,山口県,徳島県,香川県,愛媛県,高知県,福岡県,佐賀県,長崎県,熊本県,大分県,宮崎県,鹿児島県,沖縄県\
''').split(',')

prefectures_json = ''
history_total_json = ''
today_total_json = ''
prediction_total_json = ''
positive_detail_json = ''
statistics_json = ''
with open(PREFECTURES_JSON_PATH) as f:
    prefectures_json = f.read()
with open(HISTORY_TOTAL_JSON_PATH) as f:
    history_total_json = f.read()
with open(TODAY_TOTAL_JSON_PATH) as f:
    today_total_json = f.read()
with open(PREDICTION_TOTAL_JSON_PATH) as f:
    prediction_total_json = f.read()
with open(POSITIVE_DETAIL_JSON_PATH) as f:
    positive_detail_json = f.read()
with open(STATISTICS_JSON_PATH) as f:
    statistics_json = f.read()

app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')


@app.route('/')
def index():
    return jsonify({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/total')
@cross_origin(apiv1)
def total():
    if 'history' in request.args and request.args['history'] == 'true':
        return history_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    elif 'predict' in request.args and request.args['predict'] == 'true':
        return prediction_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    return today_total_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/prefectures')
@cross_origin(apiv1)
def prefectures():
    return prefectures_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/positives')
@cross_origin(apiv1)
def positives():
    if 'prefecture' in request.args:
        prefecture = request.args['prefecture']
        if prefecture in PREFECTURES:
            json_response = [x for x in json.loads(positive_detail_json) if x['prefecture'] == prefecture]
            dumped_response = json.dumps(json_response, indent=2, ensure_ascii=False)
            return dumped_response, 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return abort(404, {'prefecture': f'Does not find {prefecture}'})
    message = 'The prefecture parameter is required.\
    ex: https://covid19-japan-web-api.now.sh/api/v1/positives?prefecture=東京都'
    response_json = json.dumps({'message': message}, ensure_ascii=False)
    return response_json, 400, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/statistics')
@cross_origin(apiv1)
def statistics():
    return statistics_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


app.register_blueprint(apiv1)
