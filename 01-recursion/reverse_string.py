def reverse_string(str, index=0):
  if (index > len(str) - 1):
    return ""
  else:
    return reverse_string(str, index + 1) + str[index]
  
print(reverse_string("Jeffer"))