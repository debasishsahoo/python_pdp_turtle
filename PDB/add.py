import pdb

def add(a, b):
    ans = a + b
    return ans

pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = add(x, y)
print(sum)