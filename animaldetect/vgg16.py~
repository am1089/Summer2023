import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the VGG16 model
model = VGG16(weights='imagenet')

# Load and preprocess an image
img_path = '/mnt/c/Users/Aditya Mitra/Downloads/Dog1.jpg'  # Replace with the path to your image
img = image.load_img(img_path, target_size=(224, 224))  # VGG16 input size is (224, 224)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make predictions on the image
predictions = model.predict(x)
decoded_predictions = decode_predictions(predictions, top=3)[0]

# Print the predicted labels and probabilities
for label, description, probability in decoded_predictions:
    print(f"{label}: {description} ({probability * 100:.2f}%)")
