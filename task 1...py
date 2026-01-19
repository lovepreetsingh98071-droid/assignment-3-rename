def fac_num(number):
    if number == 1:
        return 1
    else:
        factor = number * fac_num(number - 1)
        return factor
number = int(input("Enter a number: "))
print(f"Factorial of {number} is : {fac_num(number)}")

