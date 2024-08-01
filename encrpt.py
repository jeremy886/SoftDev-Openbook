alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(clear_text, shift):
    #Encrypt the clear text
    code = ""
    for ch in clear_text:
        code += chr((ord(ch)-ord("A")+shift)%26 + ord("A"))
    return code

# Prompt the user for a phrase and shift

clear_text = "HELLO"
shift = 13

encoded_text = encrypt(clear_text, shift)
print(encoded_text)
