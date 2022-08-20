def sum_n(n):
    if n==0:
        return 0
    SmallOutput=sum_n(n-1)
    Output=SmallOutput+n
    return Output
n=int(input())
print(sum_n(n))