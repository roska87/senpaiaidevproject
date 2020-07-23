# Imports necesarios
from __future__ import print_function
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.applications import imagenet_utils
from flask import send_file
from flask_restplus import Api, Resource
from nocache import nocache
import numpy as np
import flask
import io
import ssl
import os


# Inicializar aplicación Flask
app = flask.Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
api = Api(app=app,
          title='AI Project API',
          description='ML/DL models prediction API',
          version='1.0')

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# Definir variable global para los modelos
gan_model = None
cgan_model = None

ssl._create_default_https_context = ssl._create_unverified_context
gan_space = api.namespace('gan', description='GAN horse image prediction')
cgan_space = api.namespace('cgan', description='cGAN image prediction')


label_values = {
  0: "Airplane",
  1: "Automobile",
  2: "Bird",
  3: "Cat",
  4: "Deer",
  5: "Dog",
  6: "Frog",
  7: "Horse",
  8: "Ship",
  9: "Truck",
}


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


@gan_space.route("/predict")
class GanClass(Resource):

    # return an image from the GAN model prediction
    @api.doc(responses={200: 'OK',
                        500: 'Internal Server Error'})
    @nocache
    def get(self):
        inidim = 100
        noise = np.random.randn(1, inidim)
        gen_img = gan_model.predict(noise)
        file = gen_img_to_file(gen_img[0])
        return send_file(file, attachment_filename='gan_img.png')


def abort_if_value_doesnt_exist(value):
    if value not in list(label_values.values()):
        api.abort(400, "Value '{}' doesn't exist".format(value))


@cgan_space.route("/predict/<label>", endpoint='predict')
class CGanClass(Resource):

    @api.doc(responses={200: 'OK',
                        400: 'Invalid Argument',
                        500: 'Internal Server Error'},
             params={'label': 'Specify the prediction label'},
             description='Label allowed values: {0}'.format(', '.join(list(label_values.values()))))
    @nocache
    def get(self, label):
        print("Label received:", label)
        abort_if_value_doesnt_exist(label)
        label_index = list(label_values.values()).index(label)
        noise_size = 2048
        cgan_noise = np.random.randn(10, noise_size)
        sample_label = np.arange(0, 10).reshape(-1, 1)
        gen_img = cgan_model.predict([cgan_noise, sample_label])
        print("Predicted image:", gen_img.shape, "with label:", label)
        print(gen_img.shape)
        img = gen_img[label_index]
        file = gen_img_to_file(img)
        return send_file(file, attachment_filename='cgan_img.png')


# Comenzar la ejecución del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_gan_model()
    load_trained_cgan_model()
    app.run(host='0.0.0.0', port=port)
