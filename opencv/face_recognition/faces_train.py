import os
import cv2 as opcv
import numpy as np


haar_cascade = opcv.CascadeClassifier('../facedetection/haar_face.xml')
people = ['Ben Afflek', 'Elton John',
          'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'Faces/train'

features = []
labels = []


def create_train():
    # to locate faces in dataset and trim their faces as needed.
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = opcv.imread(img_path)
            gray = opcv.cvtColor(img_array, opcv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done----------')
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = opcv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)
