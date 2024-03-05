import base64

import cv2
import numpy as np


class ImageProcessor:
    """
    ImageProcessor is responsible for all image-related processing.
    """

    def __init__(self, letters_per_captcha=5, letter_width=40) -> None:
        """
        Initialize ImageProcessor.

        Args:
            letters_per_captcha (int, optional): Specifies the number of
                                                 letters in each CAPTCHA.
                                                 Defaults to 5.
            letter_width (int, optional): Specifies the width in pixels of
                                          each letter in the CAPTCAH. Defaults
                                          to 40.
        """
        self._letters_per_captcha = letters_per_captcha
        self._letter_width = letter_width

    def decode_image(self, encoded_image: str) -> np.ndarray:
        """
        Decode an image encoded in base64 to an ndarray.

        Args:
            encoded_image (str): The encoded base64 string representing the
                                 image.

        Returns:
            np.ndarray: Matrix representation of image where each cell
                        represents a respective pixel value.
        """
        # Decode the captcha_image_str to it's original binary data.
        decoded_image = base64.b64decode(encoded_image)

        # Ensure that each byte of image data is interpreted as an integer
        # pixel value.
        decoded_image_array = np.frombuffer(decoded_image, np.uint8)

        # Decodes image from a buffer into a matrix representing the image.
        image = cv2.imdecode(decoded_image_array, cv2.IMREAD_COLOR)
        return image

    def split_image(self, image: np.ndarray) -> list[np.ndarray]:
        """
        Split a CAPTCHA image into its individual letters.

        Args:
            image (np.ndarray): CAPTCHA image represented as an ndarray.

        Returns:
            list[np.ndarray]: List of letters represented as ndarrays.
        """
        images = []
        for i in range(self._letters_per_captcha):
            images.append(
                image[:, i * self._letter_width : (i + 1) * self._letter_width]
            )
        return images
