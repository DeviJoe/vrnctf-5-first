import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)


# Иначе это можно реализовать путём вызова функции дешифрования, 
# но с отрицательными коэффициентами в key
def encrypt(msg: str, key: str):
    encrypted = ""

    key_as_list = list(key)
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            index_in_alphabet = lowercase_alphabet.index(c)
            offset = int(key_as_list[i])
            encrypted += lowercase_alphabet[(index_in_alphabet + offset) % len(lowercase_alphabet)]
            i += 1
            continue
        elif c in string.ascii_uppercase:
            index_in_alphabet = uppercase_alphabet.index(c)
            offset = int(key_as_list[i])
            encrypted += uppercase_alphabet[(index_in_alphabet + offset) % len(uppercase_alphabet)]
            i += 1
            continue
        else:
            encrypted += c
            pass
    return encrypted


def decrypt(msg: str, key: str):
    decrypted = ""
    key_as_list = list(key)
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            index_in_alphabet = lowercase_alphabet.index(c)
            offset = int(key_as_list[i])
            alphabet_length = len(uppercase_alphabet)
            decrypted += lowercase_alphabet[(index_in_alphabet - offset) % alphabet_length]
            i += 1
            continue
        elif c in string.ascii_uppercase:
            index_in_alphabet = uppercase_alphabet.index(c)
            offset = int(key_as_list[i])
            alphabet_length = len(uppercase_alphabet)
            decrypted += uppercase_alphabet[(index_in_alphabet - offset) % alphabet_length]
            i += 1
            continue
        else:
            decrypted += c
            continue
    return decrypted


if __name__ == '__main__':
    # Константа из Википедии
    pi = '3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164'
    # И так далее

    key = pi.replace(",", "").replace(" ", "")

    ct = "Wii gqji ox ywvlao{Q07_O4QG_T13Y}"
    t = decrypt(ct, key)
    print(t)
