import cv2, sys, numpy, os 
import time

haar_file = 'haarcascade_frontalface_default.xml'

path = 'datasets'
    

sub_data = 'bilal'	

#path = os.path.join(datasets, sub_data) 
if not os.path.isdir(path): 
	os.mkdir(path) 


(width, height) = (130, 100)	 
 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_file) 
webcam = cv2.VideoCapture(0)

count = 0

while count <= 5: 
	(_, im) = webcam.read() 
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
	for (x, y, w, h) in faces: 
		cv2.rectangle(im, (x, y), (x + w, y + h), (155, 155, 155), 2) 
		face = gray[y:y + h, x:x + w] 
		face_resize = cv2.resize(face, (width, height)) 
		cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
	count += 1
	
	cv2.imshow('OpenCV', im) 
	key = cv2.waitKey(2000)
	if key == 27:
		break
	if count >= 5:
		webcam.release
		cv2.destroyAllWindows()
		



        

    
    
	   
