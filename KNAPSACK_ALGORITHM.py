def knapsack(weights,profit,limit):
    p_w=[]
    n=len(weights)
    for i in range(0,n):
        p_w.append(profit[i]/weights[i])
    p_w1=Merge_sort(p_w)
    P=0
    w1=0
    W=weights[p_w.index(p_w1[-1])]
    k=-1
    while(W>0):
        P=P+profit[p_w.index(p_w1[k])]*((W)/weights[p_w.index(p_w1[k])])
        w1=w1+weights[p_w.index(p_w1[k])]
        W=limit-w1
        k=k-1
    return P
    




import math
def merge_sorted_lists(a,b):
    i=0
    j=0
    n1=len(a)
    n2=len(b)
    n3=abs(n1-n2)
    c=[]
    lc=len(c)
    while(i<n1 and j<n2):
        if(a[i]<b[j]):
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    while i<n1:  #considering n2<n1
        c.append(a[i])
        i=i+1
    while j<n2:  #considering n1>n2
        c.append(b[j])
        j=j+1
    return c

    

    
def Merge_sort(a):
    n=len(a)
    if len(a)<=1:
        return a
    mid=n//2
    left=a[:mid]
    right=a[mid:]
    l1=Merge_sort(left)
    r1=Merge_sort(right)
    return merge_sorted_lists(l1,r1)
    
a=Merge_sort([1.3,1,1.4,0.3])

print(a)
    
   
    
Total_profit=knapsack([18,15,10],[25,24,15],20)
print(Total_profit)
    
        
        
