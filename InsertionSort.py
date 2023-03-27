# -*- coding: utf-8 -*-
def insertionsort(A):
    
    for i in range(1, len(nums)):
        key = nums[i]#先訂最前面的key
        j = i - 1 #從頭開始
        while j >= 0 and key < nums[j] : #如果key比較小就要跟前面交換位置
                nums[j + 1] = nums[j] #把J往後放一個
                j = j - 1
        nums[j + 1] = key #key就變下一個

nums = [5, 2, 4, 6, 1, 3]
insertionsort(nums)
print(nums)