import cv2
import numpy as np
import os
import time
from pynput.mouse import Button, Controller

recognizer = cv2.face.LBPHFaceRecognizer_create()
print("Attempting to read trainner.yml...")
recognizer.read('trainner/trainner.yml')
print("Finished reading trainner.yml.")

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

os.system("START.mp3")
cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX
alert_duration = 10
alert_triggered = False
unknown_time = 0

def sayIt(name):
    print(f'[+] Playing audio: {name}')
    os.system("start " + name)

def draw_rounded_rectangle(img, pt1, pt2, color, alpha=0.5):
    overlay = img.copy()
    cv2.rectangle(overlay, pt1, pt2, color, -1)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

def draw_text(img, text, position, font, color, size=1, thickness=2):
    cv2.putText(img, text, position, font, size, color, thickness, cv2.LINE_AA)

def add_frame_effects(img):
    shadow = img.copy()
    shadow = cv2.GaussianBlur(shadow, (21, 21), 0)
    img[0:img.shape[0], 0:img.shape[1]] = cv2.addWeighted(shadow, 0.1, img, 1, 0)

print("[INFO] Starting face recognition...")
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    unknown_detected = False

    for (x, y, w, h) in faces:
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        print(f"[INFO] Confidence Level = {conf:.2f}")

        if conf < 61:
            if Id == 1:
                Id = "MASTER"
                color = (0, 255, 0)
            elif Id == 2:
                Id = "USER1"
                color = (255, 165, 0)
            elif Id == 3:
                Id = "USER2"
                color = (0, 0, 255)
            elif Id == 4:
                Id = "USER3"
                color = (75, 0, 130)
            elif Id == 5:
                Id = "USER4"
                color = (255, 20, 147)
            elif Id == 6:
                Id = "USER5"
                color = (128, 0, 128)
            else:
                Id = "Unknown"
                unknown_detected = True
                color = (0, 0, 255)

            alert_triggered = False
            unknown_time = 0
            print(f"[INFO] Welcome {Id}!")
        else:
            Id = "Unknown"
            unknown_detected = True
            print("[WARNING] Unknown user detected!")

        draw_rounded_rectangle(im, (x - 10, y - 40), (x + w + 10, y), (0, 0, 0), alpha=0.7)
        draw_text(im, str(Id), (x + 5, y - 10), font, color, size=1, thickness=2)

        cv2.rectangle(im, (x, y), (x + w, y + h), color, 2)
        alpha = 0.3 + 0.2 * np.abs(np.sin(time.time()))
        draw_rounded_rectangle(im, (x - 5, y - 5), (x + w + 5, y + h + 5), color, alpha)

    if unknown_detected:
        unknown_time += 1
        print(f"[INFO] Unknown user detected for {unknown_time / 10:.1f} seconds.")
        
        if unknown_time >= alert_duration * 10:
            if not alert_triggered:
                print("[ALERT] Unknown user detected continuously for 10 seconds!")
                sayIt("alert.mp3")
                alert_triggered = True
                print("[ALERT] Alert sound played.")
    else:
        unknown_time = 0

    current_time = time.strftime("%H:%M:%S")
    draw_text(im, current_time, (10, 30), font, (0, 255, 255), size=1, thickness=2)

    add_frame_effects(im)

    cv2.imshow('Face Recognition', im)

    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
print("[INFO] Face recognition ended.")
