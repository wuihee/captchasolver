from tensorflow import keras

from .constants import CHARACTERS
from .dataset_creator import DatasetCreator
from .decoder import CAPTCHADecoder
from .image_processor import ImageProcessor


class CAPTCHASolver:
    """
    CAPTCHASolver solves simple image CAPTCHAs.
    """

    def __init__(self, model_path: str, vocabulary=CHARACTERS) -> None:
        """
        Initialize CAPTCHASolver.

        Args:
            model_path (str): Path to prediction model.
            vocabulary (list[str], optional): List of all possible letters in
                                              the CAPTCHA. Defaults to
                                              CHARACTERS.
        """
        self._model = keras.models.load_model(model_path)
        self._image_processor = ImageProcessor()
        self._dataset_creator = DatasetCreator()
        self._decoder = CAPTCHADecoder(
            keras.layers.StringLookup(
                vocabulary=vocabulary, mask_token=None, invert=True
            )
        )

    def solve(self, encoded_image: str) -> str:
        """
        Solve a CAPTCHA.

        Args:
            encoded_image (str): CAPTCHA image encoded in base64.

        Returns:
            str: The CAPTCHA answer.
        """
        image = self._image_processor.decode_image(encoded_image)
        letters = self._image_processor.split_image(image)
        dataset = self._dataset_creator.create_dataset(letters)
        predictions = self._model.predict(dataset)
        captcha_answer = self._decoder.decode_predictions(predictions)
        return captcha_answer
