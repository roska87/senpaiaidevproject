# Imports necesarios
from __future__ import print_function
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.applications import imagenet_utils
import numpy as np
import flask
import io
import ssl
from flask import send_file

# Inicializar aplicación Flask
app = flask.Flask(__name__)
# Definir variable global para los modelos
gan_model = None
cgan_model = None

ssl._create_default_https_context = ssl._create_unverified_context


def load_trained_gan_model():
    print("Cargando modelo GAN de Keras...")
    global gan_model
    gan_model = load_model('models/gan_generator_model_release.h5')
    gan_model._make_predict_function()
    print("Modelo GAN cargado")


def load_trained_cgan_model():
    print("Cargando modelo cGAN de Keras...")
    global cgan_model
    cgan_model = load_model('models/cgan_generator_model_release.h5')
    cgan_model._make_predict_function()
    print("Modelo cGAN cargado")


def prepare_image(image, target):
    # Ajustar el tamaño y pre-procesar la imagen
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    # Retornar la imagen pre-procesada
    return image


def gen_img_to_file(gen_img):
    img = array_to_img(gen_img)
    file = io.BytesIO()
    img.save(file, 'png')
    file.seek(0)
    return file


@app.route("/gan/predict", methods=["GET"])
def predict_gan():
    inidim = 100
    noise = np.random.randn(1, inidim)
    gen_img = gan_model.predict(noise)
    file = gen_img_to_file(gen_img[0])
    return send_file(file, attachment_filename='gan_img.png')


@app.route("/cgan/predict/<label>", methods=["GET"])
def predict_cgan(label):
    label = int(label)
    noise_size = 2048
    cgan_noise = np.random.randn(10, noise_size)
    sample_label = np.arange(0, 10).reshape(-1, 1)
    gen_img = cgan_model.predict([cgan_noise, sample_label])
    img = gen_img[label]
    file = gen_img_to_file(img)
    return send_file(file, attachment_filename='cgan_img.png')


# Comenzar la ejecución del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_gan_model()
    load_trained_cgan_model()
    app.run()
