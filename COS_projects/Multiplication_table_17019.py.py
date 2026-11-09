number = int(input("enter a whole number: "))
while number <= 1:
    print("sorry, you must input a number higher than 1")
    number = int(input("enter another number: "))
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)
