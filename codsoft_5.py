import cv2
import tkinter as tk
from tkinter import filedialog

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces_webcam():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_with_faces = detect_faces(frame)
        cv2.imshow('Face Detection in Webcam', frame_with_faces)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def detect_faces_in_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        frame_with_faces = detect_faces(image)
        cv2.imshow('Face Detection in Image', frame_with_faces)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def detect_faces_in_video():
    file_path = filedialog.askopenfilename()
    if file_path:
        video_capture = cv2.VideoCapture(file_path)
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            frame_with_faces = detect_faces(frame)
            cv2.imshow('Face Detection in Video', frame_with_faces)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image

root = tk.Tk()
root.title("Face Detection")

button_webcam = tk.Button(root, text="Detect Faces in Webcam", command=detect_faces_webcam)
button_webcam.pack(pady=5)

button_image = tk.Button(root, text="Detect Faces in Image", command=detect_faces_in_image)
button_image.pack(pady=5)

button_video = tk.Button(root, text="Detect Faces in Video", command=detect_faces_in_video)
button_video.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.pack(pady=5)

root.mainloop()
