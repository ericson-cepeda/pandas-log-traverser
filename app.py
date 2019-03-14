import os
import logging
from flask import Flask, jsonify, request

from settings.base import SWAGGER_URL,swaggerui_blueprint, request_params
from helpers.controllers import find_by, get_groups


app = Flask(__name__)


@app.route('/')
def main():
    return jsonify(
        {"message": "OK"}
    )


@app.route('/v1/log/findBy/<string:attr_type>/limit/<int:limit>')
def find_by_type(attr_type, limit):
    return jsonify(
        {'results': find_by(attr_type, request.args.get('val'), limit=request_params.get(attr_type, limit)).to_dict(orient='records')}
    )


@app.route('/v1/log/findBy/host/group/<string:attr_col>')
def find_requests_by_host(attr_col):
    attr_type = 'host'
    return jsonify(
        get_groups(attr_col, attr_type, request.args.get('val'))
    )


if __name__ == '__main__':
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)