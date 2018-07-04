import cv2
import os

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('Classifiers/face.xml')
i = 0
offset = 50
userId = input('enter your id: ')
name = input('enter your name: ')
folderName = userId + '-' + name
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x, y, w, h) in faces:
        i = i + 1
        os.makedirs("dataSet2/" + folderName, exist_ok=True)
        cv2.imwrite("dataSet2/" + folderName + "/" + userId + '.' + str(i) + "-" + name + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im, (x-50, y-50), (x+w+50, y+h+50), (225, 0, 0), 2)
        cv2.imshow('im', im[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.waitKey(100)
    if i > 20:
        cam.release()
        cv2.destroyAllWindows()
        break

