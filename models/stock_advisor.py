from collections import defaultdict

class StockAdvisor:
    def __init__(self, stock, price_type="close"):
        self.stock = stock
        self.set_price_type(price_type)

    def set_price_type(self, price_type):
        if price_type.lower() not in ["open", "close"]:
            raise ValueError("price_type must be either 'open' or 'close'.")
        self.price_type = price_type.lower()

    def get_price(self, stock_day):
        """
        Returns the price for a given stock day, based on the selected price type ('open' or 'close').
        """
        if self.price_type == "open":
            return stock_day.open_price
        elif self.price_type == "close":
            return stock_day.close_price

    def get_cheapest_day_for_week(self, stock_days):
        """
        Determines the cheapest day for a given week based on stock day prices.
        """
        min_price = float('inf')
        cheapest_day = None

        for stock_day in stock_days:
            price = self.get_price(stock_day)
            if price < min_price:
                min_price = price
                cheapest_day = stock_day.date.strftime('%A')

        return cheapest_day, min_price

    def get_day_by_day_overview(self, stock_days, lowest_price):
        """
        Creates a day-by-day overview for a given week, including the price and difference from the lowest price.
        """
        day_overview = {}

        for stock_day in stock_days:
            price = self.get_price(stock_day)
            day_overview[stock_day.date.strftime('%A')] = {
                "Price": price,
                "Difference from Lowest": price - lowest_price
            }

        return day_overview

    def get_weekly_data(self, stock_days):
        """
        Generates data for a single week, including:
        - Day-by-day overview
        - Average price for the week
        - Average difference from the lowest price
        - Lowest day and price
        - Highest day and price
        """
        cheapest_day, lowest_price = self.get_cheapest_day_for_week(stock_days)
        day_overview = self.get_day_by_day_overview(stock_days, lowest_price)

        total_price = sum(self.get_price(stock_day) for stock_day in stock_days)
        average_price = total_price / len(stock_days)

        # Get highest day for the week
        highest_day = max(stock_days, key=lambda sd: self.get_price(sd))
        highest_price = self.get_price(highest_day)

        return {
            "Day-by-Day Overview": day_overview,
            "Average Price": average_price,
            "Average Difference from Lowest": sum(
                (self.get_price(stock_day) - lowest_price) for stock_day in stock_days) / len(stock_days),
            "Lowest Day": cheapest_day,
            "Lowest Price": lowest_price,
            "Highest Day": highest_day.date.strftime('%A'),
            "Highest Price": highest_price
        }

    def get_weekly_overview(self):
        """
        Loops through the grouped stock days and calculates the weekly overview data.
        """
        weekly_overview = {}
        weekly_cheapest_day = defaultdict(int)

        # Get stock days grouped by week
        grouped_by_week = self.stock.get_stock_days_grouped_by_week()

        # Loop over each week and calculate data
        for week, stock_days in grouped_by_week.items():
            weekly_data = self.get_weekly_data(stock_days)

            # Add the weekly data to the overview
            weekly_overview[week] = weekly_data

            # Track the cheapest day per week
            weekly_cheapest_day[weekly_data["Lowest Day"]] += 1

        return weekly_overview, weekly_cheapest_day

    def get_cheapest_day_overview(self):
        """
        Returns the overview of the cheapest days per week, including:
        - Total weeks analyzed
        - Breakdown of how many times each day was the cheapest
        - Weekly overview
        """
        weekly_overview, weekly_cheapest_day = self.get_weekly_overview()

        return {
            "stock":  self.stock.name,
            "ticker": self.stock.ticker,
            "days_analyzed": len(self.stock.stock_days),
            "total_weeks_analyzed": len(weekly_overview),
            "weeks_where_day_was_cheapest": dict(weekly_cheapest_day),
            "weekly_overview": weekly_overview
        }
