print("***********  elements in array left rotation *******************")
print("enter no of elements in array:")
n=input()
a=[]
print("enter elements:")
for i in range(0,n):
        a.append(input())
print("enter number of times to rotate elements:")
rot=input()
print("elements before rotaton :")
for i in range(0,n):
        print(a[i])
for j in range(0,rot):
        l=a[0]
        for i in range(0,n-1):
                #t=a[i]
                a[i]=a[i+1]

        a[n-1]=l
print("elements after rotation:")
for i in range(0,n):
        print(a[i])


