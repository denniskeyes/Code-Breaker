import random

#GET GUESS
def get_guess():
    return list(input("What is your guess? "))

#GENERATE RANDOM COMPUTER CODE
def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

#GENERATE THE CLUES
def generate_clues(code, user_guess):
    if user_guess == code:
        return "Congratulations, perfect Match!!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")

        if clues == []:
            return ["Nope"]
        else:
            return clues



###RUN GAME LOGIC###
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "Congratulations, perfect Match!!":

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("Here is your guess: ")
    for clue in clue_report:
        print(clue)
