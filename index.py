from sanic import Blueprint, Sanic, response
from sanic.response import json
from sanic_cors import cross_origin
from sanic.exceptions import NotFound
import textwrap


PREFECTURES_JSON_PATH = './data/created_json/prefectures.json'
TODAY_TOTAL_JSON_PATH = './data/created_json/today_total.json'
HISTORY_TOTAL_JSON_PATH = './data/created_json/history_total.json'
POSITIVE_DETAIL_JSON_PATH = './data/created_json/positive_detail.json'
POSITIVE_DETAIL_JSON_PATH_FORMAT = './data/created_json/positive_detail_by_prefecture/{0}.json'
PREFECTURES = textwrap.dedent('''\
北海道,青森県,岩手県,宮城県,秋田県,山形県,福島県,茨城県,栃木県,群馬県,埼玉県,千葉県,東京都,神奈川県,新潟県,富山県,\
石川県,福井県,山梨県,長野県,岐阜県,静岡県,愛知県,三重県,滋賀県,京都府,大阪府,兵庫県,奈良県,和歌山県,鳥取県,島根県,\
岡山県,広島県,山口県,徳島県,香川県,愛媛県,高知県,福岡県,佐賀県,長崎県,熊本県,大分県,宮崎県,鹿児島県,沖縄県\
''').split(',')

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

    if 'prefecture' in request.raw_args:
        prefecture = request.raw_args['prefecture']
        if prefecture in PREFECTURES:
            return await response.file(POSITIVE_DETAIL_JSON_PATH_FORMAT.format(prefecture))
        else:
            raise NotFound('Data not found for the specified prefecture.')
    else:
        return await response.file(POSITIVE_DETAIL_JSON_PATH)


api = Blueprint.group(apiv1)
app.blueprint(api)
