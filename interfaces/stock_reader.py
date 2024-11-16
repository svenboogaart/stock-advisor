from abc import ABC, abstractmethod
from typing import List
from models.stock import Stock


class StockReader(ABC):
    @abstractmethod
    def get_stock(self, ticker: str) -> Stock:
        """
        Fetch historical stock data for a given ticker from a data source.

        Args:
            ticker (str): The stock ticker symbol (e.g., "AAPL", "MSFT").

        Returns:
            Stock: A Stock object with historical StockDay data for the given ticker.
        """
        pass