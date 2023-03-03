def remove_duplicates(nums):
    ###first constraint
    if 1 <= len(nums) <= 3*104:
        constraint = False
        ###second constraint
        for value in nums:
            if -100 <= value <= 100:
                constraint = True
            else:
                return "Values out of range"

        if constraint:
            ###third constraint
            nums.sort()

            ###start problem
            nums_len = len(nums)
            k = 0

            for num in set(nums):
                nums[k] = num
                k += 1

            for i in range(k, nums_len):
                nums[i] = "_"

            nums = [k, nums]
            return nums
    else:
        return "List length out of range"
