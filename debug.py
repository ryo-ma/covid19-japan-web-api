from index import app
from swagger_settings import set_config
from sanic_openapi import swagger_blueprint


if __name__ == '__main__':
    app.blueprint(swagger_blueprint)
    set_config(app)
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
