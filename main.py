def sendmessage(name):
    # Sending message to INSERT_NAME_HERE...
    print(f"Sending message to {name}... ")

def deletemessage(name):
    print(f"Delete message to {name}...")

name = input("Enter your name: ")
print("1) Send Message\n2) Delete Message")

user_choice = int(input("What is your choice: "))

if user_choice == 1:
    sendmessage(name)
elif user_choice == 2:
    deletemessage(name)
else:
    print("We got something else.")
