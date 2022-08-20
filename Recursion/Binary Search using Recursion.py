def BinarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return BinarySearch(a,x,si,mid-1)
    else:
        return BinarySearch(a,x,mid+1,ei)
"""a=eval(input("Enter a List or an Array:"))
x=int(input("Select the element for Binary Search:"))
si=int(input("Enter the starting index of the String:"))
ei=len(a)
print("Index of the searched element is:",BinarySearch(a,x,si,ei))"""
print(BinarySearch([1,3,5,7,9,11,13,15,16,17],3,0,9))