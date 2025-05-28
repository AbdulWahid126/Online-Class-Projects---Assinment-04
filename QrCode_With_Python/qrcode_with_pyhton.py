import qrcode

data = 'How Are You?'

img = qrcode.make(data)

img.save('D:/My Privious All Data/GUIAI Quarter 03/Online Class Projects/QrCode_With_Python/Qr-codes/qrCode2.png')