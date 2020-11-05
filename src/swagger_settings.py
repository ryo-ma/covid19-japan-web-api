from flasgger import Swagger


def set_config(app):
    """
    Sets the application configuration.

    Args:
        app: (todo): write your description
    """
    template = {
        "swagger": "2.0",
        "info": {
            "title": "COVID19 Japan Web API",
            "version": "0.1.0",
            "description": "Web API to get COVID-19(coronavirus) information of each prefecture in Japan",
            "termsOfService": "https://github.com/ryo-ma/covid19-japan-web-api/blob/master/README.md",
            "contact": {
                "email": "saka_ro@yahoo.co.jp"
            },
            "license": {
                "name": "MIT",
                "url": "https://github.com/ryo-ma/covid19-japan-web-api/blob/master/LICENSE"
            }
        },
        "host": "covid19-japan-web-api.now.sh",
        "basePath": "",
        "schemes": [
            "https"
        ]
    }
    Swagger(app, template=template)
