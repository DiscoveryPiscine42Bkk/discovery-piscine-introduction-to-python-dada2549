original_array = [1, 2, 3, 4, 5]
new_array = [x + 2 for x in original_array if x + 2 > 5]
print("Original array:", original_array)
print("New array (each element +2 and >5):", new_array)