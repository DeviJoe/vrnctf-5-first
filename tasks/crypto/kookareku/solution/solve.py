"""
Код на самом деле приложен, чтобы показать, что эту задачу возможно сделать через него.
Вряд-ли кто-то из участников будет его писать.

Brainfuck Interpreter source: https://github.com/c-sant/brainfuck-in-python
"""

import numpy as np


class BrainfuckException(Exception):
    """
    Base Brainfuck exception.
    """


class Brainfuck:
    def __init__(self, memory_size: int = 30000, safe: bool = True):
        if memory_size < 0:
            raise ValueError('Memory size cannot be negative')

        self._data = np.array([0] * memory_size)
        self._data = self._data.astype(np.ubyte)
        self.safe = safe

    @property
    def data(self):
        return self._data

    def run_file(self, file_path: str):
        if not file_path.endswith('.b') and not file_path.endswith('.bf'):
            self.__report_error('Invalid file')

        with open(file_path, 'r') as f:
            code = f.read()

        self.run(code)

    def prompt(self):
        while True:
            value = input('> ').lower().strip()
            if value == '/quit':
                return

            self.run(value)

    def run(self, code):
        had_error = self.__evaluate(code)

        if had_error:
            return

        self.__interpret(code)

    def __report_error(self, message: str, line: int = None, column: int = None):
        if line is None or column is None:
            print(f'[Brainfuck] exception: {message}')
        else:
            print(f'[Brainfuck] exception at line {line} char {column}: {message}')

        if not self.safe:
            raise BrainfuckException(message)

    def __evaluate(self, source: str):
        line = col = 0

        stk = []

        for c in source:
            match c:
                case '[':
                    stk.append('[')
                case ']':
                    if len(stk) == 0:
                        self.__report_error("Unexpected token ']'", line, col)
                        return True

                    stk.pop()
                case '\n':
                    line += 1
                    col = -1
                case _:
                    pass
            col += 1

        if len(stk) != 0:
            self.__report_error("Unmatched brackets")
            return True

        return False

    def __interpret(self, source: str):
        line = col = ptr = current = 0

        while current < len(source):
            match source[current]:
                case '>':
                    if ptr == (len(self.data) - 1):
                        self.__report_error("Pointer out of range", line, col)
                        return True

                    ptr += 1
                case '<':
                    if ptr == 0:
                        self.__report_error("Pointer out of range", line, col)
                        return True

                    ptr -= 1
                case '+':
                    if self.data[ptr] == 255:
                        self.__report_error("Cell overflow")
                        return True

                    self.data[ptr] += 1

                case '-':
                    if self.data[ptr] == 0:
                        self.__report_error("Cell underflow")
                        return True

                    self.data[ptr] -= 1
                case '.':
                    print(chr(self.data[ptr]), end="")
                case ',':
                    value = input()
                    if not value.isdigit():
                        self.__report_error("Invalid input")

                    self.data[ptr] = np.ubyte(value)
                case '[':
                    if self.data[ptr] == 0:
                        while source[current] != ']':
                            current += 1
                case ']':
                    if self.data[ptr] != 0:
                        while source[current] != '[':
                            current -= 1
                case '\n':
                    line += 1
                    col = -1
                case _:
                    pass

            col += 1
            current += 1

        return False


def petooh_to_bf(message: str):
    res = message
    res = res.replace("Kukarek", ".")
    res = res.replace("Kudah", ">")
    res = res.replace("kudah", "<")
    res = res.replace("Ko", "+")
    res = res.replace("kO", "-")
    res = res.replace("Kud", "[")
    res = res.replace("kud", "]")
    res = res.replace(" ", "")
    res = res.replace("\n", "")
    return res


# Функция, которая на вход принимает код на языке PETOOH,
# под капотом преобразует его в Brainfuck и выводит текст в консоль.
def solve(msg: str):
    bf_text = petooh_to_bf(msg)
    bf = Brainfuck(30000, True)
    bf.run(bf_text)
