class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
   
if __name__ == "__main__":
  
    solution = Solution()
    sample_prices = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(sample_prices)
    print(f"Input Prices: {sample_prices}")
    print(f"Maximum Profit: {result}")

    
REMOVE DUPLICATES FROM SORTED ARRAY
class Solution:
   
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1


solution = Solution()
input_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
unique_count = solution.removeDuplicates(input_nums)
print(unique_count)


#GROUP ANAGRAMS
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


ob = Solution()


print(ob.groupAnagrams(strs))