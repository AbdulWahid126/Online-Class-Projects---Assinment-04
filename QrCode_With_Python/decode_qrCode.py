from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('D:/My Privious All Data/GUIAI Quarter 03/Online Class Projects/QrCode_With_Python/Qr-codes/qrCode2.png')

result = decode(img)

print(result)