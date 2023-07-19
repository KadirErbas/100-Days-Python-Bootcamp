import pyqrcode
url = input("Enter url to generate QR Code: ")

qr_code = pyqrcode.create(url) # URL’yi bir QR kodu nesnesine dönüştür
qr_code.svg('qrcode.svg',scale=5)  # QR kodunu bir svg dosyasına kaydet ve ölçeği 5 olarak ayarla