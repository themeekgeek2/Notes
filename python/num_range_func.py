# range inputs
inp_1=float(input("Enter lower range:  "))
inp_2=float(input("Enter higher range:     "))

# number inputs
inp_3=float(input("First number:    "))
#inp_4=float(input("Second number:   "))

# numRange func
def numRange(lr,hr,n):
    '''lr=inp_1
    hr=inp_2
    n=inp_3,inp_4'''
    if n>=lr and n<=hr:
        return True
        print("Input inside of the input ranges.")
    else:
        return False 
        print("The values are outside the input ranges.")
        
numRange(inp_1,inp_2,inp_3)

