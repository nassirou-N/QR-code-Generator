import pyqrcode


def qrcode():
    query = pyqrcode.create(input("entre qr mot:\n"))
    query.png('qrcode.png',scale=6)
    print('QR code genereted')


if __name__ == '__main__':
    qrcode()


# install pyqrcode
# install pypng
