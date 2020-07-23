import numpy as np
import load_models
from keras.preprocessing import image

gan_model = load_models.init_gan()
cgan_model = load_models.init_cgan()

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


def gan_predict():
    inidim = 100
    gan_noise = np.random.randn(1, inidim)
    gen_img = gan_model.predict(gan_noise)
    return gen_img


def cgan_predict(label=0):
    label = int(label)
    noise_size = 2048
    cgan_noise = np.random.randn(10, noise_size)
    sample_label = np.arange(0, 10).reshape(-1, 1)
    gen_img = cgan_model.predict([cgan_noise, sample_label])
    img = image.array_to_img(gen_img[label])
    return img


def cgan_label(value):
    return label_values[value]
