alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            result = position + shift
        elif direction == "decode":
            result = position - shift
        # or
        # if direction == "decode":
        #     shift *= -1
        # result = position + shift
        # do the above code iutside the loop after the 'cipher_text = ""' statement
        cipher_text += alphabet[result % 26]
    print(f"The {direction}d text is {cipher_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)