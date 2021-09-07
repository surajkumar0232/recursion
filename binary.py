def binary(number):
    if number==0:
        return 0

    else:
        return number%2+10 * binary(number//2)


if __name__=="__main__":

    number=int(input("Enter the numner which binary you want: "))

    print(binary(number))