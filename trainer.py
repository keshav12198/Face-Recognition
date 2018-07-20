import cv2,os
import numpy as np
from PIL import Image

# cv2.face.LBPHFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
	faceSamples = []
	Ids=[]

	for imagePath in imagePaths:
		pilImage=Image.open(imagePath).convert('L')
		imageNp=np.array(pilImage,'uint8')
		print "Complete path is ",imagePath
		print "Path is ",os.path.split(imagePath)
		test=(os.path.split(imagePath)[-1])
		print "Test is ",test
		Id=int(test.split(".")[1])
		print "Id is ",Id
		faces = detector.detectMultiScale(imageNp,1.3,5)
		for (x,y,w,h) in faces:
			faceSamples.append(imageNp[y:y+h,x:x+w])
			Ids.append(Id)
	return faceSamples,Ids

faces,Ids = getImagesAndLabels('dataSet')
recognizer.train(faces,np.array(Ids))
recognizer.save('trainer/trainer.yml')
