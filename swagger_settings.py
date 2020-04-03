

def set_config(app):
    app.config["API_HOST"] = "covid19-japan-web-api.now.sh"
    app.config["API_BASEPATH"] = ""
    app.config["API_SCHEMES"] = ["https"]
    app.config["API_VERSION"] = "0.1.0"
    app.config["API_TITLE"] = "COVID19 Japan Web API"
    app.config["API_DESCRIPTION"] = "Web API to get COVID-19(coronavirus) information of each prefecture in Japan"
    app.config["API_TERMS_OF_SERVICE"] = "https://github.com/ryo-ma/covid19-japan-web-api/blob/master/README.md"
    app.config["API_CONTACT_EMAIL"] = "saka_ro@yahoo.co.jp"
    app.config["API_LICENSE_NAME"] = "MIT"
    app.config["API_LICENSE_URL"] = "https://github.com/ryo-ma/covid19-japan-web-api/blob/master/LICENSE"
    app.config['CORS_AUTOMATIC_OPTIONS'] = True
