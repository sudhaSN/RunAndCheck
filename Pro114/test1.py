a = 33
b = "33"

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Output: TypeError: '>' not supported between instances of 'str' and 'int'