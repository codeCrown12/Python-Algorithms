# Write a program to generate a grid of equal rows and columns similar to a chessboard. example test case:
# grid(4):
# output
#  * * * *
# * * * *
#  * * * *
# * * * *
def grid(val):
    for i in range(val):
        print()
        for j in range(val):
            if (i % 2) != 0:
                print(f"#  ", end="")
            else:
                print(f"  #", end="")


val = int(input("Enter grid number: "))
grid(val)
