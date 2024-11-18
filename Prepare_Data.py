import pandas as pd

import psycopg2
import pandas as pd

def export_order_items_to_csv():
	try:
    	# Connect to PostgreSQL
    	connection = psycopg2.connect(
        	database="my_database",  # Replace with your database name
        	user="postgres",     	# Replace with your PostgreSQL username
        	password="your_password",# Replace with your PostgreSQL password
        	host="localhost",
        	port="5432"
    	)
    	# Define the query (customize as needed)
    	query = "SELECT Unit_Price, OID FROM Order_Items ORDER BY Unit_Price;"

    	# Fetch data into a DataFrame
    	df = pd.read_sql_query(query, connection)

    	# Save to CSV
    	df.to_csv("order_items.csv", index=False)
    	print("Data exported successfully to 'order_items.csv'")

	except Exception as e:
    	print(f"Error: {e}")
	finally:
    	if connection:
        	connection.close()

# Call the function to export the data
export_order_items_to_csv()
