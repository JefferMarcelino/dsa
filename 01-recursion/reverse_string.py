def reverse_string(str):
  result = []

  def helper(index):
    if index < 0:
      return
    
    result.append(str[index])
    helper(index - 1)

  helper(len(str) - 1)
  return "".join(result)
  
print(reverse_string("Jeffer"))