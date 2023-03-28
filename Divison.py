#Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.


#Code
dividend = int(input("Enter value of dividend="))
divisor = int(input("Enter value of divisor="))

def divide(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient
quotient = divide(dividend, divisor)
print(f"The quotient of {dividend} divided by {divisor} is {quotient}")
