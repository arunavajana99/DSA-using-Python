def LastIndexBetter(a,x,si):
    l=len(a)
    if si==l:
        return -1
    SmalerListOutput= LastIndexBetter(a,x,si+1)
    if SmalerListOutput!=-1:
        return SmalerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1
a=[1,2,3,4,5,4,6,4,7,8]
print(LastIndexBetter(a,4,0))