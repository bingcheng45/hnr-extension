from flask import Flask, render_template, request, flash, redirect, flash, url_for, send_from_directory, make_response
import os
import cv2
from werkzeug.utils import secure_filename
from patch import patch_attack
from keras.preprocessing import image
import numpy as np
from keras.applications.densenet import preprocess_input
from functools import wraps, update_wrapper
from datetime import datetime


def nocache(view):
    # Prevents caching of index.html
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/attack/", methods=['GET', 'POST'])
@nocache
def get_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Convert FileStorage object into cv2 image
            # https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-cv2
            filestr = file.read()
            npimg = np.fromstring(filestr, np.uint8)
            original_img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            print("npimg", original_img.shape, type(original_img))

            # Test image
            # original_img = cv2.imread("gibbon.jpg")
            # print("gibbon", original_img.shape, type(original_img))

            # Apply adversarial patch
            patch = cv2.imread("patch.png", -1)
            processed_img = patch_attack(original_img, patch)
            cv2.imwrite(filename, processed_img)

            # cv2.imshow('image', processed_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True, use_reloader=False, threaded=False)