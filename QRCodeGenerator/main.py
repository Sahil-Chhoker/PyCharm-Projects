import qrcode as qr

links = [["YouTube", "https://www.youtube.com/"]]

for link in links:
    img = qr.make(link[1])
    img.save(f"D:\Pycharm\PyCharm-Projects\QRCodeGenerator\QrCodes\{link[0]}.png")