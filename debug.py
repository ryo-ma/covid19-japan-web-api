from index import app
from swagger_settings import set_config

if __name__ == '__main__':
    app.debug = True
    set_config(app)
    app.run(host='0.0.0.0', port=8080)
