def FirstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    SmallerList=a[1:]
    SmallerListOutput=FirstIndex(SmallerList,x)
    if SmallerListOutput==-1:
        return -1
    else:
        return SmallerListOutput+1
a=[1,2,3,4,5,6,7,8,9,7]
print(FirstIndex(a,8))