# Решение

Нужно заметить, что в полоске из пикселей в центре изображения используется только зеленый канал RGB. Величина этого канала в каждом пикселе - ASCII код символа флага. Для упрощения один код был не в одном пикселе, а в квадрате 5x5 пикселей

Аргументы для encoder.py:  
encoder.py <Input file> <Output file> <Text> <Pixel size> <Start x coordinate> <Start y coordinate>

Аргументы для decoder.py:  
decoder.py <Input file> <Pixels count> <Pixel size> <Start x coordinate> <Start y coordinate>

Использованная команда для кодирования:  
.\encoder.py .\BlankImage.png .\Image.png vrnctf{r6b_fr35c0} 5 229 287

Для декодирования:  
.\decoder.py .\Image.png 25 5 229 287