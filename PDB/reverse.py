def reverse(num):
    r_num=0
    while num>0:
        r=num%10
        num=num//10
        r_num=r_num*10+r
    return r_num
if __name__=="__main__":
    print(reverse(123))