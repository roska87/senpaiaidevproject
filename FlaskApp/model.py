import numpy as np
import load_models

gan_model = load_models.init_gan()
cgan_model = load_models.init_gan()


def gan_predict():
    inidim = 100
    noise = np.random.randn(1, inidim)
    gen_img = gan_model.predict(noise)
    return gen_img


def cgan_predict(label):
    inidim = 100
    noise = np.random.randn(1, inidim)
    gen_img = cgan_model.predict(noise)
    return gen_img
