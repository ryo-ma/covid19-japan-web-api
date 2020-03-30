from sanic import Blueprint, Sanic
from sanic.response import json

app = Sanic()

apiv1 = Blueprint('apiv1', url_prefix='/api/v1')


@app.route('/')
async def index(request):
    return json({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/total')
async def all(request):
    return json({'result': 'total'})


apiv1.static('/prefectures', './data/created_json/prefectures.json', name='prefectures')


api = Blueprint.group(apiv1)
app.blueprint(api)
