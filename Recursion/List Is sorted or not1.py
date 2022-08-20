def isSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    SmallerList=a[1:]
    isSmallerListSorted=isSorted(SmallerList)
    if isSmallerListSorted:
        return True
    else:
        return False
a=eval(input())
print(isSorted(a))