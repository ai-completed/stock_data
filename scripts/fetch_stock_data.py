
import requests
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch historical stock data for a given symbol from Alpha Vantage API.
    Args:
        symbol (str): Stock symbol
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
    Returns:
        DataFrame: Stock data including date, open, high, low, close, volume
    """
    api_key = 'YOUR_API_KEY'
    base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'
    response = requests.get(base_url)
    data = response.json()
    
    # Extracting data
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)
    
    # Filtering based on date
    return df.loc[start_date:end_date]

# Example usage
if __name__ == '__main__':
    symbol = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    stock_data = fetch_stock_data(symbol, start_date, end_date)
    print(stock_data.head())
