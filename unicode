import string
import random
n = random.randint(10, 99)
m = random.randint(10, 99)
def encode(text, key1, key2):
    encoded_text = ""
    for char in text:
        encoded_char = ord(char) + key1 # shift each character by 3 positions
        if encoded_char > 127: # wrap around if the shifted value is outside the ASCII range
            encoded_char -= 94
        encoded_text += chr(encoded_char)
    return encoded_text
def decode(encoded_text, key1, key2):
    decoded_text = ""
    for char in encoded_text:
        decoded_char = ord(char) - key1 # shift each character back by 3 positions
        if decoded_char < 33: # wrap around if the shifted value is outside the ASCII range
            decoded_char += 94
        decoded_text += chr(decoded_char)
    return decoded_text
encoded_text = encode('mediafire', n,m)
print('Text: ' + encoded_text + ' Password: ' + str(n)+str(m))
decoded_text = decode(encoded_text, n, m)
print(decoded_text)
