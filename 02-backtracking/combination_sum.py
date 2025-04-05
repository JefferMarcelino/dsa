def combination_sum(nums, target):
  result = []

  def backtrack(start, current_path, current_total):
    if current_total == target:
      result.append(current_path.copy())
      return
    
    if current_total > target:
      return

    for i in range(start, len(nums)):
      current_path.append(nums[i])
      backtrack(i, current_path, current_total + nums[i])
      current_path.pop()

  backtrack(0, [], 0)
  return result

print(f"The combinations that add up to the target (12) are: {combination_sum([2, 3, 6, 7], 12)}")