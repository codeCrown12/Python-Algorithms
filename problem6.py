# Given a list of dictionary data containing customer name and purchases made, create a funtion that
# will congratulate and award customers who have made purchases greater than or equal to 50 naira at least three times.
# The function should also give a special message to customer with the highest total purchases that meet the above criteria.

def congratulateUser(customers):
    newarr = []
    for i in customers:
        count = 0
        sum = 0
        tempobj = {}
        for j in i["purchase"]:
            if j >= 50:
                count += 1
                sum += j
        if count >= 3:
            tempobj = {"name": i["name"], "total": sum}
            newarr.append(tempobj)
    # formatting purposes
    totals = []
    for i in newarr:
        totals.append(i["total"])
    print("The Premium membership goes to:")
    for i in newarr:
        if i["total"] == max(totals):
            print(i["name"])
    print("Our other winners are :")
    for i in newarr:
        if i["total"] != max(totals):
            print(i["name"])


customers = [{
    "name": "Bola",
    "purchase": [21, 90, 30, 16, 50, 60]
}, {
    "name": "King",
    "purchase": [30, 40, 45, 16, 60, 25]
}, {
    "name": "Favour",
    "purchase": [50, 55, 65, 13, 20, 60]
}, {
    "name": "Emeka",
    "purchase": [80, 90, 85, 22, 20]
}]

congratulateUser(customers)
