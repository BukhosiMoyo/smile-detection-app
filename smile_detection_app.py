import cv2

#face and smile classifires

face_detector = cv2.CascadeClassifier('frontface.xml')
smile_detector = cv2.CascadeClassifier('frontface.xml')

# Here we will be grabbing the webcam feed..
webcam = cv.VideoCapture(0)


#This will be running on while true sowe can have the camera looping over and over again

while True:

    # Here we will read the current frame from the webcam

    successful_frame_read, frame = webcam.read()


    #Then if there is an error here we will ahve to abort 

    if not successful_frame_read:
        break


    # here we will have ti change to grey scale 

    frame_grayscale = cv2.cvtColour(frame, cv2.COLOR_BGR2GRAY)

    #The app will have to detect faces first.

    faces = face_detector.detectMultiScale(frame_grayscale, 1.3, 5)

    # Running a smile detectiona within each of those faces 

    for (x, y, w, h) in faces:
        
        #Now come the part where we want to draw a square arounf the face.
        cv2.rectagle(frame, (x, y), (x+w, y+h), (106, 234, 70), 4)

        #Now we want to ceate the face sub Image This is is built on numpy so it will go like this

        face = frame[y:y+h, x:x+w]

        # Now we will grayscale the face

        face_grayscale = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # We are now ready to detect smiles on the face 

        smile = smile_detector.detectMultiScale(face_greyscale, 1.7, 20) 


        #Check if the face is smiling and label it with smlling


        #Enough code for the day have to call ot a night and get some rest. :)