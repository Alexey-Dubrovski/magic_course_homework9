# Создайте класс FileSize, который хранит размер файла в байтах.
# Реализуйте методы __add__, __sub__ и __mul__,
# чтобы можно было складывать размеры файлов,
# вычитать их и умножать на целое число для вычисления объема
# нескольких файлов одинакового размера.

class FileSize:
    def __init__(self, size):
        self.size = size

    def __add__(self, other_file):
        if isinstance(other_file, FileSize):
            return FileSize(self.size + other_file.size)
        return NotImplemented

    def __sub__(self, other_file):
        if isinstance(other_file, FileSize):
            sub_result = self.size - other_file.size
            if sub_result < 0:
                raise ValueError('Размер второго файла слишком большой')
            return FileSize(sub_result)
        return NotImplemented

    def __mul__(self, num):
        if isinstance(num, int):
            return FileSize(self.size * num)
        return NotImplemented

    def __str__(self):
        return f'{self.size}'


size_1 = FileSize(150)
size_2 = FileSize(150)
result = size_1 + size_2
print(result)
