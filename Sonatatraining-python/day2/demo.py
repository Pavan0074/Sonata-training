p=147500
t=10
r=5
Interest=(p*t*r)/100
print(Interest)

height=1.75
weight=60
Bmi=weight/height**2
print(Bmi)#calculating bodymassindex

n1=55
n2=65
n3=54
if(n1>n2) and (n1>n3):
    print('n1 is highest')
elif (n2>n3):
    print('n2 is highest')
else:
    print('n3 is highest')

pl1=input()
pl2=input()
if(pl1==pl2):
    print('no result')
elif(pl1=='rock' and pl2=='scissors') or(pl2=='paper' and pl1=='scissors')or(pl1=='paper' and pl2=='rock') :
    print('pl1 wins')
elif (pl1 == 'rock' and pl2 == 'paper') or (pl2 == 'paper' and pl1 == 'scissors') or ( pl1 == 'scissors' and pl2 == 'rock'):
    print('pl2 wins')
else:
    print('provide valid input')
