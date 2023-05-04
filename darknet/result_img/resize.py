from PIL import Image
from pytesseract import image_to_string
import glob, os
import time
import re
from tesserocr import PyTessBaseAPI, RIL
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
from pyfcm import FCMNotification
import time
import operator
import cv2
import os
import cv
import pytesseract
import numpy as np
import time
import math
from firebase import firebase

from pytesseract import image_to_string

def func(firstLine,direction) :

	notify = ''
	uid=''
	society_v=''
	society_u=''
	#inventory = db.reference("Credential").child("Plumeria")
	from firebase import firebase
	flag=1
	number=firstLine
	firebase=firebase.FirebaseApplication('https://hawkeye-14d1e.firebaseio.com',None)
	result = firebase.get('/Credential/Plumeria',None)
	send = list()
	send.append(result[u'Guard'][u'user_key'])
	if number in result:
		send.append(result[number][u'user_key'])
		uid=result[number][u'id']
		descrp='User Vehicle'
	else:
		flag=0
		uid='Non-resident'
		descrp='Non-resident'

	push_service = FCMNotification(api_key="AAAAO1FzPkg:APA91bFeokvp3z8qZdNIJ7MIi8slkjN10S8f_zjarzrOuJdlbv3-oRCereK_GpKWld3xraoe6GXE7KuCHLqKluSDaCgP6gG2h_KwnTUGxmzC0paTzvtNzFsyoXbfV9lT0kQr61RiooeU")



	print result
	registration_ids = send
	if flag==1:
		message = "The vehicle "+number+" has "+direction 
	else:
		message = "Non resident vehicle "+number+" has "+direction
	print 'SENDING NOTIFICATION..................................'
	result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_body=message)
	print result



		
		

	#print ("Start",send,"End")
	
		#push_service = FCMNotification(api_key="AAAAO1FzPkg:APA91bFeokvp3z8qZdNIJ7MIi8slkjN10S8f_zjarzrOuJdlbv3-oRCereK_GpKWld3xraoe6GXE7KuCHLqKluSDaCgP6gG2h_KwnTUGxmzC0paTzvtNzFsyoXbfV9lT0kQr61RiooeU")
		#c=str(firstLine).strip('\n')
	print "LOGS"
	now = datetime.datetime.now()


	print now.year, now.month, now.day, now.hour, now.minute, now.second

	yr=now.year
	dt=now.date
	mth=now.month
	dy=now.day
	hr=now.hour
	mt=now.minute
	t=now.time;
	sc=now.second


	yr=int(yr)

	mth=int(mth)
	dy=int(dy)
	hr=int(hr)
	mt=int(mt)

	sc=int(sc)

	ts=str();

	ts = time.time()

	print ts

	st=str()

	st=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y|%H:%M')

	print st


	ref = db.reference('entrylog')
	new_ref=ref.push({
		'dsc':descrp,
		'rnum': number,
		'timestamp':{
			'day':dy,
			'month':mth,
			'hours':hr,
			'minutes':mt,
			'year':yr,
			'timezoneOffset':-330,
			'time':567890,
			'seconds':sc,
			'date':dy

	
		},
		'timestamp_dsc': direction,
		'datetime':st,
		'uid': uid,
		'exit_status':False
	})

	print 'The new key generated is:',new_ref.key


	# Send to multiple devices by passing a list of ids.
	#egistration_ids = send
	#message = "The vehicle  "+c+" has " + direction
	#print 'SENDING NOTIFICATION..................................'
	#result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_body=message)




	#registration_id = send
	#message_title = "Vehicle Arrived"
	#message_body = "Your vehicle "+ c + " has arrived"
	#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

	#print result
	return


def validity(x) :
	if x   == 'AP' or  x   == 'AR' or  x   == 'AS' or  x   == 'BR' or  x   == 'CG' or  x   == 'GA' or  x   == 'GJ' or  x   == 'HR' or  x   == 'HP' or  x   == 'JK' or  x   == 'JH' or  x   == 'KA' or	  x   == 'KL' or  x   == 'MP' or  x   == 'MH' or  x   == 'ML' or  x   == 'MZ' or  x   == 'NL' or  x   == 'OD' or  x   == 'PB' or  x   == 'RJ' or  x   == 'SK' or  x   == 'TN' or  x   == 'TS' or  x   == 'TR' or  x   == 'UA' or  x   == 'UK' or  x   == 'UP' or  x   == 'WB' or  x   == 'AN' or  x   == 'CH' or  x   == 'DN' or  x   == 'DD' or  x   == 'DL' or  x   == 'LD' or  x   == 'PY' or  x   == 'OR':
		return True
	else :
		return False
	
	
cred = credentials.Certificate('/home/shalaka/Downloads/hawkeye-14d1e-firebase-adminsdk-6v8px-8f8054a248.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hawkeye-14d1e.firebaseio.com'
})

