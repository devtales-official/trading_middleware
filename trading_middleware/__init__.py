import os

from flask import Flask, jsonify
from binance.cm_futures import CMFutures


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'trading_middleware.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

# a simple page that says hello
@app.route('/indicatorAlert', methods=['POST'])
def indicatorAlert():

    cm_futures_client = CMFutures()

    # get server time
    print(cm_futures_client.time())

    cm_futures_client = CMFutures(key=os.getenv('BINANCE_KEY'), secret=os.getenv('BINANCE_SECRET'))

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

