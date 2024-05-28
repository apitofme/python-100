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
    """encrypt plain-text using "Caesar's Cipher" by adding the shift"""
    cipher_length = len(alphabet)
    encoded_text = ""
    for char in plain_text:
        # handle non-alphabetical characters (e.g. spaces / punctuation)
        if char not in alphabet:
            encoded_text += char
        else:
            # calculate the cipher-encoded reference for the character
            cipher_index = alphabet.index(char) + shift_amount
            # keep the look-up reference within the cipher's range
            # NOTE: better than using hard-coded "26" >> allows flexibility
            #       + list index starts at 0 (zero)! [hence the "-1"]
            if cipher_index > cipher_length - 1:
                cipher_index -= cipher_length

            encoded_text += alphabet[cipher_index]

    return encoded_text


def decrypt(cipher_text, shift_amount):
    """decrypt cipher-text using "Caesar's Cipher" by removing the shift"""
    cipher_length = len(alphabet)
    decoded_text = ""
    for char in cipher_text:
        # handle non-alphabetical characters (e.g. spaces / punctuation)
        if char not in alphabet:
            decoded_text += char
        else:
            # calculate the cipher-decoded reference for the character
            cipher_index = alphabet.index(char) - shift_amount
            # keep the look-up reference within the cipher's range
            if cipher_index > cipher_length - 1:
                cipher_index -= cipher_length

            decoded_text += alphabet[cipher_index]

    return decoded_text


# allow user to encode or decode messages
if direction == 'encode':
    print(encrypt(text, shift))
elif direction == 'decode':
    print(decrypt(text, shift))
else:
    raise ValueError(
        f"Direction MUST be either 'encode' OR 'decode': {direction}")
