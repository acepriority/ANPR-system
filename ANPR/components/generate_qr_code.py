import qrcode
from io import BytesIO


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    image_stream = BytesIO()
    img.save(image_stream, format="PNG")
    image_data = image_stream.getvalue()

    return image_data
