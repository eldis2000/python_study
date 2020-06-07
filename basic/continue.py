absent = [2,5]
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("today class is over!. {0} is get out! ".format(student))
        break
    print("{0}, read book".format(student))
