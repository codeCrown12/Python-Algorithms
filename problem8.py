# Given a list of numbers write a program that changes the position of the even numbers in the list as shown in the sample below:
# [2, 1] = 12
# [1, 2, 3, 4, 5, 6, 7] = 2143657

def revEven(myarr):
    answer = ""
    if len(myarr) > 2:
        for i in range(len(myarr)):
            temp = 0
            if myarr[i] % 2 == 0:
                temp = myarr[i - 1]
                myarr[i - 1] = myarr[i]
                myarr[i] = temp
    elif len(myarr) == 2:
        myarr.reverse()
    for i in myarr:
        answer += str(i)
    return int(answer)


# Test algorithm here by manipulating input
myarr = [1, 2, 3, 4, 5, 6, 7]
print(revEven(myarr))
