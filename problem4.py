# Given a list containing integers and strings, write a program to find the sum of all the integers in the list,
# and also to find the product of all the strings in the list
# example:
# [1,3,5,6,"10",7,"2","8",4] -> sum is 26 and product is 160

def calculate(mylist):
    total_sum = 0
    total_product = 1
    for value in mylist:
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, str):
            total_product *= int(value)
    print(f"Sum is {total_sum} and product is {total_product}")


mylist = [1, 3, 5, 6, "10", 7, "2", "8", 4]
calculate(mylist)
