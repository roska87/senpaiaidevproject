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
    new_image = new_im.resize((32, 32))
    new_image_arr = np.array(new_image)
    new_image_arr = np.expand_dims(new_image_arr, axis=0)
    return new_image_arr


# Create numpy array files from image folders
def generate():
    index = 0
    index2 = 0
    index_array = []

    for folder in directories:
        # Ignoring .DS_Store dir
        if folder == '.DS_Store':
            pass
        else:
            print(folder)
            folder2 = os.listdir(input_dir + '/' + folder)
            index += 1
            for image in folder2:
                if image == ".DS_Store":
                    pass
                else:
                    index2 += 1
                    im = Image.open(input_dir + "/" + folder + "/" + image)  # Opening image
                    # im = (np.array(im))  # Converting to numpy array
                    try:
                        # r = im[:, :, 0]  # Slicing to get R data
                        # g = im[:, :, 1]  # Slicing to get G data
                        # b = im[:, :, 2]  # Slicing to get B data
                        if index2 != 1:
                            # Creating array with shape (3, 100, 100)
                            # new_array = np.array([[r] + [g] + [b]], np.uint8)
                            new_array = make_square(im)
                            # Adding new image to array shape of (x, 3, 100, 100) where x is image number
                            out = np.append(out, new_array, 0)
                        elif index2 == 1:
                            # Creating array with shape (3, 100, 100)
                            # out = np.array([[r] + [g] + [b]], np.uint8)
                            out = make_square(im)
                        if index == 1 and index2 == 1:
                            index_array = np.array([[index]])
                        else:
                            new_index_array = np.array([[index]], np.int8)
                            index_array = np.append(index_array, new_index_array, 0)
                    except Exception as e:
                        print(e)
                        print("Removing image", image)
                    # os.remove(input_dir+"/"+folder+"/"+image)

    print(out.shape)
    print(index_array.shape)
    print(index)

    np.save('../dataset/X_train.npy', out)  # Saving train image arrays
    np.save('../dataset/Y_train.npy', index_array)  # Saving train labels


generate()
