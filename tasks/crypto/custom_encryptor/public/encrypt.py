def encrypt(plain_text: str) -> str:
    sth1 = 1
    lst1: list[int] = []
    while len(lst1) != len(plain_text):
        sth2 = 0
        for i in range(1, sth1 + 1):
            if sth1 % i == 0:
                sth2 += 1
        if sth2 == 2:
            lst1.append(sth1)
        sth1 += 1
    lst2: list[chr] = list(plain_text)
    sth_str: list[str] = list(plain_text)
    for i in range(0, len(plain_text)):
        sth_str[i] = str(ord(lst2[i]) * lst1[i] * (i + 1))
    return ' '.join(sth_str)
