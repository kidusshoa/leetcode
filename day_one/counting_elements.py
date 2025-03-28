from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(count for count in freq.values() if count == max_freq)
    

nums = [1,2,2,3,1,4]

solu = Solution()
print(solu.maxFrequencyElements(nums))
        