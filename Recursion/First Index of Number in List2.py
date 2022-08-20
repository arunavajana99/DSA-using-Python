def FirstIndexBetter(a,x,si):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si
    SmallerListOutput=FirstIndexBetter(a,x,si+1)
    return SmallerListOutput
a=[1,2,3,4,5,6,7,8,9,7]
print(FirstIndexBetter(a,7,0))  