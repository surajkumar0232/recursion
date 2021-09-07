def balanced_para(para,i,j):
    if i==len(para):
        if j==0:
            print("True : it has balanced paranthesis")
        else:
            print("False : it hasn't balanced paranthesis")
    
    elif para[i]=="(":
        print(j)
        return  balanced_para(para,i+1,j+1)

    elif para[i]==")":
        return  balanced_para(para,i+1,j-1)

    else:
        return balanced_para(para,i+1,j)

if __name__=="__main__":

    para=input("Enter the paranthesis to check (seperated by comma): ")

    i=0
    j=0

    balanced_para([para],i,j)