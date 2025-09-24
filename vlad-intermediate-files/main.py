import random
def greet_user():
    print("Welcome to Weather Bot!")
    name = input("What is your name? ")
    print(f"Hello, {name}! Here's your weather forecast:")
    temp = random.randint(0, 20)
    print(f"The temperature will be +{temp}.")

if __name__ == "__main__":
    greet_user()