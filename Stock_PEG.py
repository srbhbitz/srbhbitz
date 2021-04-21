import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials
def pegRatio(tickerName):
    yahoo_financials = YahooFinancials(tickerName)
    stocs_stats_data = yahoo_financials.get_key_statistics_data()
    print(stocs_stats_data[tickerName]['pegRatio'])
    return

if __name__ == "__main__":
    stock_ticket = input("Ticker Symbol with suffix after dot(.) if not of NYSE and NASDAQ , e.g. AC.TO, TYT.L: \n")
    pegRatio(stock_ticket)
