class Solution:
   def solve(self, weights, values, capacity):
      res = 0
      for pair in sorted(zip(weights, values), key=lambda x: - x[1]/x[0]):
         if not bool(capacity):
            break
         if pair[0] > capacity:
            res += int(pair[1] / (pair[0] / capacity))
            capacity = 0
         elif pair[0] <= capacity:
            res += pair[1]
            capacity -= pair[0]
      return int(res)

ob = Solution()
weights = [1,3,5,4,1,3,2]
values = [5,10,15,7,8,9,4]
capacity = 15
print("The max profit is: ")
print(ob.solve(weights, values, capacity))
