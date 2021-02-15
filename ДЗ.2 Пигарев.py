d = [ ]
i=1
result =0
while i<1000:
    d.append(i**3)
    i+=2
a = list.copy(d)
for i in range(len(a)):
    num=0
    while a[i]>0:
        num += a[i]%10
        a[i]//=10
    if num%7 ==0:
        result+=num
print(result)


result = 0
for i in range(len(d)):
    d[i]+=17
    num=0
    while d[i]>0:
        num += d[i]%10
        d[i]//=10
    if num%7 ==0:
        result+=num
print(result)
