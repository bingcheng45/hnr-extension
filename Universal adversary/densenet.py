import numpy as np 
import matplotlib.pyplot as plt
from keras.applications.densenet import DenseNet201, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model
from universal_perturb import rand_other,fast_signed_gradient

def original_img_peturb(x_org,x_pos):
	"""
	When reconstructing original sized images with advserial noise included this 
	fuction must be used. 
	"""
	x_pos = x_org+np.resize(x_pos,(x_org.shape[0],x_org.shape[1],3))
	return x_pos 

base_model = DenseNet201(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

img_path = "images/gibbon.jpg"

img_orginal = image.load_img(img_path)
img = image.load_img(img_path, target_size=(224, 224))
x_org = image.img_to_array(img_orginal)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

pred = base_model.predict(x)

x_pos = fast_signed_gradient(x, rand_other(pred))
x_pos = x_pos + x

# x_pos = original_img_peturb(x_org,x_pos)
# plt.imshow(x_org[:,:,::-1])
# plt.show()
# plt.imshow(x_pos[:,:,::-1])
# plt.show()
x_pos = preprocess_input(x_pos)

pred_pos = base_model.predict(x_pos)

print("Un-poisoned image: {}".format(decode_predictions(pred, top=3)[0]))
print("Advserial image: {}".format(decode_predictions(pred_pos,top=3)[0]))

