# Hand Gesture Recognition Project
This project focuses on recognizing different hand gestures such as call, rock, like, and peace using computer vision and machine learning techniques. The project utilizes tools like MediaPipe and OpenCV for real-time hand tracking and gesture recognition.

# Project Workflow
## 1. Data Preprocessing
### Preprocess the Dataset:
Cleaned and filtered the dataset to select only useful images.
Converted the images to RGB format using OpenCV.
Structured the images into a dictionary containing data and labels (from 0 to n).

## 2. Model Training
Load the Preprocessed Data:
Load the data from the pickle file.
Train a RandomForestClassifier using the preprocessed data.

## 3. Real-Time Gesture Recognition
### Load the Trained Model:
Load the model from the pickle file.
Open the camera using OpenCV.
Use MediaPipe for hand tracking and gesture recognition.
Display the recognized gesture on the screen.

### Tools and Technologies
OpenCV: For image processing and camera interfacing.
MediaPipe: For real-time hand tracking and landmark detection.
Scikit-learn: For training the machine learning model.
Pickle: For saving and loading preprocessed data and trained models.
Usage Instructions

### Preprocess your dataset: 
Follow the data preprocessing steps to prepare your images and labels.
### Train the model: 
Use the provided code to train the RandomForestClassifier on your preprocessed data.
### Run the real-time recognition: 
Execute the real-time recognition script to start recognizing hand gestures using your webcam.

### This project uses the following libraries:
OpenCV
MediaPipe
Scikit-learn
Pickle
