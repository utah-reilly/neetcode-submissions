class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        count, longest = 0, 0
        for i in nums:
            if (i - 1) not in seq:
                count = 0
                while (i + count) in seq:
                    count += 1
                if count > longest:
                    longest = count
        return longest

