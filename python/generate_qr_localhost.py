import qrcode
import argparse

def generate_qr_code(text : str, filename="qrcode.png"):

    qr = qrcode.QRCode(
        version=1,            # Controls the size of the QR code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Error correction level
        box_size=10,          # Size of each box in the QR code
        border=4              # Border width (default is 4)
    )

    # Add text data to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a QR code from a given text.")
    parser.add_argument("text", type=str, help="Text to encode into the QR code")
    parser.add_argument("-f", "--filename", type=str, default="qrcode.png", help="Output filename for the QR code image")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate the QR code with provided text and filename
    generate_qr_code(args.text, args.filename)

if __name__ == "__main__":
    main()
