#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class solution(object):
  def containsDublicates(self,nums):
    seen == set()
    for num in nums :
      if num in seen :
        return True
      seen.add(num)
    return False
# O(1) time complexity 

class solution(object):
  def containDublicate(self,nums):
    n = len(nums)
    for i in range(n-1):
      for j in range(i+1,n):
        if nums[i]==nums[j] :
          return True
    return False
# O(n^2) time complexity

class solution(object):
  def containDublicate(self,nums):
    nums.sort()
    n =len(nums)
    for i in range(1,n):
      nums[i]==nums[n-1]
      return True
    return False
# O(log n ) time complexity
