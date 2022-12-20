def compound(p,r,t):
    a=p*(pow((1+(r/100)),t))
    ci=a-p
    return a
p,r,t=map(int,input().split())
com=compound(p,r,t)
print("%.2f"%com)