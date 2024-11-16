import yfinance as yf

from interfaces.stock_reader import StockReader
from models.stock import Stock
from models.stock_day import StockDay
from datetime import datetime
import pandas as pd


class YahooFinanceStockReader(StockReader):
    def get_stock(self, ticker: str) -> Stock:
        """
        Fetch historical stock data for a given ticker from Yahoo Finance and convert it into Stock objects.

        Args:
            ticker (str): The stock ticker symbol (e.g., "AAPL", "MSFT").

        Returns:
            Stock: A Stock object with historical StockDay data for the given ticker.
        """
        # Fetch data from Yahoo Finance
        stock_data = yf.Ticker(ticker)
        historical_data = stock_data.history(period="max")  # Get maximum available historical data

        # Create Stock object
        stock_name = stock_data.info.get("longName", ticker)  # Fallback to ticker if name is not available
        stock = Stock(name=stock_name, ticker=ticker)

        # Iterate through the historical data and create StockDay objects
        for date, row in historical_data.iterrows():
            try:
                processed_date = self._process_date(date)
                stock_day = StockDay(
                    open_price=row["Open"],
                    close_price=row["Close"],
                    date=processed_date
                )
                stock.add_stock_day(stock_day)
            except Exception as e:
                print(f"Error processing row for {date}: {e}")

        return stock

    def _process_date(self, date: pd.Timestamp) -> datetime:
        """
        Helper function to process and convert date formats if needed.

        Args:
            date (pd.Timestamp): The date from Yahoo Finance.

        Returns:
            datetime: The corresponding Python datetime object.
        """
        if isinstance(date, pd.Timestamp):
            return date.to_pydatetime()
        elif isinstance(date, datetime):
            return date
        else:
            raise TypeError(f"Expected pandas.Timestamp or datetime.datetime, got {type(date)}")
