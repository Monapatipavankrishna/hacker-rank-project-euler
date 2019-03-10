def tribonnaci(a,b,c,k):
    oddnum=k
    a1=a
    b1=b
    c1=c
    index=0
    current=1
    while index<oddnum:
        a=a1
        b=b1
        c=c1
        t=0
        current=current+2
        for i in range(70000):
            d=a+b+c
            d=d%current
            if d==0:
                t=1
                break
            a=b;b=c;c=d;
            if a1==a and b1==b and c1==c:
                break
        if t==0:
            index=index+1
    return current
string=input()
string=string.split(" ")
a=int(string[0])
b=int(string[1])
c=int(string[2])
k=int(string[3])
result=tribonnaci(a,b,c,k)
print(result)
