import cv2,os
import numpy as np
from PIL import Image

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


Id = input("Enter your Id")
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
r.close()

while True:
	Name = raw_input("Enter your name")
	if flag == False:
		break
	if flag == True and Name == s:
		break

if flag == False:
	w = open("Mapping.txt",'a')
	w.write(str(Id)+"  "+Name+"\n")
	w.close()

low = 0
if flag == True:
	imgs = os.listdir('dataSet')
	low = -1
	for img in imgs:
		print img
		n = int(img.split(".")[1])
		print n

		if n == Id:
			print "Hello"
			x = int(img.split(".")[2])
			print x
			if x>low:
				low = x
				print low

sampleNum = low
print sampleNum
count = 0

while(True):
	ret,img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		sampleNum = sampleNum + 1
		count = count + 1
		print sampleNum
		cv2.imwrite("dataSet/"+Name+"."+str(Id)+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
		cv2.imshow('frame',img)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
	elif count > 49:
		break

cam.release()
cv2.destroyAllWindows()