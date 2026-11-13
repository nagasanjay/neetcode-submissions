class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counterHash = Counter(nums);
        for _value, count in counterHash.items():
            if count > 1:
                return True

        return False