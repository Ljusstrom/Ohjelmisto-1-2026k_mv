USERNAME = "python"
PASSWORD = "rules"

uname = input("Enter username: ")
pword = input("Enter password: ")

count = 1
while (uname != USERNAME or pword != PASSWORD) and count < 5:
    print("Incorrect username or password. Please try again.")
    count += 1
    uname = input("Enter username: ")
    pword = input("Enter password: ")

if (count >= 5):
    print("Access denied")
else:
    print("Welcome")