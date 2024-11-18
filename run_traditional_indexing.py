import psycopg2
import time

def measure_query_execution_time(query):
	try:
    	# Connect to PostgreSQL
    	connection = psycopg2.connect(
        	database="my_database",
        	user="postgres",
        	password="your_password",
        	host="localhost",
        	port="5432"
    	)
    	cursor = connection.cursor()

    	# Start the timer
    	start_time = time.time()

    	# Execute the query
    	cursor.execute(query)
    	result = cursor.fetchall()

    	# End the timer
    	end_time = time.time()

    	# Calculate the time taken
    	execution_time = end_time - start_time
    	print(f"Query Execution Time: {execution_time:.6f} seconds")

    	return result, execution_time

	except Exception as e:
    	print(f"Error: {e}")
	finally:
    	if connection:
        	cursor.close()
        	connection.close()

# Example query
query = "SELECT * FROM Order_Items WHERE Unit_Price > 200;"
result, time_taken = measure_query_execution_time(query)
print(f"Number of rows returned: {len(result)}")

