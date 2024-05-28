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


def caesar(cipher_mode, input_text, shift_amount):
    """encrypt / decrypt text using "Caesar's Cipher" and shift-offsets"""
    # NOTE: Not all alphabets have 26 characters, we may also want to
    #       permit more complex / combined ciphers (e.g. alpha-numeric)!
    cipher_length = len(alphabet)

    output_text = ""
    for char in input_text:
        # handle non-alphabetical characters (e.g. spaces, punctuation etc.)
        if char not in alphabet:
            output_text += char
        else:
            # NOTE: Using the modulo (%) ensures index values always fall
            #       within the necessary range, since any value that does
            #       not cleanly divide will leave a remainder equivalent to
            #       looping the index reference back around!
            if cipher_mode == 'encode':
                # calculate the cipher-encoded reference for the character
                cipher_index = (alphabet.index(char) +
                                shift_amount) % cipher_length
            elif cipher_mode == 'decode':
                # calculate the cipher-decoded reference for the character
                cipher_index = (alphabet.index(char) -
                                shift_amount) % cipher_length
            else:
                # NOTE: input validation should really be done when it is
                #       collected, looping until valid input accepted and
                #       therefore avoiding the need to throw an exception!
                raise ValueError(
                    f"Direction MUST be either 'encode' OR 'decode': {direction}")

            output_text += alphabet[cipher_index]

    return output_text
