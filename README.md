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

  

## Inputs

### `--ticker`
- **Description**: The stock ticker symbol that you want to analyze.
- **Default Value**: `GSPC` (for S&P 500)

### `--reader`
- **Description**: The stock reader to use for fetching information from a data source. You can choose from several implemented options, or extend the functionality as needed.
- **Default Value**: `yahoo`
- **Valid Options**: 
  - `yahoo`
  - `alpha_vantage`
  
## Getting Started
To get started with Stock Advisor, specify the stock ticker symbol and the desired reader option. The default settings will use the S&P 500 ticker symbol with the Yahoo reader.

## Examples
```bash
# Using the default settings
python stock_advisor.py

# Specifying a different ticker
python stock_advisor.py --ticker AAPL

# Using alpha_vantage as the reader
python stock_advisor.py --ticker AAPL --reader alpha_vantage
```

## Contribution
Feel free to extend the reader options or improve the existing functionality. Contributions to this project are welcome!

### License
This project is licensed under the MIT License.

`You can modify any sections and add further details as per your project needs!`