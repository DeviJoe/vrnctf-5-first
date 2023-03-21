from PIL import Image
import sys

print(sys.argv)
if len(sys.argv) != 7:
    print("Incorrect arguments count!")
    print("encoder.py <Input file> <Output file> <Text> <Pixel size> <Start x coordinate> <Start y coordinate>")
    exit()

stringToEncode = sys.argv[3]
pixelSize = int(sys.argv[4])
startX = int(sys.argv[5])
startY = int(sys.argv[6])

textBytes = stringToEncode.encode('ascii')

print("Bytes count:", len(textBytes))

img = Image.open(sys.argv[1])
for i in range(0, len(textBytes)):
    for y in range(0, pixelSize):
        for x in range(0, pixelSize):
            pixX = startX + x + i * pixelSize
            pixY = startY + y
            img.putpixel((pixX, pixY), (0, textBytes[i], 0))
            print("Put byte", (0, textBytes[i], 0), "at", (pixX, pixY))

img.save(sys.argv[2])
print("Saved", sys.argv[2])