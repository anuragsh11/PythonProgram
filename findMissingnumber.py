def missing_number(nums):
    arr=[0 for i in range(len(nums))]
    print(arr)
    print(len(nums))
    for i in range(len(nums)):
        if nums[i] < len(nums):
            arr[nums[i]] = -1
    print(arr)
    for i in range(len(nums)):
        if arr[i] != -1:
            return i

    return len(nums)

arra= [1,2,4,5,6,7]
print(missing_number(arra))