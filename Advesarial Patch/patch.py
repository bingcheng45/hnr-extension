import numpy as np 
import cv2

def patch_attack(original_img,patch,resize=False):
	"""
	Patch performs an advserial patch black box attack on a neural network
	"""

	x_offset = y_offset = 50

	y1, y2 = y_offset, y_offset + patch.shape[0]
	x1, x2 = x_offset, x_offset + patch.shape[1]
	assert patch.shape[2] == 4, "Make sure you use cv2.imread('patch.png',-1)"  
	alpha_s = patch[:, :, 3] / 255.0
	alpha_l = 1.0 - alpha_s

	for c in range(0, 3):
	    original_img[y1:y2, x1:x2, c] = (alpha_s * patch[:, :, c] +
	                              alpha_l * original_img[y1:y2, x1:x2, c])

	if resize != False : original_img = cv2.resize(original_img, resize) 

	return original_img

if __name__ == '__main__':
	original_img = cv2.imread("gibbon.jpg")
	patch = cv2.imread("patch.png",-1)
	x_pos = patch_attack(original_img,patch)
	