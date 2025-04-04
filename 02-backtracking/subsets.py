def generate_subsets(elements):
  result = []

  def backtrack(current_subset, index):
    result.append(current_subset.copy())

    if (index == len(elements)):
      return
    
    for i in range(index, len(elements)):
      current_subset.append(elements[i])
      backtrack(current_subset, i + 1)
      current_subset.pop()

  backtrack([], 0)
  return result

print(f"Subsets of [1, 2, 3]: {generate_subsets([1, 2, 3])}")