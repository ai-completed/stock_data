
import requests
import json

def fetch_options_data(symbol):
    """
    Fetch options data for a given symbol using the Yahoo Finance API.
    Args:
        symbol (str): Stock symbol to fetch options for
    Returns:
        dict: Options data including calls and puts
    """
    url = f'https://query2.finance.yahoo.com/v7/finance/options/{symbol}'
    response = requests.get(url)
    options_data = response.json()
    
    # Parsing options data
    calls_data = options_data['optionChain']['result'][0]['options'][0]['calls']
    puts_data = options_data['optionChain']['result'][0]['options'][0]['puts']
    
    return {'calls': calls_data, 'puts': puts_data}

# Example usage
if __name__ == '__main__':
    symbol = 'AAPL'
    options_data = fetch_options_data(symbol)
    print('Calls:', options_data['calls'])
    print('Puts:', options_data['puts'])
