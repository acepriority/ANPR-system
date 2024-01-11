"""
Load the TensorFlow model from the specified path.

Args:
    model_path (str): The path to the saved model.

Returns:
    tf.keras.Model: Loaded TensorFlow model.

Raises:
    ValueError: If there is an error loading the model.

Notes:
    - Make sure to provide the correct model path when creating an instance of this class.
    - Handle the loaded_model accordingly based on your application requirements.
"""





import tensorflow as tf


class ModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path

    def load_model(self):
        try:
            loaded_model = tf.keras.models.load_model(self.model_path)
            return loaded_model
        except Exception as e:
            raise ValueError(f"Error loading model: {str(e)}")

