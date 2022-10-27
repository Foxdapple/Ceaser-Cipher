# Caeser cipher
# Aaron Heald, 25/7/19

# V1: basic program
# V2: loops ciphering until wanted outcome

# lists
apbt_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


new_apbt_lst = []

print("if you wish to cipher press '1' if you wish to encrypt press '2'")

# Users input
option = input("Cipher or encrypt?: ")
print()

if option == '1':
    key = int(input("Key (if you don't know the key enter 0): "))

cipherInput = input("Input word: ").lower()
wordList = list(cipherInput)

position = -1

# ciphering
if option == '1':

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
                print("{} is the key")
            else:
                new_apbt_lst.clear()
                position = -1
                unknownkey = unknownkey + 1

        print()

    else:
        for x in range (len(wordList)):
            position = position + 1
            if wordList[position] in apbt_lst:
                x = apbt_lst.index(wordList[position]) + 1
                newcipher_inpt = apbt_lst[x - (key - 1)]
                new_apbt_lst.append(newcipher_inpt)
            else:
                new_apbt_lst.append(' ')

    for i in new_apbt_lst:
        print(i, end="")
    print()


# Encrypting
elif option == '2':

    for x in range (len(wordList)):
        position = position + 1
        if wordList[position] in apbt_lst:
            x = apbt_lst.index(wordList[position]) - 1
            newcipher_inpt = apbt_lst[x - (key + 1)]
            new_apbt_lst.append(newcipher_inpt)
        else:
            new_apbt_lst.append(' ')

    for i in new_apbt_lst:
        print(i, end="")
    print()


