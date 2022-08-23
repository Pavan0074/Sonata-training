def age(age):
    x = (100 - age)
    if (age == 0):
        return 'just born'
    elif (age == 100):
        return 'already completed 100 yeras'
    return x, 'to complete 100years'
y=age(55)
print(y)