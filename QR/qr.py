import qrcode as qr
img = qr.make("https://www.youtube.com/@CodeSpire2xz")
img.save("qr.png")