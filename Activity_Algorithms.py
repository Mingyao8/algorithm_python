def printMaxActivities1(p, q):
    n = len(q)
    i = 0
    for j in range(1, n):
        if p[j] >= q[i]:
            print (j, end=" "),
            i = j
            
def recursive_activity_selector(p, q, k, n):
    m = k + 1
    while m < n and p[m] < q[k]:
        m = m + 1
    if m < n:
        return [m] + recursive_activity_selector(p, q, m, n)
    else:
        return []
            
x , y = [] , []
i = input().split()
j = input().split()
x.append(i)
y.append(j)
p = x[0]
q = y[0]
for i in range(0, len(p)):
    p[i] = int(p[i])
    q[i] = int(q[i])
printMaxActivities1(p, q)
print("")
n = len(p)
k = recursive_activity_selector(p, q, 0, n)
for i in range(0,len(k)):
    print(k[i], end=' ')