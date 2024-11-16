import datetime
import unittest

from models.stock import Stock
from models.stock_day import StockDay


class TestStock(unittest.TestCase):
    def test_stock_initialization(self):
        """Test valid initialization of Stock."""
        stock = Stock("Test Stock", "TST")
        self.assertEqual(stock.name, "Test Stock")
        self.assertEqual(stock.ticker, "TST")
        self.assertEqual(stock.stock_days, [])

    def test_add_stock_day(self):
        """Test adding a StockDay to Stock."""
        stock = Stock("Test Stock", "TST")
        stock_day = StockDay(100.5, 105.2, datetime.datetime(2023, 1, 1))
        stock.add_stock_day(stock_day)
        self.assertEqual(len(stock.stock_days), 1)
        self.assertIs(stock.stock_days[0], stock_day)

    def test_add_multiple_stock_days(self):
        """Test adding multiple StockDays to Stock."""
        stock = Stock("Test Stock", "TST")
        stock_day1 = StockDay(100.5, 105.2, datetime.datetime(2023, 1, 1))
        stock_day2 = StockDay(105.2, 110.0, datetime.datetime(2023, 1, 2))
        stock.add_stock_day(stock_day1)
        stock.add_stock_day(stock_day2)
        self.assertEqual(len(stock.stock_days), 2)
        self.assertIs(stock.stock_days[0], stock_day1)
        self.assertIs(stock.stock_days[1], stock_day2)

    def test_delete_stock_day(self):
        """Test deleting a StockDay from Stock."""
        stock = Stock("Test Stock", "TST")
        stock_day1 = StockDay(100.5, 105.2, datetime.datetime(2023, 1, 1))
        stock_day2 = StockDay(105.2, 110.0, datetime.datetime(2023, 1, 2))
        stock.add_stock_day(stock_day1)
        stock.add_stock_day(stock_day2)

        stock.delete_stock_day(stock_day1)
        self.assertEqual(len(stock.stock_days), 1)
        self.assertIs(stock.stock_days[0], stock_day2)

    def test_delete_stock_day_not_in_list(self):
        """Test deleting a StockDay that is not in Stock."""
        stock = Stock("Test Stock", "TST")
        stock_day1 = StockDay(100.5, 105.2, datetime.datetime(2023, 1, 1))
        stock_day2 = StockDay(105.2, 110.0, datetime.datetime(2023, 1, 2))
        stock.add_stock_day(stock_day1)

        with self.assertRaises(ValueError):
            stock.delete_stock_day(stock_day2)