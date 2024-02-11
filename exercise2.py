number_list = []
print("NOTE: Enter more than 5 numbers as we have to find 5 greatest numbers")
number = input("Enter the first number or quit by pressing Enter: ")
for _ in range(1, 50):
    if number != "":
        number_list.append(int(number))
        number = input("Enter the next number or quit by pressing Enter: ")
    else:
        break
print(number_list[0:])
number_list.sort()
print("Sorted list:", number_list)
print("Five Greatest numbers are")
print(number_list[-1:-6:-1])