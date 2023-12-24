# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals.
# The farmer breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs


# Function:
def animals(chickens, cows, pigs):
    animal = [2, 4, 4]
    leg_count = (chickens * 2) + (cows * 4) + (pigs * 4)
    print(leg_count)

animals(2, 3, 5)   # ➞ 36

animals(1, 2, 3)   # ➞ 22

animals(5, 2, 8)   # ➞ 50
