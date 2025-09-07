import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://www.youtube.com/@CodeSpire2xz")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="green")
img.save("Customm.png")