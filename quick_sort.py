def quick_sort(nums,low,high):
    if low < high:
        q = partition(nums, low, high)
        quick_sort(nums, low, q - 1)
        quick_sort(nums, q + 1, high)

def partition(nums, low, high):
    x = nums[high] #pivot
    i = low - 1
    for j in range(low,high):
        if nums[j] <= x:
            i=i+1
            (nums[i], nums[j]) = (nums[j], nums[i])
    (nums[i + 1], nums[high]) = (nums[high], nums[i + 1])
    return i + 1
    
if __name__ == "__main__":
    nums = [2,8,7,1,3,5,6,4]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)