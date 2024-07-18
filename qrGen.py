import qrcode

def generate_qr_code(data, file_path):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file path
    img.save(file_path)
    print(f"QR code generated and saved to {file_path}")

if __name__ == "__main__":
    data = "https://www.elgiganten.dk/"
    file_path = "qrcode.png"
    generate_qr_code(data, file_path)
