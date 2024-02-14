import os

from flask import Flask, jsonify
from binance.cm_futures import CMFutures


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'trading_middleware.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/indicatorAlert', methods=['POST'])
    def indicatorAlert():

        cm_futures_client = CMFutures()

        # get server time
        print(cm_futures_client.time())

        cm_futures_client = CMFutures(key='hOlm4fkRkI5gdCsmjXFuVfpOgysT1zIqgfWMNYKR1DceA5EcdDDUg7rAkiOPkhHG', secret='zCHHger4nTRoGUYt7wLaUvMASTf9WyhL5EpGCAJkpvjeKFvICp3u9fZrqh8sE6Z6')

        # Get account information
        print(cm_futures_client.account())


        # Post a new order
        # params = {
        #     'symbol': 'BTCUSDT',
        #     'side': 'SELL',
        #     'type': 'LIMIT',
        #     'timeInForce': 'GTC',
        #     'quantity': 0.002,
        #     'price': 59808
        # }

        # response = cm_futures_client.new_order(**params)
        # print(response)


        return jsonify({})

    return app
