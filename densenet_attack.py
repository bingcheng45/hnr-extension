from keras.applications.densenet import DenseNet201, preprocess_input,decode_predictions
from keras.preprocessing import image
from keras.models import Model
import numpy as np 

base_model = DenseNet201(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

img_path = "gibbon.jpg"
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

pred = base_model.predict(x)
print(decode_predictions(preds, top=3)[0])