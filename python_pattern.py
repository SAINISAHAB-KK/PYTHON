#! /bin/python3

# for i in range(int(input())):print("*"*(i+1))
#
# n = int(input())
# for i in reversed(range(n)):print(" "*(i) + "*"*(n-i))
#
# n = int(input())
# for i in range(n):print(("* "*(i+1)).center((n*2)-1))
#
#
# for i in range(1,int(input())+1):
#     for  j in range(1,i+1):print(str(j)+ " ",end=" ")
#     print()
#
#
# k=1
# for i in range(1,(int(input())+1)):
#     for i in range(1,i+1):
#         print(k,end=" ");k=k+1
#     print()
#
#
# for _ in range (65,66+int(input())):print((chr(_)+" ")*(_-64))
#
# n=65
# for _ in range (1,int(input())+1):
#     for j in range(1,_+1):
#         print(chr(n),end=' ');n=n+1
#     print()
#
#
# n=int(input())
# for i in reversed(range(n)):print(("* "*(i+1)).center((n*2)-1))
#
# n = int(input())
# for i in range(n):print(("* "*(i+1)).center((n*2)-1))
# for i in reversed(range(n)):print(("* "*(i+1)).center((n*2)-1))
#
#
# for _ in reversed(range(int(input()))):print("* "*(_+1))
#
# n=int(input())
# for i in range(1,n+1):
#     if i == (n//2)+1:
#         print("* "*(n//2+1)) if n%2 == 0 else print("* "*(n//2+2))
#     else:
#         if n%2 == 0:
#             print(("* "*(n//2)).center(n+2)) if i ==1 else print("*"+" "*(n-1)+"*")
#         else:
#             print(("* "*(n//2)).center(n+2)) if i ==1 else print("*"+" "*(n)+"*")
#
#
#
# n= int(input())
# for i in range(n):print("* "*n) if i == 0 or i == n-1  else print("*"+" "*(n*2-3)+"*")
#
#
# n = int(input())
# for i in range(n):
#     for j in range(n):print("* ",end="") if i==j or j==0 or i==n-1  else print("  ",end="")
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,(n*2)):
#         if i+j == n+1 or j-(n-1)==i or i==n :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,(n*2)):
#         print("* ",end="")if i+j == n+1 or j-(n-1)==i else print("  ",end="")
#     print()
# for i in reversed(range(1,n)):
#     for j in reversed(range(1,(n*2))):
#         print("* ",end="") if i+j == n+1 or j-(n-1)==i else print("  ",end="")
#     print()


# for i in range(6):
#     for j in range(7):
#         print("*",end="") if (i ==0 and j%3 !=0 ) or (i ==1 and j%3==0) or (i-j ==2) or (i+j == 8) else print(end=" ")
#     print()

# import turtle
# turtle.pensize(1)
# turtle.speed(1)
# turtle.color("black")
# turtle.begin_fill()
# turtle.fillcolor("red")
# turtle.left(135)
# turtle.forward(200)
# turtle.circle(-90,200)
# turtle.setheading(60)
# turtle.circle(-90,200)
# turtle.forward(200)
# turtle.end_fill()
 

# print("Thank You!")
