from keras.preprocessing import image
import io


def gen_img_to_file(gen_img):
    img = image.array_to_img(gen_img[0])
    file = io.BytesIO()
    img.save(file, 'png')
    file.seek(0)
    return file
