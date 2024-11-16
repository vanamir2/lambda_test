import argparse

import qrcode
from io import BytesIO
import base64

def generate_qr_code(text):
    """
    Generates a QR code for the given text and returns it as a binary image.

    Parameters:
    - text (str): The text to encode into the QR code.

    Returns:
    - bytes: PNG image of the QR code.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO stream
    buffered = BytesIO()
    img.save(buffered)
    print(f"QR code generated for text: {buffered.getvalue()}")
    return buffered.getvalue()

def handler(event, context):
    """
    AWS Lambda handler function.

    Parameters:
    - event (dict): The event data passed by AWS Lambda.
    - context (object): The context in which the Lambda function is called.

    Returns:
    - dict: The response containing the PNG image for download.
    """
    # Get the 'text' parameter from the query string
    text = event.get("queryStringParameters", {}).get("text", "")

    if not text:
        return {
            'statusCode': 400,
            'body': 'Missing "text" query parameter'
        }

    # Generate the QR code as a PNG image
    qr_image = generate_qr_code(text)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/png',
            'Content-Disposition': 'attachment; filename="qrcode.png"'
        },
        'body': base64.b64encode(qr_image).decode('utf-8'),
        'isBase64Encoded': True
    }

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a QR code from a given text.")
    parser.add_argument("text", type=str, help="Text to encode into the QR code")
    parser.add_argument("-f", "--filename", type=str, default="qrcode.png", help="Output filename for the QR code image")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate the QR code with provided text and filename
    generate_qr_code(args.text)

if __name__ == "__main__":
    main()