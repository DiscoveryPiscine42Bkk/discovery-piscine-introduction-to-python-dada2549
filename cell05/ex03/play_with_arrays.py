original_array = [1, 2, 3, 4, 5, 4, 5]
temp_array = [x + 2 for x in original_array if x + 2 > 5]
new_array = list(set(temp_array))
print("Original array:", original_array)
print("New array (each element +2, >5, no duplicates):", new_array)