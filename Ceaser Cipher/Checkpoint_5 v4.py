# Caeser cipher
# Aaron Heald, 25/7/19

# V1: basic program
# V2: loops ciphering until wanted outcome
# V3: Encrypts text randomly
# V4: Functions set up to fix errors


# Functions
def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < -25 or response > 25:
                print("Please enter a number between -25 and 25 (those numbers included)")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()

def option_choice(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < 1 or response > 2:
                print("Please enter a number either 1 or 2")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()


# imports
import random


conti = False
while not conti:

    # lists
    apbt_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    new_apbt_lst = []

    print("if you wish to cipher (Encrypt to text) press '1'. If you wish to encrypt (Text to encryption) press '2'")


    new_apbt_lst.clear()

    # Users input
    option = option_choice("Cipher or encrypt?: ")
    print()
    if option == 1:
        print("You have chosen cipher")

    else:
        print("You have chosen encrypt")

    global key

    if option == 1:
        key = int_check("Key (if you don't know the key enter 0): ")
    else:
        key = int_check("Key (if you wish for a random key enter 0): ")
    cipherInput = input("Input word: ").lower()
    wordList = list(cipherInput)

    position = -1

    # ciphering
    if option == 1:

        new_key = 0
        unknownkey = 1
        if key == 0:
            valid = False
            while not valid:
                for x in range(len(wordList)):
                    position = position + 1
                    if wordList[position] in apbt_lst:
                        x = apbt_lst.index(wordList[position]) + 1
                        newcipher_inpt = x + (unknownkey - 1)
                        if newcipher_inpt > 25:
                            newcipher_inpt = newcipher_inpt - 26
                        newcipher_inpt = apbt_lst[newcipher_inpt]
                        new_apbt_lst.append(newcipher_inpt)
                    else:
                        new_apbt_lst.append(' ')
                for i in new_apbt_lst:
                    print(i, end="")

                print()
                sense = input("Does this make sense? if so press enter: ")
                print()

                if sense == '':
                    valid = True
                    new_key = (len(apbt_lst) + (apbt_lst.index(wordList[0])) - (apbt_lst.index(new_apbt_lst[0]))) - 26
                    print("{} is the key".format(new_key))
                else:
                    new_apbt_lst.clear()
                    position = -1
                    unknownkey = unknownkey + 1

            print()

        # runs if key is known
        else:
            for x in range (len(wordList)):
                position = position + 1
                if wordList[position] in apbt_lst:
                    x = apbt_lst.index(wordList[position]) + 1
                    newcipher_inpt = x - (key + 1)
                    if newcipher_inpt > 25:
                        newcipher_inpt = newcipher_inpt - 26
                    newcipher_inpt = apbt_lst[newcipher_inpt]
                    new_apbt_lst.append(newcipher_inpt)
                else:
                    new_apbt_lst.append(' ')

        for i in new_apbt_lst:
            print(i, end="")
        print()


    # Encrypting
    elif option == 2:

        # checks if user wants random key
        if key == 0:
            ran_key = random.randint(1, 25)
        else:
            ran_key = key

        # encrypts code
        for x in range (len(wordList)):
            position = position + 1
            if wordList[position] in apbt_lst:
                x = apbt_lst.index(wordList[position]) + 1
                newcipher_inpt = x + (ran_key - 1)
                if newcipher_inpt > 25:
                    newcipher_inpt = newcipher_inpt - 26
                newcipher_inpt = apbt_lst[newcipher_inpt]
                new_apbt_lst.append(newcipher_inpt)
            else:
                new_apbt_lst.append(' ')

        for i in new_apbt_lst:
            print(i, end="")
        print()
        if key == 0:
            print("The key is {}".format(ran_key))
            print()


    #checks with user if they wish to repeat the code
    repeat = input("Do you wish to decrypt/encrypt something again, if so press enter: ")

    if repeat == "":
        valid = False
        print()
        print()

    else:
        valid = True
        print("Thanks for using this Caesar cipher")
