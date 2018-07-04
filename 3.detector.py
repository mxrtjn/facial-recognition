import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
recognizer.read('trainer/trainer.yml')#recognizer.load('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x, y, w, h) in faces:
        nbr_predicted = ''
        cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
        userId_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])

        print(userId_predicted)
        if conf < 50:
            if userId_predicted == 1:
                userId_predicted = 'User 1'
            elif userId_predicted == 5750:
                userId_predicted = 'Felipe Pacora'
        else:
            userId_predicted = "Unknown"
        cv2.putText(im, str(userId_predicted)+"--"+str(conf), (x, y+h), font, 1, (64, 220, 126)) #Draw the text
        cv2.imshow('im', im)
        #cv2.waitKey(10)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()
