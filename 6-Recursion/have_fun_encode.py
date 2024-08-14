def encode_message(message, shift):
    encoded_chars = []
    temp = 0
    for i, char in enumerate(message):
        if 'a' <= char <= 'z':
            base = ord('a')
            new_char = chr((ord(char) - base + shift + i + temp) % 26 + base)
            if new_char == char:
                new_char = chr((ord(new_char) - base + 1) % 26 + base)
                temp += 1
            encoded_chars.append(new_char)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            new_char = chr((ord(char) - base + shift + i + temp) % 26 + base)
            if new_char == char:
                new_char = chr((ord(new_char) - base + 1) % 26 + base)
                temp += 1
            encoded_chars.append(new_char)
        else:
            encoded_chars.append(char)
    return ''.join(encoded_chars)

def decode_message(encoded_message, shift):
    decoded_chars = []
    temp = 0
    for i, char in enumerate(encoded_message):
        if 'a' <= char <= 'z':
            base = ord('a')
            original_char = chr((ord(char) - base - shift - i - temp) % 26 + base)
            if original_char == char:
                original_char = chr((ord(original_char) - base - 1) % 26 + base)
                temp += 1
            decoded_chars.append(original_char)
        elif 'A' <= char <= 'Z':
            base = ord('A')
            original_char = chr((ord(char) - base - shift - i - temp) % 26 + base)
            if original_char == char:
                original_char = chr((ord(original_char) - base - 1) % 26 + base)
                temp += 1
            decoded_chars.append(original_char)
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

# Main program
print("This is Caesar cipher")
message, initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:", encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)