class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        sum_total = 0
        for num in nums:
            sum_total += num
            sum_list.append(sum_total)
        return sum_list