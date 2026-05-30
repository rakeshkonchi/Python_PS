# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('*',end=" ")
#     print()

# n=4
# for i in range(1, n+1):
#     for space in range(1, n-i+1):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print('*', end=' ')
#     for k in range(1, i):
#         print('*', end=' ')
#     print()
# n=4
# for i in range(n-1, 0, -1):
#     for space in range(1, n-i+1):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print('*', end=' ')
#     for k in range(1, i):
#         print('*', end=' ')
#     print()


# for i in range(97,101):
#     print(chr(i),end="")

# for i in range(65,69):
#     print(chr(i),end="")

# for i in range(1,5):
#     print(i,end=" ")

# for i in range(1,4):
#     print('*',end=" ")

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for space in range(1,i):
#         print(' ',end=' ')
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     for space in range(1, i):
#         print(' ',end=' ')
#     for space in range(1,i):
#         print(' ',end=' ')
#     for k in range(1,n-i+2):
#         print('*',end=' ')
#     print()

# n=4
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for k in range(1,i):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()

#Fusion pattern
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
# n=3
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     for space in range(1, i):
#         print(' ',end=' ')
#     for space in range(1,i):
#         print(' ',end=' ')
#     for k in range(1,n-i+2):
#         print('*',end=' ')
#     print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()


# n = 4
# for i in range(n,0,-1):
#     for space in range(1,n-i+1):
#         print(' ', end=' ')
#     for j in range(1,i+1):
#         print('*', end=' ')
#     for k in range(1,i):
#         print('*', end=' ')
#     print()
# n=4
# for i in range(2,n+1):
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for k in range(1,i):
#         print('*',end=' ')
#     print()

# n=4
# for i in range(1,n+1):
#     for space in range(1,i):
#         print(' ',end=' ')
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     for k in range(1,n-i+1):
#         print('*',end=' ')
#     print()
# n=3
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for j in range(1,i+2):
#         print('*',end=' ')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()

#Boundary pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('*',end=' ')
#         elif i==2 or j==2 or i==4 or j==4:
#             print('+',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n or j==3: #j==n//2+1 or 5//2
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n or i==3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n or j==3 or i==3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==3 or j==3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#diagonal pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1 or i==1 or j==1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==1 or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1 or i==1 or j==1 or i==n or i==j or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1 or i==j or i==1 or i==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# n=5
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i+j==n+1 or j-i==n-1 or i==n :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#number pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# n=4
# x=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(x,end=" ")
#         x+=1
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==3:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j%2,end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==3:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print((j+1)%2,end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j%4,end=' ')
#     print()

# n=4
# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x+=1
#     print()

# n=5
# for i in range(1,n+1):
#     x=5
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x-=1
#     print()

# n=5
# for i in range(1,n+1):
#     x=n-i+1
#     for j in range(1,n-i+2):
#         print(x,end=" ")
#         x+=1
#     print()

# n=5
# for i in range(1,n+1):
#     x=1
#     for space in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x+=1
#     y=i-1
#     for k in range(1,i):
#         print(y,end=" ")
#         y-=1
#     print()

# n=4
# for i in range(1,n+1):
#     x=i
#     for space in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=x-1
#     y=2
#     for k in range(1,i):
#         print(y,end=" ")
#         y=y+1
#     print()

# n=3
# x=1
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print(x,end=" ")
#         x+=1
#     print()

# n=4
# for i in range(1,n+1):
#     x = 4 * i
#     for j in range(1,n+1):
#         print(x,end=" ")
#         x+=1
#     print()

# n=4
# for i in range(1,n+1):
#     x = 4 * i
#     for j in range(1,n+1):
#         print(x,end=" ")
#         x-=1
#     print()

#Alphabet pattern

# n=5
# for i in range(1,n+1):
#     x = ord('A')
#     for j in range(1,n+1):
#         if i==j or i<j:#i<=j
#             print(chr(x),end=" ")
#             x+=1
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     x=ord('L')+i-1  #76+1-1
#     for j in range(1,n+1):
#         if i<=j:
#             print(chr(x),end=" ")
#             x+=1
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 and 1<j<n or j==1 and i>1 or i==3 or j==n and i>1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 and 1<j<n or j==1 and i>1 and i<5  or j==n and i>1 and i<5 or i==5 and 1<j<n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==5 or j==1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()