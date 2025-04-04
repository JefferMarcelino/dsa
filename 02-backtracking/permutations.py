def find_permutations(elements):
  result = []

  def backtrack(path, visited):
    if len(path) == len(elements):
      result.append(path.copy())
      return
    
    for i in range(len(elements)):
      if (visited[i]):
        continue

      visited[i] = True
      path.append(elements[i])

      backtrack(path, visited)

      path.pop()
      visited[i] = False
  
  backtrack([], [False] * len(elements))
  return result

print(f"Permutations of [1, 2, 3]: {find_permutations([1, 2, 3])}")
print(f"Permutations of [A, B, C]: {find_permutations(["A", "B", "C"])}")