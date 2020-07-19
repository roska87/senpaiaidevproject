from get_images import search_and_download
from dataset_generator import generate

DRIVER_PATH = './chromedriver'
IMAGE_QTY = 100

# Download images
search_and_download(search_term='dog', number_images=IMAGE_QTY, driver_path=DRIVER_PATH)
search_and_download(search_term='car', number_images=IMAGE_QTY, driver_path=DRIVER_PATH)

# Generate dataset files
generate()
