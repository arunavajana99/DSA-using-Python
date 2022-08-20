def SelectionSort(arr):
    length=len(arr)
    for i in range (length-1):
        minindex=i
        for j in range(i+1,length):
            if(arr[j]<arr[minindex]):
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
arr=[1,3,2,4,0,6,8]
#arr=eval(input("Enter an Array for Selection Sort:"))
SelectionSort(arr)
print("The Sorted Array is:",arr)
