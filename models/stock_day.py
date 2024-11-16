import datetime


class StockDay:
    def __init__(self, open_price: float, close_price: float, date: datetime.datetime):
        # Type checking
        if not isinstance(open_price, (int, float)):
            raise TypeError(f"Expected float for open_price, got {type(open_price).__name__}")
        if not isinstance(close_price, (int, float)):
            raise TypeError(f"Expected float for close_price, got {type(close_price).__name__}")
        if not isinstance(date, datetime.datetime):
            raise TypeError(f"Expected datetime for date, got {type(date).__name__}")


        self.open_price = open_price  # Store as float
        self.close_price = close_price  # Store as float
        self.date = date
