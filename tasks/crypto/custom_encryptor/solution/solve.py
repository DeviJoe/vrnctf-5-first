def decrypt(cipher_text: str) -> str:
    ct_list: list[chr] = cipher_text.split(' ')
    curr_number = 1
    primes_list: list[int] = []
    while len(primes_list) != len(cipher_text):
        multipliers = 0
        for i in range(1, curr_number + 1):
            if curr_number % i == 0:
                multipliers += 1
        if multipliers == 2:
            primes_list.append(curr_number)
        curr_number += 1
    plain_text: list[str] = []
    for i in range(0, len(ct_list)):
        plain_text += chr(int(float(str(ord(chr(int(ct_list[i]))) / primes_list[i] / (i + 1)))) // 1)
    return ''.join(plain_text)


if __name__ == '__main__':
    rec_plain = decrypt('236 684 1650 2772 6380 7956 14637 18088 9936 34510 32395 49728 60762 29498 76845 43248 115345 137250')
    print(f"Plain text recovered: {rec_plain}")
