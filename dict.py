
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


li = [10, -5, 20, -2, 0, 30]

count = sum(1 for x in li if x > 0)

print("Positive numbers:", count)

li = [10, 20, 10, 30, 20]

s = set(li)

print(s)