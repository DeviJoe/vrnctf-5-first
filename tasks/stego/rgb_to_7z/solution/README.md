# Решение

Усложненная версия таска rgb_to_ascii. Главное отличие в том, что тут в rgb закодированы не ASCII символы флага, а байты 7Z архива. Для решения нужно написать скрипт, который считает красный канал каждого пикселя, и запишет его в файл. В архиве будет 100 текстовых файлов одинаковой длины, внутри одного из которых (в данном случае flag38.txt) будет флаг

Аргументы для file_gen.py (скрипт для создания текстовых файлов со случайным текстом заданной длины и префиксом "Your flag is in another file!"):  
file_gen.py <Output dir> <Text length> <Count>

Аргументы для encoder.py:  
encoder.py <Input file> <Output file> <Input file to hide in rgb> <Pixel size> <Start x coordinate> <Start y coordinate> <Line width>

Аргументы для decoder.py:  
decoder.py <Input file> <Output file> <Pixel size> <Start x coordinate> <Start y coordinate> <End x coordinate> <End y coordinate> <Line width>

Использованная команда для кодирования:  
.\encoder.py .\BlankImage.png .\image.png .\files.7z 1 130 255 300

Для декодирования:  
.\decoder.py .\image.png .\files.7z 1 130 255 286 318 300