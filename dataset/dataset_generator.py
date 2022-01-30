import os
import numpy as np
from PIL import Image

# Directory containing images you wish to convert
input_dir = "../dataset/images/"
directories = os.listdir(input_dir)


# Convert an image to a numpy image array
def make_square(im, min_size=32, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = min(x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    new_image = new_im.resize((min_size, min_size))
    new_image_arr = np.array(new_image)
    new_image_arr = np.expand_dims(new_image_arr, axis=0)
    return new_image_arr


# Create numpy array files from image folders
def generate():
    folder_index = 0
    image_index = 0
    index_array = []
    for folder in directories:
        # Ignoring .DS_Store dir
        if folder == '.DS_Store':
            pass
        else:
            print(folder)
            images = os.listdir(input_dir + '/' + folder)
            folder_index += 1
            for image in images:
                if image == ".DS_Store":
                    pass
                else:
                    image_index += 1
                    # Opening image
                    im = Image.open(input_dir + "/" + folder + "/" + image)
                    try:
                        if image_index != 1:
                            # Creating array with shape (32, 32, 3)
                            new_array = make_square(im)
                            # Adding new image to array shape of (x, 32, 32, 3) where x is image number
                            out = np.append(out, new_array, 0)
                        elif image_index == 1:
                            # Creating array with shape (32, 32, 3)
                            out = make_square(im)
                        if folder_index == 1 and image_index == 1:
                            index_array = np.array([[folder_index-1]])
                        else:
                            new_index_array = np.array([[folder_index-1]], np.int8)
                            index_array = np.append(index_array, new_index_array, 0)
                    except Exception as e:
                        print(e)
                        print("Error with image", image)

    print(out.shape)
    print(index_array.shape)
    print(folder_index)

    np.save('../dataset/X_train.npy', out)  # Saving train image arrays
    np.save('../dataset/Y_train.npy', index_array)  # Saving train labels


generate()