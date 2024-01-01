import numpy as np
import tensorflow as tf


class DatasetCreator:
    """
    DatasetCreator handles the creation of a TensorFlow dataset.
    """

    def create_dataset(self, images: list[np.ndarray]) -> tf.data.Dataset:
        """
        Create a dataset that from the CAPTCHA that the prediciton model can
        take.

        Args:
            images (list[np.ndarray]): List of arrays representing individual
                                       CAPTCHA letters.

        Returns:
            tf.data.Dataset: Dataset to be passed into the prediction model.
        """
        dataset = tf.data.Dataset.from_tensor_slices(images)
        dataset = (
            dataset.map(
                self._encode_letter, num_parallel_calls=tf.data.AUTOTUNE
            )
            .batch(16)
            .prefetch(buffer_size=tf.data.AUTOTUNE)
        )
        return dataset

    @staticmethod
    def _encode_letter(image: np.ndarray) -> tf.Tensor:
        """
        Helper method used to convert an image into a required tensor.

        Args:
            image (np.ndarray): ndarray of a single CAPTCHA letter.

        Returns:
            tf.Tensor: The processed tensor to be fed to the model.
        """
        tensor = tf.convert_to_tensor(image, dtype=tf.uint8)
        tensor = tf.image.rgb_to_grayscale(tensor)
        tensor = tf.image.convert_image_dtype(tensor, tf.float32)
        tensor = tf.transpose(tensor, perm=[1, 0, 2])
        return tensor
