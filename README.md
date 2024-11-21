# Project By Rudransh Sharma
# Emotion Recognition Software with joke feature if angry or sad

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


Here is a sample README.md file for your Emotion Recognition Software to use on GitHub:

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
Note: Tkinter is pre-installed with Python, so you do not need to install it separately.

## How to Use
Clone the repository:

Clone this repository to your local machine:

bash
##  git clone https://github.com/your-username/emotion-recognition.git
cd emotion-recognition
 Run the emotion recognition script:

After ensuring the dependencies are installed, run the following command to start the software:

bash
python emotion_joke_detection.py
## Interacting with the Software:

The software will start capturing video from your webcam.
It will analyze the emotions on the faces in the frame.
If the detected emotion is either "sad" or "angry," a popup will appear asking if you want to hear a joke.
If you click "Yes," a random joke will be displayed in another popup window.
## Exit the Program:

Press the "q" key in the webcam window to stop the program and close all windows.
 ## Code Explanation
Face Detection: The software uses OpenCV's Haar Cascade Classifier (haarcascade_frontalface_default.xml) to detect faces in the webcam video stream.
Emotion Recognition: The DeepFace library is used to analyze facial expressions and detect the dominant emotion from the face.
Popup for Jokes: The program uses the Tkinter library to create a popup window asking the user if they want to hear a joke when the detected emotion is sad or angry.
## Sample Output
When running the software, the webcam feed will show the face detection results, and any detected emotion will be labeled on the screen. If a sad or angry emotion is detected, a popup will appear asking if you'd like to hear a joke.

## Contributing
If you have suggestions or improvements for this project, feel free to fork the repository and submit a pull request. If you encounter any bugs or issues, please create an issue in the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
All rights are Reserved To Rudransh Sharma

## Acknowledgments
OpenCV: Open Source Computer Vision Library for real-time computer vision.
DeepFace: A Python library for deep learning-based facial recognition and analysis.
Tkinter: Standard Python library for creating graphical user interfaces.
