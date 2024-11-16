import requests

from interfaces.stock_reader import StockReader
from models.stock import Stock
from models.stock_day import StockDay
from datetime import datetime


class AlphaVantageStockReader(StockReader):
    API_KEY = "your_alpha_vantage_api_key"  # Replace with your own Alpha Vantage API key

    def get_stock(self, ticker: str) -> Stock:
        """
        Fetch historical stock data for a given ticker from Alpha Vantage and convert it into Stock objects.

        Args:
            ticker (str): The stock ticker symbol (e.g., "AAPL", "MSFT").

        Returns:
            Stock: A Stock object with historical StockDay data for the given ticker.
        """
        url = f'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': ticker,
            'apikey': self.API_KEY,
            'outputsize': 'full'  # Get the full data (or 'compact' for last 100 days)
        }

        # Fetch data from Alpha Vantage
        response = requests.get(url, params=params)
        data = response.json()

        if "Time Series (Daily)" not in data:
            raise ValueError(f"Error fetching data for {ticker}. Response: {data}")

        # Create Stock object
        stock = Stock(name=ticker, ticker=ticker)

        # Iterate through the historical data and create StockDay objects
        for date_str, day_data in data["Time Series (Daily)"].items():
            try:
                processed_date = datetime.strptime(date_str, "%Y-%m-%d")
                stock_day = StockDay(
                    open_price=float(day_data["1. open"]),
                    close_price=float(day_data["4. close"]),
                    date=processed_date
                )
                stock.add_stock_day(stock_day)
            except Exception as e:
                print(f"Error processing row for {date_str}: {e}")

        return stock
