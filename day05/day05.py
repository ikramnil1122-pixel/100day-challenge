# PYTHON LOOPS
import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '_', '+', '=', '-', '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', '.', '?', '/']
num = int(input("how many numbers do you want in your password? "))
alpha = int(input("how many alphabets do you want in your password? "))
sym = int(input("how many symbols do you want in your password? "))
password = (random.sample(numbers, k=num) +
            random.sample(alphabets, k=alpha) + random.sample(symbols, k=sym))
random.shuffle(password)
password = ''.join(map(str, password))
print("your password is ", password)
