import requests
import pandas as pd
import datetime as dt

def extract():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    param = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50, "page": 1
    }
    response = requests.get(url, params=param)
    data = response.json()
    df = pd.DataFrame(data)[
        ['id', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h', 'last_updated']]
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df.insert(len(df.columns), column='extracted_at', value=dt.datetime.now())
    return df



