# Cat and Dog Classifier

This project is a web application that classifies images uploaded by users as either a cat or a dog. It uses a pre-trained MobileNetV2 model and is built using Flask for the backend.

## Features

- Upload an image through a user-friendly web interface.
- Classify the uploaded image as a **Cat** or **Dog**.
- Display the classification result on the webpage.

## Project Structure


## Prerequisites

Ensure you have the following installed on your system:
- Python 3.6 or higher
- Pip (Python package installer)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CatDogClassifier.git
   cd CatDogClassifier

pip install flask tensorflow pillow

python app.py

http://127.0.0.1:5000/

How It Works
The user uploads an image via the web interface.
The app preprocesses the image to match the input requirements of the pre-trained MobileNetV2 model.
The model predicts the category of the image (Cat or Dog).
The result is displayed to the user.


Technologies Used
Backend: Flask (Python)
Frontend: HTML
Machine Learning Framework: TensorFlow/Keras (MobileNetV2)
Future Enhancements
Deploy the app on a cloud platform like Heroku or AWS.
Add better styling to the web interface.
Expand the classifier to identify multiple categories or dog breeds.
