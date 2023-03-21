from PIL import Image
import sys

if len(sys.argv) != 6:
    print("Incorrect arguments count")
    print("decoder.py <Input file> <Pixels count> <Pixel size> <Start x coordinate> <Start y coordinate>")
    exit()

byteCount = int(sys.argv[2])
pixelSize = int(sys.argv[3])
startX = int(sys.argv[4])
startY = int(sys.argv[5])

textBytes = bytearray([])

img = Image.open(sys.argv[1])
for i in range(0, byteCount * pixelSize, pixelSize):
    byte = img.getpixel((startX + i, startY))
    textBytes.append(byte[1])
    print("Got byte", byte[1])

print("Result:")
print(textBytes.decode("ascii"))