import base64


def convert_image_to_base64(image_path: str) -> str:
    """
    Return the base64 encoding of an image.

    Args:
        image_path (str): Path to the image.

    Returns:
        str: The base64 encoding of the image.
    """
    with open(image_path, "rb") as image:
        binary_data = image.read()
    encoded_image = base64.b64encode(binary_data)
    encoded_image_str = encoded_image.decode("utf-8")
    return encoded_image_str


image_path = "./test_captcha.png"
encoded_image = convert_image_to_base64(image_path)  # Answer is "2ag2h"
