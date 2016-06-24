print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Linked List implementation  %%%%%%%%%%%%%%%%%%%%%%%%%%%")
class Node:
    def __init__(node,data,right=None):
        node.data=data
        node.right=None
    def getData(node):
        return node.data
    def setData(node,data):
        node.data=data
    def getRight(node):
        return node.right
    def setRight(node,right):
        node.right=right
    #def Display(node1):
      #  while node1:
      #      print(node1.getData())
       #     node1=node1.right

print("enter no of elements in list")
n=input()
a=[]
print("enter elements in list")
for i in range(0,n):
    a.append(input())
temp=Node(a[0])
head=temp
for i in range(1,n):
    temp1=Node(a[i])
    temp.right=temp1
    temp=temp1
temp4=head
print("elements in list is:")
while temp4:
    print("----->",temp4.getData())
    temp4=temp4.right
print("enter element to search")
val=input()
temp4=head
for i in range(0,n):
    if temp4.getData()==val:
        print("val is found at", i)
        break
    temp4=temp4.right


