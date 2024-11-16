# Stock Advisor

## Overview
Stock Advisor is a tool designed to provide insights and information about various stock tickers. It allows you to fetch stock data from different sources, enabling you to make informed investment decisions.

This tool gives you info, like the cheapest day to buy a given ticker, example output:

    {
        "total_weeks_analyzed": 5096,
        "weeks_where_day_was_cheapest": {
            "Friday": 1118,
            "Thursday": 694,
            "Wednesday": 697,
            "Tuesday": 956,
            "Monday": 1631
        }
    }

Here you can see per week, what day the stock was cheapest.
You can also get an overview peer year/week for example, 2024 week 45:

    "2024-W45": {
        "Day-by-Day Overview": {
            "Monday": {
                "Price": 63.36000061035156,
                "Difference from Lowest": 1.6199989318847656
            },
            "Tuesday": {
                "Price": 63.20000076293945,
                "Difference from Lowest": 1.4599990844726562
            },
            "Wednesday": {
                "Price": 63.0,
                "Difference from Lowest": 1.2599983215332031
            },
            "Thursday": {
                "Price": 62.54999923706055,
                "Difference from Lowest": 0.80999755859375
            },
            "Friday": {
                "Price": 61.7400016784668,
                "Difference from Lowest": 0.0
            }
        },
        "Average Price": 62.77000045776367,
        "Average Difference from Lowest": 1.029998779296875,
        "Lowest Day": "Friday",
        "Lowest Price": 61.7400016784668,
        "Highest Day": "Monday",
        "Highest Price": 63.36000061035156
    }


  
## Using the stock advisor
To get started with Stock Advisor, specify the stock ticker symbol and the desired reader option. The default settings will use the S&P 500 ticker symbol with the Yahoo reader.

### Install Dependencies
Make sure you have python 3.x, else you will need to install python first.

`python --version`

Install the requirements.

`pip install -r requirements.txt`

### run the script
This section provides information on the command-line arguments available for this Python script. These arguments allow you to customize the behavior of the script when it is executed.
Basic example without any parameters:

`python stock_advisor.py`
### Arguments

#### `--ticker`
- **Type:** `str`
- **Default:** `^GSPC` (S&P 500)
- **Help:** Specify the stock ticker symbol for which you want to retrieve data. If not provided, the script defaults to the S&P 500 index (`^GSPC`).

Example Usage:
`python stock_advisor.py --ticker AAPL`

#### `--reader`
- **Type:** `str`
- **Default:** `yahoo`
- **Help:** Select the stock reader source to use for data retrieval. The default value is set to `yahoo`, but you can specify other options based on your preferences or needs.

Example Usage:
`python stock_advisor.py --reader yahoo`

**Note**,
yahoo works without any changes, 
for **alpha_vantage** you will need to add your api key in `/models/stock_readers/alpha_vantage_reader.py`, 
in the line `API_KEY = "YOUR_KEY_HERE"`

#### `--when`
- **Type:** `str`
- **Default:** `close`
- **Help:** Indicate whether to calculate values for the market open or close price. The default setting is to retrieve data at the market close. You can specify "open" if you want data for the opening price.

Example Usage:
`python stock_advisor.py --when open`

### Full Command Example

Here’s how you can combine these arguments in a single command:

`python stock_advisor.py --ticker MSFT --reader yahoo --when open`

This command analyzes the Microsoft (MSFT) ticker using the Yahoo stock reader.

## Contribution
Feel free to extend or improve the existing functionality. Contributions to this project are welcome!

### License
This project is licensed under the Apache Version 2.0 License.
