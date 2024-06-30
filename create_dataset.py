# importing the packages
import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

# creating the objects of mediapipe for hand recognition
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# setting the dataset directory path
DATA_DIR = "./data"

data = []
labels = []

# iterating over all images in each sub-directories for each type
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        # converting the image into rgb using cv
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # processing the rgb in hands of mp
        results = hands.process(img_rgb)

        # processing all 21 landmarks in the hand
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    # storing the normalized x and y values
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            # creating the dataset using the normalised x and y values
            data.append(data_aux)
            # setting the label
            labels.append(dir_)

# storing the dataset into a pickle file
f = open("data.pickle", "wb")
pickle.dump({"data": data, "labels": labels}, f)
f.close()
