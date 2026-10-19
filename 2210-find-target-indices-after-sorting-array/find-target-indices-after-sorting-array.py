class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_count = sum(1 for x in nums if x < target)
        target_count = sum(1 for x in nums if x == target)
        return list(range(less_count, less_count + target_count))