def cut_rod(prices, n):
    if (n == 0):
        return 0
    q = -1
    for i in range(1,n+1):
        q = max(q,prices[i]+cut_rod(prices, n-i))
    return q
     
def top_down_cut_rod(prices, n):
    r = [0]
     
    for j in range(1,n+1):
        r.append(float("-inf"))
        for i in range(1,j + 1):
            r[j] = max(r[j] , prices[i]+r[j-1])
    return r[n-1]
            
def extended_bottom_up_cut_rod(prices, n):
    r = [0]
    s = [0]
    for i in range(1,n+1):
        r.append(float("-inf"))
        s.append(0)
        
        for j in range(1,i+1):
            if (r[i] < prices[j]+r[i-j]):
                r[i] = prices[j]+r[i-j]
                s[i] = j
    return r,s

if __name__ == "__main__":
#    prices = [6, 10, 12, 15, 20, 23]
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(prices)-1
    print(cut_rod(prices, n))
    print(top_down_cut_rod(prices, n))
    print(extended_bottom_up_cut_rod(prices, n))