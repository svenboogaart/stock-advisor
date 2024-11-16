import unittest
import datetime

from models.stock_day import StockDay


class TestStockDay(unittest.TestCase):

    def setUp(self):
        """Create a StockDay instance for use in the tests"""
        self.test_date = datetime.datetime(2023, 10, 1)  # A sample date
        self.stock_day = StockDay(open_price=100.50, close_price=105.75, date=self.test_date)

    def test_initialization(self):
        """Test that the StockDay object is correctly initialized"""
        self.assertEqual(self.stock_day.open_price, 100.50)
        self.assertEqual(self.stock_day.close_price, 105.75)
        self.assertEqual(self.stock_day.date, self.test_date)

    def test_open_price_type(self):
        """Test that the open_price is a float"""
        self.assertIsInstance(self.stock_day.open_price, float)

    def test_close_price_type(self):
        """Test that the close_price is a float"""
        self.assertIsInstance(self.stock_day.close_price, float)

    def test_date_type(self):
        """Test that the date is of type datetime.datetime"""
        self.assertIsInstance(self.stock_day.date, datetime.datetime)

    def test_invalid_date(self):
        """Test that the date cannot be set to an invalid type"""
        with self.assertRaises(TypeError):
            # Pass an invalid type (e.g., a string instead of datetime)
            StockDay(open_price=100.50, close_price=105.75, date="invalid-date")

    def test_invalid_open_price(self):
        """Test that the open_price must be a float"""
        with self.assertRaises(TypeError):
            StockDay(open_price="100.50", close_price=105.75, date=self.test_date)

    def test_invalid_close_price(self):
        """Test that the close_price must be a float"""
        with self.assertRaises(TypeError):
            StockDay(open_price=100.50, close_price="105.75", date=self.test_date)


if __name__ == '__main__':
    unittest.main()
