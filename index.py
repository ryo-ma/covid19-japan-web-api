from sanic import Blueprint, Sanic, response
from sanic.response import json
from sanic_cors import cross_origin


PREFECTURES_JSON_PATH = './data/created_json/prefectures.json'
TODAY_TOTAL_JSON_PATH = './data/created_json/today_total.json'
HISTORY_TOTAL_JSON_PATH = './data/created_json/history_total.json'
POSITIVE_DETAIL_JSON_PATH = './data/created_json/positive_detail.json'

app = Sanic()

apiv1 = Blueprint('apiv1', url_prefix='/api/v1')


@app.route('/')
async def index(request):
    return json({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/total')
@cross_origin(apiv1)
async def today_total(request):
    if 'history' in request.raw_args and request.raw_args['history'] == 'true':
        return await response.file(HISTORY_TOTAL_JSON_PATH)
    return await response.file(TODAY_TOTAL_JSON_PATH)


@apiv1.route('/prefectures')
@cross_origin(apiv1)
async def prefectures(request):
    return await response.file(PREFECTURES_JSON_PATH)


@apiv1.route('/positives')
@cross_origin(apiv1)
async def positives(request):
    return await response.file(POSITIVE_DETAIL_JSON_PATH)


api = Blueprint.group(apiv1)
app.blueprint(api)
