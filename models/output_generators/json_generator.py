import json
import re

from models.stock_advisor import StockAdvisor


class JsonGenerator:
    def __init__(self, stock):
        self.stock = stock

    def sanitize_filename(self, stock_ticker, stock_name):
        """
        Sanitize the filename to ensure it's valid by keeping only alphanumeric characters and underscores.
        The filename will not end with an underscore, and .json will be appended.
        Double underscores will be collapsed into a single underscore.

        Args:
            stock_ticker (str): The stock ticker.
            stock_name (str): The stock name.

        Returns:
            str: The sanitized filename with .json extension.
        """
        # Create the initial filename string
        filename = f"weekly_cheapest_day_overview_{stock_ticker}_{stock_name}"

        # Replace all non-alphanumeric characters (except underscores) with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', filename)

        # Collapse consecutive underscores into a single underscore
        sanitized = re.sub(r'_{2,}', '_', sanitized)

        # Remove trailing underscores (if any)
        sanitized = sanitized.rstrip('_')

        # Append the .json extension
        sanitized_filename = sanitized + '.json'

        return sanitized_filename

    def write_to_json(self, data, filepath):
        """
        Writes the provided data to a JSON file.

        Args:
            data (dict): The data to write to the file.
            filepath (str): The destination filepath.
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data successfully written to {filepath}")
        except Exception as e:
            print(f"Error writing to JSON: {e}")

    def write_cheapest_day_overview_to_json(self, advisor: StockAdvisor, filepath=None):
        """
        Write the weekly cheapest day overview to a JSON file.

        Args:
            advisor (StockAdvisor): The advisor instance that contains the analyzed data.
            filepath (str): The file path to write the JSON data to.
                             If not provided, a default filename based on the stock's ticker and name will be used.
        """
        try:
            # Generate default filename based on stock's ticker and name if filepath is None
            if filepath is None:
                stock_ticker = self.stock.ticker
                stock_name = self.stock.name
                sanitized_filename = self.sanitize_filename(stock_name, stock_ticker)

                # Debug: Check sanitized filename
                print(f"Sanitized filename: {sanitized_filename}")

                filepath = sanitized_filename  # Assign the sanitized filename to filepath

            # Get cheapest day overview from the advisor
            overview = advisor.get_cheapest_day_overview()

            # Write the data to the JSON file
            self.write_to_json(overview, filepath)
        except Exception as e:
            print(f"Error writing to JSON: {e}")
