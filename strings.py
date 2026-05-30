# s1="Nibba"
# s2="Nibbi"
# s3=s1+s2
# print(s3)

# s1="dinga"
# s2="dingi"
# s3=s1-s2
# print(s3)

# s1="sundra"
# s2="sundri"
# s3=s1*s2
# print(s3)

# s1="sundra"
# s2="sundri"
# s3=s1*2
# print(s3)

# s1="raja"
# s2="rani"
# s3=s1/s2
# print(s3)

# s1='Rama'
# print(s1.lower())

# s2='Sita'
# print(s2.upper())

# s3='PenTagOn'
# print(s3.swapcase())

# s4='SPAce'
# print(s4.capitalize())

# s5='dinga is dancing'
# print(s5.replace('is', 'was'))

# s6='Munni is eating'
# print(s6.startswith('Munna'))
# print(s6.startswith('M'))

# s7='Dingi is Dead'
# print(s7.endswith('Alive'))
# print(s7.endswith('ad'))

# s1='Rama'
# s2='Sita'
# s3='rama'
# s4='Rama'
# s5='Sita'
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(s4))
# print(id(s5))

# s1='rama'
# s2,s3,s4,s5=s1
# print(s2)
# print(s3)
# print(s4)
# print(s5)

# s1="If You Think You Can or You Cant"
# print(s1.count("Think"))
# print(s1.find("You"))
# print(s1.find("Can"))
# print(s1.rfind("You"))
# print(s1.index("You"))
# print(s1.rindex("You"))
# print(s1.find("Python"))
# print(s1.index("Python"))

# s1=input("enter string:")
# if s1.isalpha():
#     print(s1,"Contains only characters")
# elif s1.isdigit():
#     print(s1,"contains only digits")
# elif s1.isalnum():
#     print(s1,"contains both character and  digits")
# else:
#     print(s1,"contains other characters")

# s2=input("enter string:")
# print(s2.isalpha())
# print(s2.isdigit())
# print(s2.isalnum())

# s1='Hi'
# s1='Hello'
# s1='Hey'
# print(s1)

# s1='Rama'
# s2=''
# for i in s1:
#     s2=s2+i
# print(s2)

# s1='Rama'
# s2=''
# for i in s1:
#     s2=i+s2
# print(s2)

# s1=input("enter string:")
# s2=s1.upper()
# s3=''
# for i in s2:
#     s3=i+s3
# if s2==s3:
#     print('palindrome')
# else:
#     print('not palindrome')

# s1='chinni is dancing'
# o/p dancing is chinni

# s1='chinni is dancing'
# s2=s1.split()
# s3=''
# for i in s2:
#     s3=i + ' ' + s3
# print(s3)
# print(s2)
# print(len(s3))
# print(len(s1))

# s1=' dinga is vibing '
# print(s1.lstrip())
# print(s1.rstrip())
# print(s1.strip())

# s1='R a m a'
# s2=''
# for i in s1:
#     if i!= ' ':
#         s2=s2+i
# print(s2)

# s1='R a m a'
# s2=''
# for i in s1:
#     if i==' ':
#         continue
#     else:
#         s2+=i
# print(s2)

# s1 = 'Rama'
# s2 = ''
# for i in s1:
#     if i in s2:
#         continue
#     else:
#         s2 += i
# print(s2)

# s1='Raj'
# s2='Ram'
# s3='Raj'
# print('R' in s1)
# print('s' in s1)
# print(s1 in s3)
# print('s' not in s2)
# print(s2 not in s1)
# print(s3 not in s1)

# s1 = 'Rama'
# s2 = ''
# for i in s1:
#     if i not in s2:
#         s2 += i
# print(s2)

# s1=input("enter a alphabet")
# print(ord(s1))
# s2=int(input("enter a ASCII no."))
# print(chr(s2))

# s1='R a m a'
# s2=''
# for i in s1:
#     if i=='a':
#         s2+='@'
#     else:
#         s2+=i
# print(s2)

# name=input("Enter your name:")
# native=input("Enter your native place:")
# print(f"my name is {name} And I am from {native}")

