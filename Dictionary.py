Dic = {"bird" : "鳥", "cat" : "貓", "dog" : "狗", "fish" : "魚", "mouse" : "老鼠", "rabbit" : "兔子", "cow" : "母牛", "horse" : "馬", "pig" : "豬", "sheep" : "綿羊"}
# new_Dic = {v:k for k , v in Dic.items()}
while(1):
    i = input("請輸入指令: 1.英翻中 2.中翻英 3.離開 \n")
    print("")
    if(i == 1):
        print("請輸入英文單字: \n")
        k = input()
        if(Dic.get(k) != None):
            print(k + " => " + Dic[k] + "\t")
        else:
            print("查無此單字 ")
        print("")
#     elif (i == 2):
#         print("請輸入中文單字: \n")
#         k = input()
#         if(new_Dic.get(k) != None):
#             print(k + " => " + new_Dic[k]+ "\t")
#         else:
#             print("查無此單字 \t")
#         print("")
    elif(i == 3):
        print()
        break
    else:
        print("請輸入正確的指令! ")
        print("")