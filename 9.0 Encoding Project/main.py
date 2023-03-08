alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
def encode(text, shift, direction):
    result = ""
    shift = shift % 26

    if shift < 0:
        return "shift must be greater than "

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = char_index + shift
            result += alphabet[new_index]
        else:
            result += char

    return result


end = False

while not end:
    print(art.logo)
    input_text = input('Enter your text: \n').lower()
    input_shift = int(input('Enter shift: \n'))
    input_direction = input('Enter direction "encode" or "decode":\n').lower()

    x = encode(input_text, input_shift, input_direction)
    print(x)

    terminate = input('Do you want to quit? "yes" or "no":\n').lower()

    if terminate == 'yes':
        end = True
