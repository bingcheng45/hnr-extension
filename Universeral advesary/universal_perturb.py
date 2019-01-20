import random
import pickle as pkl
import numpy as np 
import cv2
from tqdm import tqdm 
import tensorflow as tf
from keras.applications.vgg16 import VGG16,preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras import backend as K

sess = tf.Session()

def rand_other(pred):
	new_pred = np.argmax(pred)
	while np.argmax(pred) == new_pred:
		new_pred = random.randint(0,199)
	return new_pred

def fast_signed_gradient(model,x,y,e=0.20):
	theta = model.trainable_weights[0]
	outputTensor = model.output
	label= tf.constant([0.0 if i!= y else 1.0 for i in range(1000)],dtype=tf.float32)
	loss = K.categorical_crossentropy(outputTensor,label, from_logits=False)
	grads = K.gradients(loss, model.input)[0]
	sess.run(tf.initialize_all_variables())
	return sess.run(grads,feed_dict={model.input:x})

base_model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)
train_datagen = ImageDataGenerator(shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
        '/Users/mingliangang/Downloads/tiny-imagenet-200/train',
        target_size=(224, 224),
        batch_size=1)

err = 0
delta = 0.1
gamma = 3000
v = np.zeros((1,224,224,3))
while err<=1-delta:
	for i,z in tqdm(enumerate(train_generator)):
		x_i,y_i = z
		x_i = preprocess_input(x_i)
		pred = base_model.predict(x_i)
		pred_v = base_model.predict(x_i + v)
		if np.argmax(pred) == np.argmax(pred_v):

			r = fast_signed_gradient(base_model,x_i,rand_other(pred))
			pred_v = base_model.predict(x_i + v+ r)
			if np.argmax(pred) == np.argmax(pred_v): 
				err +=1
				continue # Escape if the fast signed method fails

			while np.argmax(pred) != np.argmax(pred_v):
				r= r*0.9
				pred_v = base_model.predict(x_i + v+ r)
			r/=0.9
			v_prime=v+r 
			# Dubious, really dubious implementation of the projection
			# We can also use a pesudo inverse to calculate the projection
			# Rmb linear regression
			v = np.dot(v,v_prime)/(np.linalg.norm(v))
			if np.linalg.norm(v) > gamma: v *= gamma/np.linalg.norm(v)

with open("univseral_pertub.pkl","rb") as f:
	pkl.dump(v,f)