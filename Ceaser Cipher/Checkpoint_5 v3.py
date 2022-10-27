# Caeser cipher
# Aaron Heald, 25/7/19

# V1: basic program
# V2: loops ciphering until wanted outcome
# V3: Encrypts text randomly

# imports
import random

# lists
apbt_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


new_apbt_lst = []

print("if you wish to cipher press '1' if you wish to encrypt press '2'")


new_apbt_lst.clear()

# Users input
option = input("Cipher or encrypt?: ")
print()

global key

if option == '1':
    key = int(input("Key (if you don't know the key enter 0): "))
else:
    key = int(input("Key (if you wish for a random key enter 0): "))
cipherInput = input("Input word: ").lower()
wordList = list(cipherInput)

position = -1

# ciphering
if option == '1':

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
elif option == '2':

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
