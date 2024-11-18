from tensorflow.keras.models import load_model
import time
import pandas as pd

# Load the trained learned index model
model = load_model("learned_index_model.h5")

# Load dataset (order_items.csv) for testing
data = pd.read_csv("order_items.csv")

def learned_index_query_with_timing(key, data):
	try:
    	# Start the timer
    	start_time = time.time()

    	# Predict position using the model
    	position = model.predict([[key]])[0][0]

    	# Find the closest match in the dataset
    	closest_row = data.iloc[(data["Unit_Price"] - key).abs().idxmin()]

    	# End the timer
    	end_time = time.time()

    	# Calculate the time taken
    	execution_time = end_time - start_time
    	print(f"Learned Index Query Time: {execution_time:.6f} seconds")

    	return closest_row, execution_time

	except Exception as e:
    	print(f"Error: {e}")

# Example query using the learned index
key_to_query = 200
result, time_taken = learned_index_query_with_timing(key_to_query, data)
print(f"Closest row returned: {result}")
