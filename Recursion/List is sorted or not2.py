def isSortedBetter(a,si):
    l=len(a)
    if si==l-1 or si==1:
        return True
    if a[si]>a[si+1]:
        return False
    isPartSortedBetter=isSortedBetter(a,si+1)
    return isPartSortedBetter
a=eval(input())
print(isSortedBetter(a,0))
