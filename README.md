# Video Game Sales Analysis

This project analyzes video game sales data using both SQL and Pandas in Python. It compares average global sales before and after 2005 using two different methods

## Getting Started

## Project Description

The Python script in this repository performs the following tasks:
- Loads video game sales data from a CSV file
- Inserts the data into a MySQL database
- Adds a new column to categorize games as pre-2005 or post-2005
- Calculates average global sales for both periods using SQL and Pandas
- Compares the results from both methods

## Prerequisites

- Python 3.x
- pandas
- SQLAlchemy
- MySQL Connector for Python

## Installation

1. Clone this repository: https://github.com/martinsbash/vgsales-analysis.git
2. Navigate into the project directory: cd vgsales-analysis
3. Install required Python packages: pip install pandas sqlalchemy mysql-connector-python
4. Ensure that you have a MySQL database named 'sales_db' created and ready for use.

## Running the Tests

### Breakdown of Tests

1. The script inserts video game sales data from a CSV file into a MySQL table.
2. It adds a new column to categorize the games as 'pre-2005' or 'post-2005'.
3. The script calculates average global sales for both periods using SQL queries.
4. It performs the same calculations using Pandas for comparison.
5. Results from both SQL and Pandas are printed to the console.

## Deployment

To deploy this project, ensure that your MySQL server is running and that the database 'sales_db' is created. Update the database connection string in the script with your MySQL credentials and run the script using: python vgsales_analysis.py

## Author

[Martins Bash 1oo890325]

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgment

- Data source: [dc.connect]
