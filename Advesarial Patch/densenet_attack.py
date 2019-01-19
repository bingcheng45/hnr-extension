import numpy as np 
import cv2
from keras.applications.densenet import DenseNet201, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model
from patch import patch_attack
import csv


base_model = DenseNet201(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)


def attack(raw_image_path):
    """Attack"""
    image_path = 'images/' + raw_image_path
    patch_path = 'images/patch.png'

    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # original image for patching
    original_img = cv2.imread(image_path)
    patch = cv2.imread(patch_path, -1)

    # cv2.imshow('image', patch)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # patch attack original image
    x_pos = patch_attack(original_img, patch)
    x_pos = cv2.resize(x_pos, (224,224))
    x_pos = x_pos[::-1].astype(np.float32)
    x_pos = np.expand_dims(x_pos, axis=0)
    x_pos = preprocess_input(x_pos)

    pred = base_model.predict(x)
    pred_pos = base_model.predict(x_pos)

    original = decode_predictions(pred, top=3)[0][0]
    adversarial = decode_predictions(pred_pos, top=3)[0][0]

    o_pred = original[2]
    o_label = original[1]
    a_pred = adversarial[2]
    a_label = adversarial[1]

    with open('results.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([raw_image_path, o_pred, o_label, a_pred, a_label])

    print("Original:", o_pred, o_label)
    print("Adversarial:", a_pred, a_label)

    return
