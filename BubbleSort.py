def BubbleSortArray(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[6,4,8,3,1,2]
#arr=eval(input("Enter an Array for Bubble Sort:"))
BubbleSortArray(arr)
print(arr)