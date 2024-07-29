import pandas as pd
from sqlalchemy import create_engine, text

# Load the dataset
file_path = 'C:\\Users\\marti\\vgsales.csv'  # Change this to your actual file path
data = pd.read_csv(file_path)

# Establish a connection to the MySQL database using SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:Incorrect2007!@localhost/sales_db')
conn = engine.connect()

# Insert data into MySQL table using SQLAlchemy
data.to_sql('vgsales', con=engine, if_exists='replace', index=False)

# SQL queries executed through Python
# Adding a new column for period (pre-2005, post-2005)
conn.execute(text('ALTER TABLE vgsales ADD COLUMN Period VARCHAR(50)'))
conn.execute(text('''
    UPDATE vgsales 
    SET Period = CASE
        WHEN Year < 2005 THEN 'pre-2005'
        ELSE 'post-2005'
    END
'''))

# Calculate average global sales for pre-2005
avg_pre_2005_sql = conn.execute(text('''
    SELECT AVG(Global_Sales) 
    FROM vgsales 
    WHERE Period = 'pre-2005'
''')).fetchone()[0]

# Calculate average global sales for post-2005
avg_post_2005_sql = conn.execute(text('''
    SELECT AVG(Global_Sales) 
    FROM vgsales 
    WHERE Period = 'post-2005'
''')).fetchone()[0]

# Close the connection
conn.close()

# Using Pandas to perform the same operations
# Creating a new column for period
data['Period'] = data['Year'].apply(lambda x: 'pre-2005' if x < 2005 else 'post-2005')

# Calculate average global sales before and after 2005
avg_global_sales_pre_2005_pandas = data[data['Period'] == 'pre-2005']['Global_Sales'].mean()
avg_global_sales_post_2005_pandas = data[data['Period'] == 'post-2005']['Global_Sales'].mean()

# Print the results from both MySQL and Pandas
print("Average global sales before 2005 (SQL):", avg_pre_2005_sql)
print("Average global sales after 2005 (SQL):", avg_post_2005_sql)
print("Average global sales before 2005 (Pandas):", avg_global_sales_pre_2005_pandas)
print("Average global sales after 2005 (Pandas):", avg_global_sales_post_2005_pandas)
