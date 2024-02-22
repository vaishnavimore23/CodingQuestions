class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        maxLen = 0
        currentLen = 0
        if len(nums) == 1:
            return 1

        for i in range(len(nums) - 1):
            if (nums[i + 1] == nums[i] + 1) or (nums[i] == nums[i + 1]):
                currentLen += 1
                print(currentLen)
            else:
                # maxLen = max(currentLen, maxLen)
                currentLen = 0
                print(maxLen)
            maxLen = max(currentLen, maxLen)
        return maxLen


def main():
    obj = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    maxlen = obj.longestConsecutive(nums)
    print(maxlen)


if __name__ == "__main__":
    main()
