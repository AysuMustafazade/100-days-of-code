# for loop
for i in range(5):
    print(i)


# while loop
count = 0
while count < 5:
    print(count)
    count += 1


# break / continue
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)