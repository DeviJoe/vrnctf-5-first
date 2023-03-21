from PIL import Image
import sys

if len(sys.argv) != 8:
    print("Incorrect arguments count!")
    print("encoder.py <Input file> <Output file> <Input file to hide in rgb> <Pixel size> <Start x coordinate> <Start y coordinate> <Line width>")
    exit()

fileToEncode = sys.argv[3]
pixelSize = int(sys.argv[4])
startX = int(sys.argv[5])
startY = int(sys.argv[6])
line_width = int(sys.argv[7])

in_file = open(fileToEncode, "rb")
fileBytes = bytearray(in_file.read())
# Добавляем яркий пиксель в конце, что бы конец последовательности был четко виден
fileBytes.append(255)

print("Bytes count:", len(fileBytes))

img = Image.open(sys.argv[1])
for i in range(0, len(fileBytes)):
    line_y = i // line_width
    for y in range(0, pixelSize):
        for x in range(0, pixelSize):
            pixX = startX + x + i * pixelSize - line_y * line_width
            pixY = startY + line_y + y 
            img.putpixel((pixX, pixY), (fileBytes[i], 0, 0))
            print("Put byte", (fileBytes[i], 0, 0), "at", (pixX, pixY))

img.save(sys.argv[2])
print("Saved", sys.argv[2])