from datetime import date, timedelta
import pandas_datareader as web
import yfinance as yf

yf.pdr_override()
format = '%Y-%m-%d'

def getStock(ticker):
  result = {}
  start = date.today()
  end = start + timedelta(days=1)

  df = web.data.get_data_yahoo(ticker + ".SA", start=start, end=end)

  value = "{0:.2f}".format(df['Close'].values[0])

  result['value'] = float(value)
  result['date'] = start.strftime(format)
  result['ticker'] = str(ticker).upper()

  return result
