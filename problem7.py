# Validate Credit or Debit Card
#
# A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that's also stored in a database somewhere so that when your card is used to buy something, the creditor knows whom to the bill.
#
# For Context
#
# Your task is to take a credit card number and determine whether that number is an American Express Credit Card number or Master Card number or Visa or something else.
#
# Luckily for us, credit card numbers actually have some structure or patterns to them.
#
# American Express Card numbers always have 15 digits and start with 34 or 37;
# Most Master Card numbers have 16 digits and start with 51, 52, 53, 54, or 55;
# Visa Card numbers have 13 or 16 digits and start with 4.
# Also for a credit card number to be considered valid, it has to satisfies the checksum or Luhn Algorithm: a mathematical algorithm invented by Hans Peter Luhn of IBM which is mostly used in generating credit card numbers.
#
# How does this algorithm work?
#
# The algorithm takes the following steps:
#
# Multiply every other digit by 2, starting with the second-to-last digit
# Add those product’s digits together
# Add the sum to the sum of the digits that weren’t multiplied by 2
# If the total’s last digit is 0, the number is valid else it invalid
# That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014
#
# Step 1: Multiply every other digit by 2, starting with the second-to-last digit
#
# For the sake of discussion, let‘s put every other digit in a quote, starting with the number’s second-to-last digit. This will give us
#
# 4 0 0 3 6 0 0 0 0 0 0 0 0 0 1 4
#
# Okay, let’s multiply each of the quoted digits by 2:
#
# 1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
#
# That gives us:
#
# 2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
#
# Step 2: Add those product’s digits together
#
# 2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
#
# NB: We only add the product digit and not the products themselves together
#
# Step 3: Add the sum to the sum of the digits that weren’t multiplied by 2
#
# Sum of numbers that weren’t multiplied by 2 are:
#
# 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 7
#
# Then Let’s add the sum in step2 to it
#
# 7 + 13 = 20
#
# Step 4: If the total’s last digit is 0, the number is valid else it invalid
#
# Yes, the last digit in the sum was 0, so David’s card is valid!
#
# So, validating credit card numbers isn't hard, but it does get a bit tedious by hand. Let's write a program.
#
# Program Expectation
#
# Prompt the user for input: a credit card number
# Calculate the checksum: to figure out if it could be a valid credit card or not
# Check for card length and starting digits
# Print AMEX for American Express Card, MASTERCARD for mastercard, VISA for visa card, or INVALID: if it doesn’t satisfy any of the 3 types of cards
# Test your program on different credit card

# Luhn's algorithm implementation
def checkSum(card):
    card_rev = card[::-1]
    double_arr = []
    undoubled_arr = []

    # Loop through the reversed card digits starting from the second to the last digit
    for i in card_rev[1::2]:
        a = int(i) * 2
        double_arr.append(a)

    # Loop through and save the non-doubled integers
    for i in card_rev[0::2]:
        undoubled_arr.append(int(i))

    # Check if any of the doubled values results in a double integer
    for i in double_arr:
        a = str(i)
        if len(a) > 1:
            double_arr.remove(i)
            b = list(a)
            for j in b:
                double_arr.append(int(j))
    final_arr = double_arr + undoubled_arr
    total = sum(final_arr)
    if total % 10 == 0:
        return True
    return False

# Credit card type validation
def verifyCard(card):
    if checkSum(card):
        if (len(card) == 15) and (card[:2] == "34" or card[:2] == "37"):
            return "AMEX"
        elif (len(card) == 16) and (card[:2] == "51" or card[:2] == "52" or card[:2] == "53" or card[:2] == "54" or card[:2] == "55"):
            return "MASTERCARD"
        elif (len(card) == 13 or len(card) == 16) and card[:1] == "4":
            return "VISA"
        else:
            return "INVALID"
    else:
        return "INVALID"


print(verifyCard("4003600000000014"))
