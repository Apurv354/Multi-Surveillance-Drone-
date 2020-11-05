import numpy as np
import cv2
def main():
    
    cap = cv2.VideoCapture(2)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while(1):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        fgmask = fgbg.apply(gray)
     
        cv2.imshow('fgmask',gray)
        cv2.imshow('frame',fgmask)

        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        
        

    cap.release()
    cv2.destroyAllWindows()
