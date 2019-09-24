num = int(input("Enter the number upto which prime numbers should be generated: "))

for i in range(num):
    for j in range(2, num//2):
        if i % j == 0:
            break
    else:
        print(i)