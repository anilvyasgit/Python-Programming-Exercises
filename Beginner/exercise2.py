#to input any integer
n=int(input())

#share a number
ans=n

#facorial development
#progressive multiplication

while n>1:
    n-=1
    ans=ans*(n)

#ultimate answer
print(ans)
