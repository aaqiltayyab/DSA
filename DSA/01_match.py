n = int(input("Enter the marks : "))
match n:
    case n if n > 90:
        print("Fist Division")
    case n if n > 80:
        print("Second Division")
    case n if n > 70:
        print("Third Division")
    case _:
        print("Fail")

