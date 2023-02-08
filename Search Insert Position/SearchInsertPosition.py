def searchInsert(nums: list[int], target: int) -> int:

    low=0
    high=len(nums)-1
    while(low<=high):
        mid = (low+high)//2
        if(nums[mid]==target):
            return mid
        elif(target>nums[mid]):
            low=mid+1
        else:
            high=mid-1

    return low

# Test case 1
nums = [1,3,5,6]
target = 5

# Test case 2
nums = [1,3,5,6]
target = 2

# Test case 3
nums = [1,3,5,6]
target = 7



result =  searchInsert(nums,target)
print(result)