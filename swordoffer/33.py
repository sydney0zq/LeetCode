
# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # too brute, 236ms
        # set_nums = set(nums)
        # for n in set_nums:
        #     remind = target - n
        #     if remind in set_nums:
        #         return [n, remind]

        # too brute also, 172ms
        visited = set()
        for n in nums:
            remind = target - n
            if remind in visited:
                return (n, remind)
            else:
                visited.add(n)
        return []

        # two pointers
        # 正确性证明：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:       # nums[l] + nums[r] <  target
                l += 1
        return []

