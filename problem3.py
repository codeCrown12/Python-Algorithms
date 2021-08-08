# for a set of numbers within the range of 1 to 100, write a program to return 'fizz' if a number is divisible by 3,
# return 'buzz' if a number is divisible by 5 and finally to return 'fizzbuzz' if a number is divisible by both 3 and 5

def myfunct():
    for i in range(1, 100):
        if (i % 3) == 0 and (i % 5) == 0:
            print("fizzbuzz")
        elif (i % 3) == 0:
            print("fizz")
        elif (i % 5) == 0:
            print("buzz")
        else:
            print(i)


myfunct()
