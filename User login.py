username="India"
user_input=input("Enter the Username :")
password="Hello"
password_input=""
password_attempt=1
password_locke=False
while user_input!=username:
    user_input=input(" Entered Username is wrong,Please check and Enter correct Username :")
while password_input!=password and not (password_locke):
    if password_attempt <= 3:
        password_input = input("enter the password :")
    else:
        password_locke=True
    password_attempt+=1

if password_locke:
    print("your account is locked")
else:
    print("login sucessfully")














