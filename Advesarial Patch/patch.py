import numpy as np 
import cv2

def patch_attack(original_img,patch,resize=False):
	"""
	Patch performs an advserial patch black box attack on a neural network
	"""
	print("SIZES", original_img.shape) # (2308,3468,3) GIBBON
	# (1026,778,3) TOTORO

	h, w = original_img.shape[:2]
	size = min(h,w)
	size //= 5

	patch = cv2.resize(patch, dsize=(size, size), interpolation=cv2.INTER_CUBIC)
	print("SIZES", patch.shape) # (662,838,4)

	x_offset = 50
	y_offset = 50

	y1, y2 = y_offset, y_offset + patch.shape[0]
	print("y1, y2", y1, y2) #(50,712)

	x1, x2 = x_offset, x_offset + patch.shape[1]
	print("x1, x2", x1, x2) #(50,888)

	assert patch.shape[2] == 4, "Make sure you use cv2.imread('patch.png',-1)"
	alpha_s = patch[:, :, 3] / 255.0
	alpha_l = 1.0 - alpha_s
	print(original_img.shape)  #(1026,778,3)
	print("A", patch[:,:,:].shape)  #(662, 838, 4)
	print("B", original_img[y1:y2, x1:x2, :].shape)  #(662, 728, 3)

	for c in range(0, 3):
		original_img[y1:y2, x1:x2, c] = (alpha_s * patch[:, :, c] +
						alpha_l * original_img[y1:y2, x1:x2, c])

	# if resize != False : original_img = cv2.resize(original_img, resize)
	# x_pos = original_img[::-1].astype(np.float32)

	return original_img


if __name__ == '__main__':
	original_img = cv2.imread("gibbon.jpg")
	patch = cv2.imread("patch.png",-1)
	x_pos = patch_attack(original_img,patch)
