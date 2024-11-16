import argparse

from models.output_generators.json_generator import JsonGenerator
from models.stock_advisor import StockAdvisor
from models.stock_readers.yahoo_finance_reader import YahooFinanceStockReader
from models.stock_readers.alpha_vantage_reader import AlphaVantageStockReader


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch stock data and perform analysis.")
    parser.add_argument(
        "--ticker",
        type=str,
        nargs="?",  # Make the ticker argument optional
        default="^GSPC",  # Default to S&P 500 ticker if not provided
        help="The stock ticker symbol (default: '^GSPC' for S&P 500)."
    )
    parser.add_argument(
        "--reader",
        type=str,
        default="yahoo",
        help="The stock reader to use (default: yahoo)."
    )
    parser.add_argument(
        "--when",
        type=str,
        help="Calculate for open or close.",
        default="close"
    )

    # Parse the arguments
    args = parser.parse_args()

    reader = None
    when = "close"

    # Validate the stock reader input
    if args.reader.lower() not in ["yahoo", "alpha_vantage"]:
        print(f"Warning: '{args.reader}' is not a valid stock reader. Falling back to default 'yahoo' reader.")
        reader = YahooFinanceStockReader()  # Default to Yahoo Finance
    elif  args.reader.lower() == "yahoo":
        reader = YahooFinanceStockReader()
    elif args.reader.lower() == "alpha_vantage":
        reader = AlphaVantageStockReader()

    # Validate the stock reader input
    if args.when and args.when.lower() not in ["open", "close"]:
        print(f"Warning: '{args.when}' is not a valid value for when. Falling back to default 'close'.")
    elif args.when.lower() == "open":
        when = "open"


    try:
        # Fetch the stock data using the selected reader
        stock = reader.get_stock(args.ticker)

        # Output the stock data
        print(f"Stock: {stock.name} ({stock.ticker})")
        print("Historical data:")
        for stock_day in stock.stock_days:
            print(f"Date: {stock_day.date}, Open: {stock_day.open_price}, Close: {stock_day.close_price}")

        advisor = StockAdvisor(stock, when)

        # Initialize JsonGenerator for writing JSON data
        json_generator = JsonGenerator(stock)

        # Write the cheapest day overview to a JSON file
        json_generator.write_cheapest_day_overview_to_json(advisor)


    except Exception as e:
        print(f"Error fetching data for ticker {args.ticker}: {e}")


if __name__ == "__main__":
    main()
