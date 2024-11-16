from models.stock_day import StockDay
from collections import defaultdict

class Stock(object):
    def __init__(self,
                name: str,
                ticker: str):
        self.name = name
        self.ticker = ticker
        self.stock_days = []

    def add_stock_day(self, stock_day: StockDay):
        self.stock_days.append(stock_day)

    def delete_stock_day(self, stock_day: StockDay):
        """Remove a specific StockDay from the stock_days list."""
        if stock_day in self.stock_days:
            self.stock_days.remove(stock_day)
        else:
            raise ValueError("The specified StockDay is not in the list.")

    def get_stock_days_grouped_by_week(self):
        """
        Groups stock days by week (using ISO week format YYYY-Www).

        Returns:
            dict: A dictionary where the key is a week identifier (e.g., "2024-W44")
                  and the value is a list of StockDay objects for that week.
        """
        grouped_by_week = defaultdict(list)

        for stock_day in self.stock_days:
            # Get the week in 'YYYY-Www' format
            week = stock_day.date.strftime('%Y-W%U')  # '%Y-W%U' gives us a string like "2024-W44"

            # Group by this week
            grouped_by_week[week].append(stock_day)

        return grouped_by_week


