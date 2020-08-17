import cv2
import numpy as np
import io
import random
import base64
from keras import models
from keras.models import load_model

from flask import Flask, request, render_template, make_response, Response


init_Base64 = 21 # data:image/png;base64, 로 시작
app = Flask(__name__)
model = load_model('mnist_cnn_tiny.h5')
model.summary()

@app.route('/')
def home():
    return render_template("mnist.html")

@app.route('/upload', methods=['POST'])
def upload():
    draw = request.form['url']
    # hidden에 url로 함
    draw = draw[init_Base64:]
    draw_decoded= base64.b64decode(draw)
    image = np.asarray(bytearray(draw_decoded), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    image= cv2.resize(image, dsize=(28, 28), interpolation=cv2.INTER_AREA)
    image = image.reshape(1, 28, 28, 1)
    print(image.shape)
    p = model.predict(image)

    return np.argmax(p)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
