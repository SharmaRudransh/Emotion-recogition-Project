# Emotion-recogition-Project
# Emotion Recognition Software

This project utilizes OpenCV and DeepFace to perform real-time emotion detection from a live video feed. The software detects human faces from the webcam, analyzes their emotions, and displays the detected emotion on the screen. Additionally, if the detected emotion is "sad" or "angry," the software prompts the user with a popup asking if they want to hear a joke. If the user responds "Yes," a random joke is displayed.

## Features

- Real-time emotion detection from webcam feed.
- Detects emotions such as happy, sad, angry, surprised, and more.
- Displays a rectangle around the face with the emotion label.
- Popup prompt to ask the user if they want to hear a joke when a sad or angry emotion is detected.
- Shows a random joke if the user clicks "Yes."

## Requirements

Before running the project, make sure you have the following Python libraries installed:

- OpenCV (`opencv-python`)
- DeepFace (`deepface`)
- Tkinter (for creating popups)

You can install the required libraries using pip:

```bash
pip install opencv-python deepface
