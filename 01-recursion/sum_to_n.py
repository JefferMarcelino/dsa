def sum_to_n(n):
  if (n == 1):
    return 1;
  else:
    return n + sum_to_n(n-1)
  
print(sum_to_n(5))