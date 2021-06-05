from binance.client import Client
import binance.enums
import auth_config
import csv

client = Client(auth_config.API_KEY, auth_config.API_SECRET)
start_date = "1 Jan, 2015"
end_date = "6 Jun, 2021"
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, start_date, end_date)

with open('15m_BTCUSDT_01-01-15_to_06-06-21.csv','w', newline='') as candlehist:
    candlewriter = csv.writer(candlehist, delimiter = ',')
    for candle in klines:
        candlewriter.writerow(candle)



