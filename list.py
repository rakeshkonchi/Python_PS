#create list and print list
# n=int(input("enter the number:"))
# out=[]
# for i in range(1,n+1):
#     val=eval(input('enter the number:'))
#     out.append(val)
# print(out)

#sum of all int present inside the list
# l=eval(input('enter a list:'))
# sum=0
# for i in l:
#     if type(i)==int:
#         sum=sum+i
# print(sum)

#count the occurrence of given element in a given list
# l=eval(input('enter a list:'))
# val=int(input('enter a val:'))
# count=0
# for i in l:
#     if i==val:
#         count+=1
# print(count)

#reverse a list using two pointer
# l=eval(input('enter a list:'))
# i=0
# j=len(l)-1
# while i<j:
#     l[i],l[j]=l[j],l[i]
#     i=i+1
#     j=j-1
# print(l)

#list is palindrome or not
#slicing method
# l=eval(input('enter a list:'))
# rev=l[::-1]
# if l==rev:
#     print('palindrome')
# else:
#     print('not a palindrome')

#two pointer
# l=eval(input('enter a list:'))
# i=0
# j=len(l)-1
# flag=True
# while i<j:
#     if l[i]!=l[j]:
#         flag=False
#         break
#     i=i+1
#     j=j-1
# if flag :
#     print('palindrome')
# else:
#     print('not a palindrome')

#rotate the given list n no. of times to right
# l=eval(input('enter a list:'))
# n=int(input('enter a number of rotation:'))
# n=n%len(l)
# print(l[-n:]+l[:-n])

#rotate the given list n no. of times to left
# l=eval(input('enter a list:'))
# n=int(input('enter a number of rotation:'))
# n=n%len(l)
# print(l[n:]+l[:n])

# l1=eval(input("enter the list:"))
# l2=eval(input("enter the list:"))
# out=[]
# for i in l1:
#     if i in l2 and i not in out:
#         out.append(i)
# print(out)

# l=eval(input("enter the list:"))
# val=int(input("enter the number:"))
# for i in range(0,len(l)):
#     if l[i]==val:
#         print(i)
#         break

# l=eval(input("enter the list"))
# out=[]
# for i in l:
#     if i not in out:
#         print(i,':',l.count(i))
#     out.append(i)

# l=eval(input("enter the list"))
# out=[]
# for i in l:
#     if i in out:
#         print(i)
#         break
#     out.append(i)

l=eval(input("enter the list"))
n=int(input("enter the number"))
out=[]
for i in range(0,len(l)):
    if l[i]==n:
        out.append([l[i]])
    else:
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                out.append([l[i],l[j]])

print(out)