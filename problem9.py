# 1. An atm has 100, 20, 9, and 1 Naira bills (NGN) available to be dispensed.  Given an amount between 0 and 10,000 Naira (inclusive) and asaiming that the ATM wants to use as few bills as possible, determine  the minimal number of 100, 20, 9, and 1 dollar bills the ATM needs to dispense (in that order). Here's the specification for the withdraw method you'll complete.
#
# Withdraw  (amount)
#
# Parameters
# Amount: Number - amount of money to withdraw. Assume that the amount is always divisible into 100, 20, 9, and 1 bills.
#
# Return value
# Array  <Number> An array of 4 integers representing the number of 100, 20, 9, and 1 Naira bills needed to complete the withdraw  (in that order). Constraints: 0《amount《10,000.
#
# Examples
# Amount         return value
# 1049              [10,2,1,0]
# 130                [1,1,1,1]
import math


def printNotes(amount):
    hundredNotes = math.floor(amount / 100)
    amount = amount - (hundredNotes * 100)
    twentyNotes = math.floor(amount / 20)
    amount = amount - (twentyNotes * 20)
    nineNotes = math.floor(amount / 9)
    amount = amount - (nineNotes * 9)
    oneNotes = math.floor(amount / 1)
    return [hundredNotes, twentyNotes, nineNotes, oneNotes]


print(printNotes(int(input("Enter the amount to withdraw: "))))
