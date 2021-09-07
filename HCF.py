def hcf(a,b):
    if (a == 0):
        return b

    elif (b == 0):
        return a

    elif (a == b):
        return a

    elif (a > b):
        return hcf(a-b, b)
    else:
        return hcf(a, b-a)

if __name__=="__main__":

    a=int(input("Enter First Value: "))
    b=int(input("Enter Second Value: "))

    print(hcf(a,b))