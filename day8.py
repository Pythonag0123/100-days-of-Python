#Caesor Cipher

alphas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',u',v','w','x','y','z']
def caesar_cipher(message, shift, command):
    encoded_message = ''
    for i in message:
        if i in alphas:
            position = alphas.index(i)
            if command == "encode":
                new_position = (position + shift) % len(alphas)
            elif command == "decode":
                new_position = (position - shift) % len(alphas)
            encoded_message += alphas[new_position]
        else:
            encoded_message += i
    print(encoded_message)

command = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower().strip()
shift = int(input("Enter the number of alphabet codes to shift: "))
message = input("Print Your Message: ").lower()

caesar_cipher(message, shift, command)
