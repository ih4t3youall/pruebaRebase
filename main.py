
def sum(a,b):
    print("sumando")
    return int(a)+int(b)
def resta(a,b):
    print("restando")
    return float(a)-float(b)

print("insert numer 1")
number1 = input()
print("insert number 2")
number2 = input()

result = sum(number1,number2)
print(result)
result1 = resta(number1,number2)
print(result1)
