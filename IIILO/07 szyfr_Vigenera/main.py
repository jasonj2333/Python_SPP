text = 'informatyka jest fajna'
key = 'super tajne'

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key, alphabet):
    message = ''
    text = text.upper()
    key = key.upper().replace(' ', '')
    key_len = len(key)
    i = 0

    for char in text:
        if char in alphabet:
            text_index = alphabet.find(char)
            key_index = alphabet.find(key[i % key_len])
            c = (text_index + key_index) % len(alphabet)
            message += alphabet[c]
            i += 1
        else:
            message += char
    return message

def decrypt(text, key, alphabet):
    reversed_key = ''
    for c in key.upper().replace(' ', ''):
        key_index = (len(alphabet) - alphabet.find(c)) % len(alphabet)
        reversed_key += alphabet[key_index]
    return encrypt(text, reversed_key, alphabet)

cipher_text = encrypt(text, key, alphabet)
print(cipher_text)
print(decrypt(cipher_text, key, alphabet))

