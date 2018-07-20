import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam=cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)

while True:
	ret,im=cam.read()
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(255,0,0),2)
		Id,conf=recognizer.predict(gray[y:y+h,x:x+w])
		if(conf<50):
			s = ''
			flag = False
			r = open("Mapping.txt",'r')
			for a in r.read():
				if flag == True and a == '\n':
					break
				if flag == True and a!=' ':
					s = s + a
				if a == str(Id):
					flag = True
			Id = s
			print Id
		else:
			Id="Unknown"
			print Id
		cv2.putText(im, str(Id), (x,y+h), fontface, fontscale, fontcolor) 
	
	cv2.imshow('im',im)
	if cv2.waitKey(10) & 0xFF==ord('q'):
		break
cam.release()
cv2.destroyAllWindows()