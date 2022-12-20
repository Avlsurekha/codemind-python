def reverse(n):
    rev=0
    n1=n
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    if(n1==rev):
        return True
    else:
        return False
n=int(input())
res=reverse(n)
print(res)
