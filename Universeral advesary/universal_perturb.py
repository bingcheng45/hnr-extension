import pickle as pkl
import numpy as np 
import cv2
from keras.applications.vgg16 import VGG16,preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras import backend as K 

def fast_signed_gradient(base_model,x,y):
	
	pass

base_model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)
train_datagen = ImageDataGenerator(shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
        '/Users/mingliangang/Downloads/tiny-imagenet-200/train',
        target_size=(224, 224),
        batch_size=1)

err = 0
gamma = 3000
v = np.zeros((1,224,224,3))
while err<=1-gamma:
	for i,z in enumerate(train_generator):
		x_i,y_i = z
		x_i = preprocess_input(x_i)
		pred = np.argmax(base_model.predict(x_i))
		pred_v = np.argmax(base_model.predict(x_i + v))
		if pred == pred_v:
			continue
			
			r = fast_signed_gradient(base_model,x,y)
			pred_v = np.argmax(base_model.predict(x_i + v+ r))
			
			if pred == pred_v: 
				err +=1
				continue # Escape if the fast signed method fails

			while pred != pred_v:
				r= r*0.9
				pred_v = np.argmax(base_model.predict(x_i + v+ r))
			r/=0.9
			v_prime=v+r 
			#Dubious, really dubious implementation of the projection
			v = np.dot(v,v_prime)/(np.linalg.norm(v))


	break

with open("univseral_pertub.py") as f:
	pkl.dump(v,f)