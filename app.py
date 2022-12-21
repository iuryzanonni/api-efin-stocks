from flask import Flask
from flask_restful import Resource, Api

import stock as stock

app = Flask(__name__)
api = Api(app)

@app.route('/stocks/<string:ticker>', methods=['GET'])
def get_stock(ticker):
  return stock.getStock(ticker)

if __name__ == '__main__':
  app.run()