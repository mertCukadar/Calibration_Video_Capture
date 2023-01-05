import numpy as np
import cv2 

class Calibration:
   
  
    def Calibrator():
        """
        Author: Mert Kaan Çukadar

        This application will cover the topic of detect and take a photo from center
        of calibration image.

        param1: 'q' --> this comman close the application. 
        param2: 's' --> if you ready to captrure the image this comman save it to your current file

        before you start: 
        please get your calibration image's center to intersection point's of two lines
        then press 's' button to save it. After that you can close the program with 'q' button. 
        """


        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Camera is not opened...")
            exit()

        while True:
            rat , frame = cap.read()

        # if frame is not True
            if not rat:
                print(f"rat value is: {rat}\n video capture can not recieve image")
                break

        # Operations on frame will come gere for now we will convert our image gray scale

            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            w,h = np.shape(gray)
        
            halfy = h/2
            halfx = w/2

        #print(f"w :{w} h: {h}")
        
            gray[int(halfx) , :] = 255
            gray[: , int(halfy)] = 255

            if cv2.waitKey(1) == ord("s"):
                cv2.imwrite("calibrated_img.png",frame)
        #displat the result frame

            cv2.imshow("frame" , gray)
            if cv2.waitKey(1) == ord("q"):
                break

        
        cap.release()
        cv2.destroyAllWindows()

help(Calibration)

Calibration.Calibrator()
