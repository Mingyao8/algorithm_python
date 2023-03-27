# -*- coding: utf-8 -*-
def mergesort(items, p, r):
    if p>=r :#不能再切
        return 
    q = (p + r)//2 #找出中間
    mergesort(items, p, q) #一直切
    mergesort(items, q + 1, r)#一直切
    merge(items, p, q , r)
   
def merge(items, p, q, r):
    rightpart = items[q+1:r+1]#右邊的長度
    leftpart = items[p:q + 1]#左邊的長度
    leftpart_index = 0
    rightpart_index = 0
    sorted_index = p #用來看現在在陣列的哪個位置
    
    while leftpart_index < len(leftpart) and rightpart_index < len(rightpart): #兩邊的陣列都跑到完
        if leftpart[leftpart_index] <= rightpart[rightpart_index]:#如果左邊比較小，就sorted
            items[sorted_index] = leftpart[leftpart_index] #left part 的 index 就增加
            leftpart_index = leftpart_index + 1          
        else:
            items[sorted_index] = rightpart[rightpart_index]#如果右邊比較小，就sorted
            rightpart_index = rightpart_index + 1 #right part 的 index 就增加          
        sorted_index+=1

    while leftpart_index < len(leftpart): #右邊的跑完了，剩下左邊的
        items[sorted_index] = leftpart[leftpart_index]
        leftpart_index = leftpart_index + 1
        sorted_index = sorted_index + 1

    while rightpart_index < len(rightpart):#左邊的跑完了，剩下右邊的
        items[sorted_index] = rightpart[rightpart_index]
        rightpart_index = rightpart_index + 1
        sorted_index = sorted_index + 1
    
items = [2,4,5,7,1,2,3,6]
mergesort(items, 0, len(items)-1)
print(items)