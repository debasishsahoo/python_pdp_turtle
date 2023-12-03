from reverse import reverse
x=12
import pdb;pdb.set_trace()
#breakpoint()
r_x=reverse(x)

def product(x,y):
    res=x*y
    breakpoint()
    return res


ans =product(x,r_x)
print(f"Product of {x} and {r_x} is {ans}")