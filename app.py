from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('cat_dog_classifier.h5')
  # Replace with your trained model path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded!', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected!', 400

    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # Preprocess the image
    img = load_img(file_path, target_size=(224, 224))  # Resize to 224x224
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    prediction = model.predict(img_array)
    class_label = 'Dog' if prediction[0][0] > 0.5 else 'Cat'

    return render_template('result.html', label=class_label, image_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
