import requests
import json

def fetch_ohlcv():
    
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR/history?period_id=1HRS&time_start=2012-01-01T00:00:00&time_end=2023-08-27T00:00:00"
    #url = "https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_EUR_BTC/history?period_id=1MTH&time_start=2012-03-01T00:00:00"
    headers = { "X-CoinAPI-Key": "ad32a6ea-1eb1-446d-bf72-6057abdc0b74" }  # Replace with your API key
 
    response = requests.get(url, headers=headers)
 
    # Check if the response is successful
    if response.status_code == 200:
        if response.content:
            return response.json()
        else:
            print("Response is empty.")
            return None
    else:
        # Handle other HTTP status codes
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

with open('BTCEUR-1h.json', 'w') as f:
    json.dump(fetch_ohlcv(), f)

print("im duone")
