def print_natural_numbers(n):
  if (n == 0):
    return
  else:
    print_natural_numbers(n -1)
    print(n)

print_natural_numbers(50)