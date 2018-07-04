import cv2
import os
import numpy as np
from PIL import Image 

recognizer = cv2.face.LBPHFaceRecognizer_create() #cv2.createLBPHFaceRecognizer()
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
path2 = 'dataSet2'

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]

    folder_paths = [os.path.join(path2, f) for f in os.listdir(path2)]
    files = []
    counter = 0
    for folderImg in folder_paths:
        counter = counter + 1
        if folderImg == 'dataSet2/.DS_Store':
            continue
        files.extend([os.path.join(folderImg, f) for f in os.listdir(folderImg)])
#        if counter > 10:
#            break
    #print(files)


    #print(image_paths2)
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    counter = 0
    totalImage = len(files)
    print(str(counter) + " of " + str(totalImage))
    for image_path in files:
        counter = counter + 1
        if image_path == 'dataSet2/.DS_Store':
            continue
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        userId = int(os.path.split(image_path)[1].split("-")[0].split(".")[0])
        #print(image_path)
        #userId=int(''.join(str(ord(c)) for c in userId))
        #print(userId)
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(userId)
            cv2.imshow("Adding faces to traning set... ", image[y: y + h, x: x + w])
            cv2.waitKey(10)
        print(str(counter) + " of " + str(totalImage))
     # return the images list and labels list
    return images, labels
#print('path:')
#print(path)
images, labels = get_images_and_labels(path)
cv2.imshow('test',images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.save('trainer/trainer.yml')
cv2.destroyAllWindows()
