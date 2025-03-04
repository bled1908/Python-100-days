import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decision = "yes"

while decision == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "encode":
                    result = position + shift
                elif direction == "decode":
                    result = position - shift
                cipher_text += alphabet[result % 26]
            else:
                cipher_text += letter
        print(f"The {direction}d text is {cipher_text}")

    caesar(text, shift, direction)
    
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if decision == "no":
        print("Goodbye")