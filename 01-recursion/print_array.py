def print_array(array, index=0):
  if (index > len(array) -1):
    print()
  else:
    print(array[index], end=" ")
    print_array(array, index + 1)

print_array([1, 2, 3, 4, 5, 6, 10])