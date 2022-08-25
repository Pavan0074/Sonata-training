def age():
    name=input('Enter name:')
    age=int(input('Enter age:'))
    if (age == 0):
        print (name + 'just born')
    elif (age == 100):
        print( name +'already completed 100 yeras')
    else:
         x = (100 - age)
         print(name ,'needed',str(x) ,'to complete 100years')
age()