try:
    age = int(input("enter age :"))
    print(age)
except ValueError:
    print("invalid age")