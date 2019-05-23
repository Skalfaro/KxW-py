
secret_word = "culo"
guess = ""
number_of_guesses = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if number_of_guesses < guess_limit:
        guess = input("enter a guess: ")
        number_of_guesses += 1
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print("u lose")
else:
    print("u win")