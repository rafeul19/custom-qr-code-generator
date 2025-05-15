import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def generate_basic_qr(filepath="input.txt"):
    with open(filepath, "r") as f:
        text = f.readline().strip()
        filename = f.readline().strip()
    img = qrcode.make(text)
    img.save(filename)

def generate_styled_qr(data, filename, logo_path=None):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make()
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(),
        embedded_image_path=logo_path
    )
    img.save(filename)

# Usage:
generate_basic_qr("code 2/input.txt")
generate_styled_qr("https://www.facebook.com", "styled_qr.png", logo_path="Allinlogo22.png")
