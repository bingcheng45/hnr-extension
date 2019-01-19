import os 
import shutil
base_path = "/Users/mingliangang/Downloads/tiny-imagenet-200/train/"
train = os.listdir(base_path)
for labels in train[1:]:
	os.makedirs("/Users/mingliangang/Desktop/images/"+labels)
	shutil.copy(base_path+labels+"/images/"+os.listdir(base_path+labels+"/images")[0],"/Users/mingliangang/Desktop/images/"+labels+"/"+os.listdir(base_path+labels+"/images")[0])