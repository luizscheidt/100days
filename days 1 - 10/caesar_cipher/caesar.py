alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, direction):
    cipher_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:  
            shifted_index = alphabet.index(letter) + shift_amount
            shifted_index %= len(alphabet)
            cipher_text += alphabet[shifted_index]

    print(f"Here is the {direction}d text: {cipher_text}")

caesar(text, shift, function)