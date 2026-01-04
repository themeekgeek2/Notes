class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def sum(self):
        return self.n1+self.n2
        
    def diff(self):
        return self.n1-self.n2


a=int(input('Enter first number:    '))
b=int(input('Enter second number:   '))

calc=Calculator(a,b)

reveal=input('Reveal answer:    ')
if reveal=="yes":
    print(f'Sum: {calc.sum()}')
    print(f'Diff: {calc.diff()}')
else:
    print('Thank you.')

'''ORIGINAL

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')'''
