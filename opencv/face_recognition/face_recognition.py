import numpy as np
import cv2 as opcv

haar_cascade = opcv.CascadeClassifier('../facedetection/haar_face.xml')

people = ['Ben Afflek', 'Elton John',
          'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = opcv.face.LBPHFaceRecognizer_create()
face_recognizer.read('faces_trained.yml')

img = opcv.imread('Faces/val/ben_afflek/1.jpg')

gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)
opcv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[lable]} with a confidence of {confidence}')

    opcv.putText(img, str(people[label]), (20, 20),
                 opcv.FONT_HERSHY_COMPLEX, 1.0, (0, 255, 0), thickness=2)

    opcv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
opcv.imshow('Detected Face', img)
opcv.waitKey(0)
