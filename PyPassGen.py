import random
import time

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# print("==== Welcome to PyPassGen! ====")



def amount():
    global amount
    amount = int(input("How many passwords would you like to generate? "))
    return amount


def length():
    global length
    length = int(input("Length of the password? "))
    return length


def gen():
    f = open("PyPassGen - Passwords.txt", "w")
    for _ in range(amount):
        password = ""
        for _ in range(length):
            password += random.choice(characters)
        # time.sleep(0.05)
        print(password)
        print(password, file=f)
    f.close

thankYou = "Thank you for using this password generator! Have a nice day! (-v-)"

while True:
    print("==== Welcome to PyPassGen! ====")
    try:
        amount()
        length()
        print("\nGenerating password(s), please wait...\n")
        time.sleep(1)
        gen()
        print("\nPasswords generated! See \"PyPassGen - Passwords.txt\" for the output file.\n" + thankYou)
        input("Press ENTER to quit program...")
        break
    except:
        x = input("\nYou didn't input numbers (>n<)\nTry again? Y/N " + "\n")
        if x == "y":
            continue
        elif x == "n":
            print(thankYou)
            break