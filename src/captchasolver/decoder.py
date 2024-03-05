import numpy as np
import tensorflow as tf
from tensorflow import keras


class CAPTCHADecoder:
    """
    CAPTCHADecoder hanldes decoding the predictions from the model.
    """

    def __init__(self, reverse_char_lookup: keras.layers.StringLookup) -> None:
        """
        Initialize CAPTCHADecoder.

        Args:
            reverse_char_lookup (layers.StringLookup): Reverse character lookup
                                                       to match results to
                                                       respective ASCII values.
        """
        self._reverse_char_lookup = reverse_char_lookup

    def decode_predictions(self, predictions: np.ndarray) -> str:
        """
        Decode a set of predictions from the model into ASCII.

        Args:
            predictions (np.ndarray): The prediction output from the model.

        Returns:
            str: The CAPTCHA answer.
        """
        decoded_predictions = self._perform_ctc_decoding(predictions)
        captcha_answer = self._predictions_to_ascii(decoded_predictions)
        return captcha_answer

    def _perform_ctc_decoding(self, predictions: np.ndarray) -> np.ndarray:
        """
        Performs CTC decoding on the predictions.

        Args:
            predictions (np.ndarray): The prediction output from the model.

        Returns:
            np.ndarray: Decoded predictions.
        """
        input_length = np.ones(predictions.shape[0]) * predictions.shape[1]
        decoded = keras.backend.ctc_decode(
            predictions, input_length=input_length, greedy=True
        )[0][0][:, :1]
        return decoded

    def _predictions_to_ascii(self, decoded_predictions: np.ndarray) -> str:
        """
        Converts decoded predictions to ASCII

        Args:
            decoded_predictions (np.ndarray): Decoded predictions from the
                                              model.

        Returns:
            str: Decoded text.
        """
        text = ""
        for letter in decoded_predictions:
            text += (
                tf.strings.reduce_join(self._reverse_char_lookup(letter))
                .numpy()
                .decode("utf-8")
            )
        return text
