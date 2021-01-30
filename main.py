from grabscreen import grab_screen
import cv2
import numpy as np
import time
import keys as k

keys = k.Keys()

def pathing(minimap):
	lower = np.array([50,10,10])
	upper = np.array([250,150,150])

	hsv = cv2.cvtColor(minimap, cv2.COLOR_RGB2HSV)
	mask = cv2.inRange(hsv,lower,upper)

	matches = np.argwhere(mask==0)
	mean_y = np.mean(matches[:,1])
	target = minimap.shape[1]/2

	error = target - mean_y

	try:
		keys.directMouse(-3*int(error),0)
	except:
		print(error)
	print(error)

	cv2.imshow("cv2Screen",mask)
	cv2.waitKey(10)



for i in range(5):
	print(i)
	time.sleep(1)

print("start")
keys.directKey('w')
keys.directKey('shift')
for i in range(5000):
	screen = grab_screen(region=(190,820,240,870))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

	pathing(screen)


	# cv2.imshow("cv2Screen",screen)
	# cv2.waitKey(10)
keys.directKey('w', keys.key_release)
keys.directKey('shift', keys.key_release)
cv2.destroyAllWindows()