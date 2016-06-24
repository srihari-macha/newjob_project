print("%%%%%%%%%%%%%%%%%%%%%%%%%%%% Bubble sort %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("enter no of elements in array:")
n=input()
a=[]
print("enter elements")
for i in range(0,n):
    a.append(input())
print("elements before sort")
for i in range(0,n):
    print a[i],
#print("elements after sort")
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            (a[i],a[j])=(a[j],a[i])
print("\nelements after sort is:")
for i in range(0,n):
    print a[i],