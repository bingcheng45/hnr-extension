import numpy as np 
import matplotlib.pyplot as plt
from keras.applications.densenet import DenseNet201, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model
from universal_perturb import rand_other,fast_signed_gradient
import cv2

base_model = DenseNet201(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

img_path = "images/gibbon.jpg"

def uni_perturb(img_path):
    img_orginal = image.load_img(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    x_org = image.img_to_array(img_orginal)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    pred = base_model.predict(x)

    x_pos = fast_signed_gradient(x, rand_other(pred))
    x_pos = x_org+np.resize(x_pos,(x_org.shape[0],x_org.shape[1],3))


    filename = 'transformed_img.jpg'
    cv2.imwrite(filename, x_pos)

    # cv2.imshow('image', processed_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return filename


    plt.imshow(x_org)
    plt.show()
    plt.imshow(x_pos)
    plt.show()
    # x_pos = np.expand_dims(x_pos, axis=0)
    # x_pos = preprocess_input(x_pos)

    # pred_pos = base_model.predict(x_pos)

    # print("Un-poisoned image: {}".format(decode_predictions(pred, top=3)[0]))
    # print("Advserial image: {}".format(decode_predictions(pred_pos,top=3)[0]))
