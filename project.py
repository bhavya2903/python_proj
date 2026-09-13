import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: 0r quit(q) "))
    if(target=="q"):
        break
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
print("------game over------")
<br> "this is number guessing game"
<br>
import random
import string
password_length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(password_length):
    password += random.choice(characters)
print("Generated Password:", password)
<br>"this isautomatic password guesser"

