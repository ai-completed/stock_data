
# Automated Options Trading Project Documentation

## Overview

This project aims to automate the trading of stocks and options by fetching data, analyzing trends, and making decisions based on predefined criteria.

## Structure

- **/data**: Contains raw and processed data for stocks and options.
- **/scripts**: Includes scripts to fetch and analyze data.
- **/outputs**: Stores results and reports generated by scripts.
- **/docs**: Documentation of the project.

## Scripts Description

- `fetch_stock_data.py`: Fetches historical stock data from Alpha Vantage.
- `fetch_options_data.py`: Retrieves options data from Yahoo Finance.
- `analysis_tools.py`: Tools for calculating volatility and moving averages.

## Usage

To run the scripts, navigate to the `/scripts` directory and execute the desired script via command line.

## Data Handling

Data fetched by the scripts is processed and stored in `/data/processed_data` for further analysis.

## Outputs

Analysis results and reports are saved in `/outputs` directory.

## Dependencies

- Python 3.8+
- pandas
- requests

## Future Work

Further improvements will include more sophisticated data analysis techniques and real-time data processing capabilities.