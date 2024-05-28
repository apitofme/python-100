"""
-=< 100 Days of Python >=-
-=[ Day 008 ]=-

Project: Caesar Cipher

Create a program that allows us to both encrypt and decrypt messages using
the Caesar Cipher (shift cipher).

Named after the famous Roman Emperor Julius Caesar the "Caesar Cipher" (or
'shift cipher') is a type of substitution cipher in which each letter of
the plaintext is 'shifted' and replaced by a letter some fixed number of
positions down the alphabet. For example, with a left shift of 3, D would
be replaced by A, E would become B, and so on.
- Ref: https://en.wikipedia.org/wiki/Caesar_cipher
"""
# construct the reference alphabet
alphabet = [chr(value) for value in range(ord("a"), ord("z") + 1)]

# user inputs
direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the cipher's shift offset: "))


def encrypt(plain_text, shift_amount):
    """use list indexing to implement a 'Caesar' cipher encryption"""
    cipher_length = len(alphabet)
    encoded_text = ""
    for char in plain_text:
        # handle non-alphabetical characters (e.g. spaces / punctuation)
        if char not in alphabet:
            encoded_text += char
        else:
            # calculate the cipher encoded character's look-up reference
            cipher_index = alphabet.index(char) + shift_amount
            # better than using hard-coded "26" >> allows flexibility
            # NOTE: list index starts at 0 (zero)! [hence the "-1"]
            if cipher_index > cipher_length - 1:
                cipher_index -= cipher_length

            encoded_text += alphabet[cipher_index]

    return encoded_text
