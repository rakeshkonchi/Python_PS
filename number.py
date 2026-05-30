#even or odd
# n=int(input('enter a val:'))
# if n%2==0:
#     print('even no.')
# else:
#     print('odd no.')

#prime
# n=int(input("enter the number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("the number is prime")
# else:
#     print("the number is not prime")

#HCF
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# for i in range(1, min(a, b) + 1):
#     hcf=i
# print(hcf)

# LCM
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# for i in range(1, min(a, b) + 1):
#     hcf=i
# print('lcm is:',(a*b)//hcf)


#Successive calculation
# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

#factorial
# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

#genesis
# n=0
# for i in range(1,5):
#     n=n*10
#     d=int(input('enter val:'))
#     n=n+d
# print(n)

#destruction
# n=int(input("enter the number"))
# while n>0:
#     d=n%10
#     n=n//10
#     print('extracted num is:',d)
#     print('remaining num is:',n)

#sum of individual digit
# n=int(input("enter the number"))
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum)

#product of individual digit
# n=int(input("enter the number"))
# pro=1
# while n>0:
#     d=n%10
#     pro=pro*d
#     n=n//10
# print(pro)

# calculate the length of the integer
# n=int(input("enter the number"))
# count=0
# while n>0:
#     d=n%10
#     count+=1
#     n=n//10
# print(count)

# reverse a number
# n=int(input("enter the number"))
# rev=0
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# print(rev)

# check number is palindrome or not
# n=int(input("enter the number"))
# rev=0
# temp=n
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if temp==rev:
#     print('Palindrome')
# else:
#     print('Not Palindrome')

# armstrong or not
# n=int(input("enter the number"))
# sum=0
# for i in str(n):
#     num=int(i)
#     sum=sum+num**(len(str(n)))
# if sum==n:
#     print('armstrong')
# else:
#     print('not armstrong')

#Perfect no or not
# n=int(input("enter the number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum = sum+i
# if sum==n:
#     print('perfect num')
# else:
#     print('not perfect num')

# Strong num or not
# n=int(input("enter the number"))
# sum = 0
# for i in str(n):
#     num=int(i)
#     fact = 1
#     for j in range(1,num+1):
#         fact=fact*j
#     sum=sum+fact
# if sum==n:
#     print('it is a strong number')
# else:
#     print('it is not a strong number')

# Duck num or not
# n=input("enter number")
# if n[0]!='0' and '0' in n:
#     print('duck num')
# else:
#     print('not a duck num')

# xylem or phloem
# n=int(input("enter the number"))
# n_str=str(n)
# first_last=int(n_str[0]) + int(n_str[-1])
# sum=0
# for i in n_str[1:len(n_str)-1]:
#     num=int(i)
#     sum=sum+num
# if first_last==sum:
#     print('Xylem')
# else:
#     print('phloem')

#neon num or not
# n=int(input("enter the number"))
# sqr=n**2
# sum=0
# for i in str(sqr):
#     sum=sum+int(i)
# if sum==n:
#     print('neon')
# else:
#     print('not a neon')

#Happy num or not
# n=int(input("enter the number:"))
# s=set()
# while n!=1:
#     if n in s:
#         print('not a happy number')
#         break
#     s.add(n)
#     total=0
#     for i in str(n):
#         total=total+(int(i)**2)
#     n=total
# else:
#     print('happy number')

# Automorphic num or not
# n=int(input("enter the number:"))
# sqr=n**2
# if str(sqr).endswith(str(n)):
      # print(str(sqr))
#     print('Automorphic Number')
# else:
#     print('Not Automorphic Number')

#spy num or not
# n=int(input("enter the number"))
# sum=0
# prod=1
# for i in str(n):
#     sum=sum+int(i)
#     prod=prod*int(i)
# print(sum)
# print(prod)
# if sum==prod:
#     print('spy number')
# else:
#     print('not spy number')

#swap 2 num using temp var
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# temp=a
# a=b
# b=temp
# print(a,b)

#swap 2 num without using extra var
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# a,b=b,a
# print(a,b)

# swap 2 num without using extra var
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

