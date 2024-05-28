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
# can't be bothered to create and import the art as a module!
logo = r'''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''

# construct the reference alphabet
alphabet = [chr(value) for value in range(ord("a"), ord("z") + 1)]


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
            else:  # cipher_mode == 'decode':
                # calculate the cipher-decoded reference for the character
                cipher_index = (alphabet.index(char) -
                                shift_amount) % cipher_length

            output_text += alphabet[cipher_index]

    return output_text


def get_user_input(prompt, accepted_values, default=None):
    """generic function to obtain user input with minimal validation"""
    if default:
        default = str(default)
        if default not in accepted_values:
            raise ValueError("Default value NOT in accepted values!")

    user_input = None
    while user_input not in accepted_values:
        user_input = input(prompt)
        if user_input.strip() == "" and default is not None:
            user_input = default

    return user_input


def get_numeric_input(prompt, default=None):
    """function to obtain numerical user input with minimal validation
    NOTE: no type conversion is performed by this function, it simply
    asserts that a user input "is numeric" -- i.e. str.isnumeric()
    """
    if default and not str(default).isnumeric():
        raise TypeError(
            'Parameter "default" MUST be numeric or a numeric string: ' +
            f'"{default}"'
        )

    user_input = None
    while not user_input or not str(user_input).isnumeric():
        user_input = input(prompt)
        if user_input.strip() == "" and default is not None:
            user_input = default

    return user_input


print(logo)
# main program loop
while True:
    # get user inputs
    direction = get_user_input(
        "Type 'encode' to encrypt or 'decode' to decrypt:\n",
        ['encode', 'decode']
    )
    text = input("Type your message:\n").lower()  # needs no validation
    shift = int(get_numeric_input("Type the cipher's shift offset: "))

    print(caesar(direction, text, shift))

    # allow user to break out of the program loop
    rerun = get_user_input(
        "\nType 'yes' to continue or 'no' to exit: ",
        ['yes', 'no']
    )
    if rerun == 'no':
        break
