from flask_swagger_ui import get_swaggerui_blueprint


LOGS_LOCATION = 'data/access.log'
_VERSION = 1  # API version


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'https://gist.githubusercontent.com/ericson-cepeda/a021d286a302b371a635a1f2937ce651/raw/0b9da16e57e276e0fceac93d0e386d14ec7b4cd7/logs_traverser_api.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

request_params = {
    #'code': 10
}