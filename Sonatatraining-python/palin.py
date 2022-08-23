def pal(n):
    if(n==n[::-1]):
        return 'it is a palindrome'
    else:
        return 'not a palindrome'
n=input('enter a number')
x=print(pal(n))