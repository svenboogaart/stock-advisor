import datetime
from typing import List

from interfaces.stock_reader import StockReader
from models.stock import Stock
from models.stock_day import StockDay


class JSONStockReader(StockReader):
    def get_stocks(self, input_data) -> List[Stock]:
        """
        Converts a JSON-like list of stocks and their days into Stock objects.

        Example input_data format:
        [
            {
                "name": "Test Stock",
                "ticker": "TST",
                "stock_days": [
                    {"open_price": 100.5, "close_price": 105.2, "date": "2023-01-01"},
                    {"open_price": 105.2, "close_price": 110.0, "date": "2023-01-02"}
                ]
            }
        ]

        Args:
            input_data (list): A list of dictionaries representing stocks.

        Returns:
            List[Stock]: A list of Stock objects.
        """
        stocks = []
        for stock_data in input_data:
            stock = Stock(stock_data["name"], stock_data["ticker"])
            for day_data in stock_data.get("stock_days", []):
                stock_day = StockDay(
                    open_price=day_data["open_price"],
                    close_price=day_data["close_price"],
                    date=datetime.datetime.strptime(day_data["date"], "%Y-%m-%d")
                )
                stock.add_stock_day(stock_day)
            stocks.append(stock)
        return stocks