count = 0
summ = 0

while True:
    try:
        for x in range(count, 5):
            count = x
            print("Enter int #", count + 1, ": ")
            number = int(input())
            summ += number
        print("Your sum is:", summ)

    except ValueError:
        print("Invalid input. Please enter an int.")
    else:
        break
