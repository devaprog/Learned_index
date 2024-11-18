# Example traditional query
traditional_query = "SELECT * FROM Order_Items WHERE Unit_Price > 200;"
_, traditional_time = measure_query_execution_time(traditional_query)

# Example learned index query
learned_key = 200
_, learned_time = learned_index_query_with_timing(learned_key, data)

# Compare the execution times
print(f"Traditional Indexing Time: {traditional_time:.6f} seconds")
print(f"Learned Indexing Time: {learned_time:.6f} seconds")

if learned_time < traditional_time:
	print("Learned indexing is faster!")
else:
	print("Traditional indexing is faster!")


