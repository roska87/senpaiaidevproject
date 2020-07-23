from keras.models import model_from_json
from keras.models import load_model


def init_gan_old():
    json_file = open('models/gan_generator_3000.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("models/gan_generator_3000.h5")
    print("Loaded GAN Model from disk")

    # compile and evaluate loaded model
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return loaded_model


def init_gan():
    gan = load_model('models/gan_generator_model_release.h5')
    gan._make_predict_function()
    print("Loaded GAN Model from disk")
    return gan


def init_cgan():
    cgan = load_model('models/cgan_generator_model_release.h5')
    cgan._make_predict_function()
    print("Loaded cGAN Model from disk")
    return cgan
