import numpy as np
from PIL import Image, ImageTk

def lomo_fi(image):

	# img = Image.open('/media/coding_coffee/New Volume/Projects/test_dump/Tony_Stark.jpg')
	# img.show()
	# img = image
	img = np.asarray(img)
	img = img.tolist()

	colorPtr = 0 #0-red, 1-green, 2-blue

	alpha = 0.8 #<1
	beta  = 2.1
	gamma = 0.6	#<1 #will use this later

	for color in img:
		row = 0
		for location in color:
			col = 0
			for value in location:
				if value<100:
					img[colorPtr][row][col] = alpha*value
				elif value<125:
					img[colorPtr][row][col] = 100*alpha + beta*value
				else:
					img[colorPtr][row][col] = 100*alpha + 125*beta + gamma*value
				col+=1
			row+=1	
		### Track color
		colorPtr+=1

	newImage = np.array(img, dtype=np.uint8)
	newImage = Image.fromarray(newImage, 'RGB')
	# newImage.show()
	return newImage