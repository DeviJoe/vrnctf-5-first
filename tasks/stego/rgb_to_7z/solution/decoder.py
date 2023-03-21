from PIL import Image
import sys
import os

if len(sys.argv) != 9:
    print("Incorrect arguments count")
    print("decoder.py <Input file> <Output file> <Pixel size> <Start x coordinate> <Start y coordinate> <End x coordinate> <End y coordinate> <Line width>")
    exit()

output_file = sys.argv[2]
pixelSize = int(sys.argv[3])
startX = int(sys.argv[4])
startY = int(sys.argv[5])
endX = int(sys.argv[6])
endY = int(sys.argv[7])
line_width = int(sys.argv[8])

fileBytes = bytearray([])

img = Image.open(sys.argv[1])
for i in range(0, endX - startX + (endY - startY) * line_width, pixelSize):
    x = startX + i % line_width
    y = startY + i // line_width
    byte = img.getpixel((x, y))
    fileBytes.append(byte[0])
    print(f"Got byte {byte[0]:03d} at {x}, {y}")

with open(output_file, 'wb') as f:
    f.write(bytes(fileBytes))

print(f"Written in {output_file}")