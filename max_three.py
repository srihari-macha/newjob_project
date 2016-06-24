print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Finding max three elements $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("enter no of elements")
n=input()
a=[]
print("enter elements")
for i in range(0,n):
    a.append(input())
max1=0
max2=0
max3=0
for i in range(0,n):
    if a[i]>max1:
        t1=max1
        max1=a[i]
        if t1 > max2:
            t2=max2
            max2=t1
            if t2>max3:
                max3=t2
    elif a[i]>max2:
        t3=max2
        max2=a[i]
        if t3>max3:
            max3=t3
    elif a[i]>max3:
        max3=a[i]

print("Max three elements are")
print("max1 element:", max1)
print("max2 element:", max2)
print("max3 element:", max3)
