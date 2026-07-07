import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load trained model
model = load_model("mnist_model.keras")

def predict_digit(image_path):
    image = Image.open(image_path).convert("L")
    image = image.resize((28, 28))

    image = np.array(image)
    image = 255 - image
    image = image / 255.0

    image = image.reshape(1, 28, 28, 1)

    prediction = model.predict(image)

    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    return digit, confidence