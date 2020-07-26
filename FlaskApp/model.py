import numpy as np
import load_models

gan_model = load_models.init_gan()
cgan_model = load_models.init_cgan()
cgan_custom_model = load_models.init_cgan_custom()

cgan_label_values = {
  0: "airplane",
  1: "automobile",
  2: "bird",
  3: "cat",
  4: "deer",
  5: "dog",
  6: "frog",
  7: "horse",
  8: "ship",
  9: "truck"
}


cgan_custom_label_values = {
  0: "car",
  1: "dog",
  2: "face"
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
    return gen_img[label]


def cgan_custom_predict(label=0):
    label = int(label)
    noise_size = 2048
    cgan_noise = np.random.randn(3, noise_size)
    sample_label = np.arange(0, 3).reshape(-1, 1)
    gen_img = cgan_custom_model.predict([cgan_noise, sample_label])
    return gen_img[label]


def cgan_values():
    return list(cgan_label_values.values())


def cgan_value_index(label):
    return list(cgan_label_values.values()).index(label)


def cgan_custom_values():
    return list(cgan_custom_label_values.values())


def cgan_custom_value_index(label):
    return list(cgan_custom_label_values.values()).index(label)
