def login(user_id, password):
    if user_id == "IRONMAN" and password == "Tony_$":
        return "Login successful"
    else:
        return "Invaid Credentials"

for i in range(3):
    user_id = input("Enter your user id: ")
    password = input("Enter your password: ")
    result = login(user_id, password)
    print(result)
    if result == "Login successful":
        break
else:
    print("Account blocked")

