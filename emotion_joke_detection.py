import cv2
from deepface import DeepFace
import tkinter as tk
from tkinter import messagebox
import random

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to show popup and ask for joke
def ask_for_joke():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create a popup asking if the user wants to hear a joke
    answer = messagebox.askquestion("Want to hear a joke?", "Do you want to hear a joke?", icon='question')

    # If the user clicks 'Yes', show a joke
    if answer == 'yes':
        joke = get_joke()
        messagebox.showinfo("Here's a Joke!", joke)

# Function to fetch a random joke
def get_joke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "Why don’t oysters donate to charity? Because they are shellfish.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I asked my dog what’s two minus two. He said nothing.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out."
    ]
    return random.choice(jokes)

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']

        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # If the emotion is sad or angry, ask if the user wants to hear a joke
        if emotion in ['sad', 'angry']:
            ask_for_joke()

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
