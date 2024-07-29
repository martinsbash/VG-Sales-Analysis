# Video Game Sales Analysis

This project analyzes video game sales data using both SQL and Pandas in Python. It compares average global sales before and after 2005 using two different methods

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes. For deployment instructions, refer to the Deployment section

## Project Description

The Python script in this repository performs the following tasks:
- Loads video game sales data from a CSV file
- Inserts the data into a MySQL database
- Adds a new column to categorize games as pre-2005 or post-2005
- Calculates average global sales for both periods using SQL and Pandas
- Compares the results from both methods

## Prerequisites

To run this project, you need the following software installed:

- Python software
- Pandas library
- SQLAlchemy library
- MySQL Connector for Python
- A MySQL server with a database named `sales_db'

## Installation

Follow these steps to get your development environment up and running:

1. **Download the Project Files**: Download the project files directly from the repository.
2. **Navigate to the Project Directory**: cd path/to/your/project
3. **Install Required Python Packages**: pip install pandas sqlalchemy mysql-connector-python
4. **Prepare the MySQL Database**: Ensure you have a MySQL database named `sales_db` set up and ready for use.
5. **Update the File Path**: Modify the file path in the script to point to your local CSV file containing the video game sales data.
6. **Run the Analysis Script**: python vgsales_analysis.py 
This will execute the script and output the average global sales before and after 2005.

## Running the Tests
To verify the functionality of the script, you can run the following automated tests:

### End-to-End Tests

These tests ensure that the data is correctly inserted into the MySQL database and that the average global sales calculations are accurate.

- **Example**: Run the script to see the output of average global sales: python vgsales_analysis.py

### Breakdown of Tests

1. The script inserts video game sales data from a CSV file into a MySQL table.
2. It adds a new column to categorize the games as 'pre-2005' or 'post-2005'.
3. The script calculates average global sales for both periods using SQL queries.
4. It performs the same calculations using Pandas for comparison.
5. Results from both SQL and Pandas are printed to the console.

## Deployment

For deploying this project on a live system, ensure that:

- Your MySQL server is operational.
- The `sales_db` database is created.
- Update the database connection string in the script with your MySQL credentials.

## Built With

- **Pandas** - For data manipulation and analysis.
- **SQLAlchemy** - For database interaction using Python.
- **MySQL Connector** - To connect Python with MySQL.

## Author

[Martins Bash 1oo890325]

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://license.md/licenses/mit-license/)) file for details.

## Acknowledgment

- Data source: https://www.kaggle.com/datasets/gregorut/videogamesales
