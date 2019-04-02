# Importing required libraries
import numpy as np
import mss.tools
import time
import cv2
import mss

# Printing warning
print("For this to work properly your screen must be set to 1920x1090!")
print("To stop script use CTRL+C.")
time.sleep(2)

# Taking screenshots every one and a half seconds
count = 0
while count < 5:
	with mss.mss() as sct:
		time.sleep(1.5) # Change screenshot time here
		# Setting size and position of image
		monitor = {"top": 130, "left": 80, "width": 561, "height": 420}
		output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
		# Taking screnshot and saving
		sct_img = sct.grab(monitor)
		mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
		print("Screenshot taken")
		image = cv2.imread(output)
		boundaries = [
				([17, 15, 100], [50, 56, 200])
		]

		# Finding color within boundaries and putting mask over original image
		for (lower, upper) in boundaries:
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)
			gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	
		# Checking if image has motion
		if cv2.countNonZero(gray) == 0:
			print("No motion, turning off light")
			# Put no motion code here
		else:
			print("Motion found, turning on light")
			# Put motion code here


