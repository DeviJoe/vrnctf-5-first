# Решение

## Алгоритм шифрования

1. Получить список простых чисел вплоть до длины флага.
2. К каждому символу в флаге берётся charcode, умножается на его номер (индекс, увеличенный на 1) и на простое число по индексу текущего числа.

Дешифратор для данной задачи строится в обратную к шифратору.

## Алгоритм расшифровки

1. Получить список простых чисел вплоть до количества цифр шифротекста.
2. Взять каждое число исходного шифротекста разделить на его номер (индекс, увеличенный на 1) и на простое число по индексу текущего числа и получить символ по charcode.
