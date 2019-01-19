import numpy as np 
import cv2
from keras.applications.densenet import DenseNet201, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model
from universal_perturb import rand_other,fast_signed_gradient

base_model = DenseNet201(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

img_path = "gibbon.jpg"
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

original_img = cv2.imread("gibbon.jpg")
patch = cv2.imread("patch.png", -1)

# cv2.imshow('image', patch)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


pred = base_model.predict(x)

x_pos = fast_signed_gradient(original_img, rand_other(pred))
cv2.imshow("image_pos",x_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()

# x_pos = np.expand_dims(x_pos, axis=0)
# x_pos = preprocess_input(x_pos)

# pred_pos = base_model.predict(x_pos)

# print("Un-poisoned image: {}".format(decode_predictions(pred, top=3)[0]))
# print("Advserial image: {}".format(decode_predictions(pred_pos,top=3)[0]))
