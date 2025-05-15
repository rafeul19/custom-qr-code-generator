# custom-qr-code-generator
This Python-based project enables users to generate QR codes from text or URLs, with options ranging from simple QR codes to advanced, styled versions. It utilizes the qrcode library along with additional styling modules to produce both basic and visually appealing QR codes. The project is divided into three parts for different use cases.

Code Overview:
1. Basic QR Code Generator (User Input Based):

    Purpose: Generates a QR code from direct user input via the console.

    Process:

        Takes input for text/URL and desired filename.

        Generates a QR code using qrcode.make().

        Saves the QR code image to the specified filename.

    Usage: Ideal for quick, one-off QR code creation.

import qrcode

text = input("Enter the text or Url to be converted in Qrcode: ")
filename = input("Enter filename to save the qrcode image: ")

def generate_qr_code(text, filename):
    image_qrcode = qrcode.make(text)
    image_qrcode.save(filename)

generate_qr_code(text, filename)

2. QR Code with Styling and Logo Embedding:

    Purpose: Creates both basic and styled QR codes from file input or direct parameters.

    Features:

        Supports reading data from a text file.

        Applies advanced styling (rounded modules, radial gradient colors).

        Allows embedding a logo into the center of the QR code.

    Modules Used:

        StyledPilImage, RoundedModuleDrawer, and RadialGradiantColorMask from qrcode.image.styles.

    Use Case: Suitable for branding and professional applications.

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

3. Basic QR Code Generator (File-Based Input):

    Purpose: Similar to the first example, but uses file input instead of console input.

    Functionality:

        Reads the text/URL and output filename from an external file.

        Generates and saves the QR code accordingly.

    Usage: Useful for batch processing or automated scripts.

import qrcode

def generate_qr_code(filepath="input.txt"):
    with open(filepath, "r") as file:
        lines = file.readlines()
    text = lines[0].strip()
    filename = lines[1].strip()
    image_qrcode = qrcode.make(text)
    image_qrcode.save(filename)

generate_qr_code("code 2/input.txt")

Conclusion:

This QR code generator project provides both basic and advanced capabilities for converting text or URLs into QR code images. It demonstrates versatility in input methods and output customization, making it useful for personal, academic, or business applications.
