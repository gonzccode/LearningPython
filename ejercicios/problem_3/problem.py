def contain_duplicate(nums):
    ###first constraint
    if 1 <= len(nums) <= 105:
        constraint = False
        ###second constraint
        for value in nums:
            if -109 <= value <= 109:
                constraint = True
            else:
                return "Values out of range"

        if constraint:
            ###start problem
            k = 0
            for i in set(nums):
                k += 1

            if k == len(nums):
                return False
            else:
                return True
    else:
        return "List length out of range"
        
contain_duplicate([1, 2, 3, 1])
contain_duplicate([1, 2, 3, 4])
contain_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