#f1=open('res/Input', 'a')
flag = True;
open('/home/shalaka/darknet/ques.txt', 'w').close()
f2=open('/home/shalaka/darknet/ques.txt','r')
dict = {}
direction = 0
#time.sleep(20)
prev = 0
b=f2.readline()
while b == '':
	b=f2.readline()
	continue
b=b.strip().split(' ')
height = int(b[1])
width = int(b[0])
count = 0
deno = math.sqrt(height*height+width*width)
prevx = 0
prevy = 0
flg = 0
prevno = ''
prevd=''
while (flag):
	b=f2.readline()
	if b == '':
		continue
	elif b == 'END\n':
		print "Break"
		#print "a"+max(dict.iteritems(), key=operator.itemgetter(1))[0]+"b"
		if direction>0 :
			temp = 'arrived'
		else :
			temp = 'left'
		if dict:	
			line=max(dict.iteritems(), key=operator.itemgetter(1))[0]
			print 'PASS ' +line +' Direction '+temp
			if line!=prevno or temp!=prevd:
				func(line,temp)
				prevno=line
				prevd=temp
		break
	else :
		b=b.strip().split(' ')
		p=int(b[1])-prevx
		q=int(b[2])-prevy
		prevx = int(b[1])
		prevy = int(b[2])
		if (flg==1) and math.sqrt((p*p)+(q*q))/deno>0.03:
			#print ('Direction', direction)
			#print ('Y',b[2])
			print b[0]
			print "CHANGE\n"
			if direction>0 :
				temp = 'arrived'
			else :
				temp = 'left'			
			if dict:	
				line=max(dict.iteritems(), key=operator.itemgetter(1))[0]
				print 'PASS' +line +'Direction '+temp
				if line!=prevno or temp!=prevd:
					func(line,temp)
					prevno=line
					prevd=temp
			dict = {}
			flg=0
			prevx=0
			prevy=0
			direction = 0
			prev = 0
			continue

		else:
			#print b[0]
			print b[1]
			print b[2]
			c=b[0].strip().split('/')
			#print c[0]
			#print c[1]
			imageFile = c[1]
			im1 = '/home/shalaka/darknet/result_img/'+imageFile
			if prev == 0:
				prev=b[2]
			else :
				direction+=int(b[2])-int(prev)
				prev=b[2]
			print direction
			count+=1
			

			img_path = im1
			img = cv2.imread(img_path)

			# Extract the file name without the file extension
			file_name = os.path.basename(img_path).split('.')[0]
			file_name = file_name.split()[0]

			#output_dir = "/home/deval/Pictures"
			# Create a directory for outputs
			output_path = "/home/shalaka/darknet/result_img/res/"
			if not os.path.exists(output_path):
				os.makedirs(output_path)
			fm = cv2.Laplacian(img, cv2.CV_64F).var()
			text = "Not Blurry"
			if fm < 500:
				text = "Blurry"
			print img_path
			# Rescale the image, if needed.
			img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

			# Convert to gray
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			#img = cv2.bitwise_not(img,img)
			if text == "Blurry":
				# Apply dilation and erosion to remove some noise
				kernel = np.ones((1, 1), np.uint8)
				simg = cv2.dilate(img, kernel, iterations=1)
				img = cv2.erode(img, kernel, iterations=1)

	
				img =cv2.adaptiveThreshold(cv2.medianBlur(img,3), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 3)
			# Apply threshold to get image with only black and white
			#img =cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9,75,75), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)
			#img = cv2.threshold(cv2.medianBlur(img,3),0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

			# Save the filtered image in the output directory
			save_path = os.path.join(output_path, file_name + "_filter_" + ".jpg")
			cv2.imwrite(save_path, img)

			# Recognize text with tesseract for python
			n_plate = pytesseract.image_to_string(img, lang="eng")
			
			m_plate=''
			#print ("n_plate"+n_plate+c[1])
			for i in range(len(n_plate)):
				#print "Letters"+n_plate[i]
				if (n_plate[i]>='A' and n_plate[i]<='Z') or (n_plate[i]>='0' and n_plate[i]<='9'):
					m_plate=m_plate+n_plate[i];
					#print ("Gussa"+n_plate[i])
	
			print m_plate
			import unicodedata
			x = re.findall("[A-Z]{1,2}[0-9]{1,2}[A-Z]{1,3}[0-9]{1,4}", m_plate)
			
			if x:
				#print "X "+x[0]
				#print "SubX "+x[0][:2] 
				if validity(x[0][:2]):
					if dict.has_key(x[0]):
						dict[x[0]]+=1
					else:
						dict[x[0]]=1
	
			for index, key in enumerate(dict): 
		    		print key, dict[key] 
		if flg==0:
			flg=1
					 

