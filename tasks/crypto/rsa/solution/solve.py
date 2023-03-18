from Crypto.Util.number import long_to_bytes, inverse
from factordb.factordb import FactorDB


def decrypt(c, p, q, exponent):
    # Вычисление фи по формуле Эйлера
    phi = (p - 1) * (q - 1)
    # Вычисление n
    n = p * q
    # Вычисление элемента (d) приватного ключа
    d = inverse(exponent, phi)
    # Расшифрование шифротекста.
    m = pow(c, d, n)
    return long_to_bytes(m)


if __name__ == '__main__':
    n = 65489316517760964817551290061367919641018086931735345641980121467508282286511
    e = 65537
    ct = 48590290469775795984316818242447556425920095864272111358986793298343462199442
    # Либо просто через браузер открыть FactorDB и скопировать оба множителя
    f = FactorDB(n)
    f.connect()
    factors: list = f.get_factor_list()

    print(str(decrypt(ct, factors[0], factors[1], e), "utf-8"))
