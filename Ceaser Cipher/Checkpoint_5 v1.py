# Caeser cipher
# Aaron Heald, 25/7/19

# V1: basic program

# lists
apbt_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_apbt_lst = []

print("if you wish to cipher press '1' if you wish to encrypt press '2'")

# Users input
option = input("Cipher or encrypt?: ")
print()

key = int(input("Key: "))
cipherInput = input("Input word: ").lower()
wordList = list(cipherInput)

position = -1

# Encrypting
if option == '2':

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

# ciphering
elif option == '1':

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
