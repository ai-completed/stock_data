
import pandas as pd

def calculate_volatility(data):
    """
    Calculate the historical volatility of stock prices.
    Args:
        data (DataFrame): DataFrame containing stock prices with a 'Close' column.
    Returns:
        float: The calculated historical volatility.
    """
    # Daily returns
    daily_returns = data['Close'].pct_change()
    
    # Standard deviation of daily returns (annualized)
    volatility = daily_returns.std() * (252**0.5)  # Annualizing the volatility
    return volatility

def moving_average(data, window_size):
    """
    Calculate the moving average of stock prices.
    Args:
        data (DataFrame): DataFrame containing stock prices with a 'Close' column.
        window_size (int): The number of days over which to calculate the moving average.
    Returns:
        DataFrame: The moving averages appended as a new column.
    """
    data['Moving Average'] = data['Close'].rolling(window=window_size).mean()
    return data

# Example usage
if __name__ == '__main__':
    # Assuming data is a DataFrame loaded elsewhere in your project
    data = pd.DataFrame({
        'Close': [150, 152, 148, 149, 153, 157, 155, 158, 162, 160]
    })
    print('Volatility:', calculate_volatility(data))
    print('Moving Average (5 days):\n', moving_average(data, 5))
