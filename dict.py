
li = []

a = int(input("How many numbers do you want to enter? "))

count = 0

for i in range(a):
    b = int(input("Enter a number: "))
    li.append(b)

    if b > 0:
        count += 1

print("Numbers:", li)
print("Total positive numbers:", count)
