def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            current = nums[index]
            compliment = target - current
            if compliment in nums:
                index_compliment = nums.index(compliment)
                if index == index_compliment:
                    # check the rest of the nums
                    # past that index
                    if compliment in nums[index+1:]:
                        new_index = nums[index+1:].index(compliment)
                        index_compliment = index + new_index + 1
                        return [index,index_compliment]
                    else:
                        continue
                else:
                    return [index,index_compliment]

print(twoSum([3,3], 6))