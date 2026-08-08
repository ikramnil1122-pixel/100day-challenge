print("Welcome to the Band Name Generator!")
city = input("What city did you grow up in? ")
pet = input("What is the name of your first pet? ")
print("Your band name is " + city + " " + pet)
# 2 exercice
name = input("What is your name? ")
colore = input("What is your favorite color? ")
food = input("What is your favorite food? ")
print("Hello " + name + "!\n Your favorite color is " +
      colore + " and you like " + food)
# 3 exercice


def fuzz_buzz():
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    return


number = int(input("Enter a number: "))
fuzz_buzz()
