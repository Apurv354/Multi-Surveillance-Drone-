import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
def main():
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    #log.basicConfig(filename='webcam.log',level=log.INFO)

    video_capture = cv2.VideoCapture(2)
    anterior = 0
    i=0


    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if anterior != len(faces):
            anterior = len(faces)
            #log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
        label2= "{}: {:.2f}%".format('No. of Person', anterior)
        cv2.putText(frame, label2, (10, 40),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 2)
        # show the output frame


        # Display the resulting frame
        #cv2.putText(frame, "Number of faces detected: " + str(anterior), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        cv2.imshow('Video', frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # When everything is done, release the capture

    print(anterior)
    video_capture.release()
    cv2.destroyAllWindows()

