def add(n1,n3=10,n2=100):
    sum=n1+n2+n3
    return sum
res=add(5,20,50)
print(res)
res=add('pavan ','veeravalli')
print(res)
res=add(True,False)
print(res)
res=add([1,2,3],[4])
print(res)
range()
f=lambda n1,n2:n1+n2
print(f(10,20))