# class Employee:
#     def work(self,A=10,B=20,C=30):
#         print(A)
#         print(B)
#         print(C)
# E=Employee()
# X=11
# Y=22
# Z=33
# E.work()
# E.work(X,Y,Z)
# E.work(Y,Z)
# E.work(Z)
# E.work(B=Z)
# E.work(A=Y,B=X,C=Z)

#str into list and list into str
# s=input("enter string")
# l=list(s)
# st=''
# for i in l:
#     st+=i
# print(st)

# s=input("enter string")
# ch=input("enter character")
# count=0
# for i in s:
#     if i==ch:
#         count+=1
# print(count)

#sort in alphabetical order
# s=input("enter string")
# l=list(s)
# l.sort()
# st=''
# for i in l:
#     st=st+i
# print(st)

#reverse a string
# s=input("enter string")
# print(s[::-1])

#or

# s=input("enter string")
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

#or

# s=list(input('enter a string'))
# i=0
# j=len(s)-1
# while i<j:
#     s[i],s[j] = s[j],s[i]
#     i+=1
#     j-=1
# print(''.join(s))

#palindrome or not
# s=input("enter string :")
# rev=s[::-1]
# if s==rev:
#     print('palindrome')
# else:
#     print('not palindrome')

#using two pointer
# s=input("enter string")
# i=0
# j=len(s)-1
# flag=True
# while i<j:
#     if s[i]!=s[j]:
#         flag=False
#         break
#     i=i+1
#     j=j-1
# if flag:
#     print("palindrome")
# else:
#     print("not a palindrome")

# s=input("enter string")
# out=''
# for i in s:
#     if 'A' <= i <= 'Z':
#         out += chr(ord(i) + 32)
#     elif 'a' <= i <= 'z':
#         out += chr(ord(i) - 32)
#     else:
#         out += i
# print(out)

# s = input("Enter a string: ")
#
# capital = 0
# small = 0
# digits = 0
# spaces = 0
# special = 0
# words = 0
#
# for ch in s:
#     if ch.isupper(): #'A'<=ch<='Z':
#         capital += 1
#     elif ch.islower(): #'a'<=ch<='z':
#         small += 1
#     elif ch.isdigit(): #'0'<=ch<='9':
#         digits += 1
#     elif ch.isspace(): #ch == ' '
#         spaces += 1
#     else:
#         special += 1
#
# words = len(s.split())  # word=space+1
#
# print("Capital letters:", capital)
# print("Small letters:", small)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Words:", words)
# print("Special symbols:", special)

# storing word in list
# s1=input("enter string:")
# s2=s1.split()
# print(s2)

# Another way(without using split method)
# s=input("enter string:")
# out=[]
# word=''
# for i in s:
#     if i!=' ':
#         word=word+i
#     else:
#         out.append(word)
#         word=''
# out.append(word)
# print(out)

# s=input("enter string").split()
# if len(s)>1:
#     print('second string is ',s[1])
# else:
#     print('there is no second string')

# s=input("enter string").split()
# if len(s)>1:
#     print('second word is :',s[-2])
# else:
#     print('there is no second word')

# s=input("enter string:").split()
# out=[]
# for i in s:
#     out.append(i[::-1])
# print(' '.join(out))

# s=input("enter string").split()
# rev=s[::-1]
# print(''.join(rev))

#remove the duplicate values
# s1 = input('enter a string:')
# s2 = ''
# for i in s1:
#     if i in s2:
#         continue
#     else:
#         s2 += i
# print(s2)

#find the duplicate values
# s=input("enter string")
# res=''
# for i in s:
#     if s.count(i)>1 and i not in res:
#         print(i)
#     res+=i

# s=input("enter string").split()
# largest=''
# for i in s:
#     if len(i)>len(largest):
#         largest=i
# print(largest)

# def sam():
#     s=input('enter the string:').split()
#     out=[]
#     for i in s:
#         out.append(i[0]+i[-1])
#     print(' '.join(out))
# sam()

# s=input("enter string").split()
# dict={}
# for i in s:
#     dict[i]=len(i)
# print(dict)

# s=input("enter string")
# s1=''
# for i in s:
#     if i not in s1:
#         c=s.count(i)
#         s1=s1+i+str(c)
# print(s1)
