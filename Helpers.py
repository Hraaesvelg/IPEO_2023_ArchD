import numpy as np
import skimage as sk
import matplotlib.pyplot as plt
from skimage import io

def normalize_image(image):
    # Rescaling the image pixel values to the range [0, 1]
    normalized_image = sk.exposure.rescale_intensity(image, in_range='image', out_range=(0, 1))
    return normalized_image
def show_img(path, print = True):
    # Load the multi-band TIFF image
    image_path = path
    multi_band_image = io.imread(image_path)

    # Display individual bands
    num_bands = multi_band_image.shape[2]  # Get the number of bands in the image

    if print:
        plt.figure(figsize=(12, 6))

        for i in range(num_bands):
            plt.subplot(1, num_bands, i + 1)
            plt.imshow(multi_band_image[:, :, i], cmap='gray')
            plt.title(f'Band {i + 1}')

        plt.tight_layout()
        plt.show()

    # Normalize the image
    normalized_image = normalize_image(multi_band_image)

    # Display the normalized image
    if print:
        plt.figure()
        plt.imshow(normalized_image)
        plt.axis('off')
        plt.title('Normalized Image')
        plt.show()
    return normalized_image, num_bands






path = "data/lidar/tile_0_lidar.tif"
_, band = show_img(path,True)
print(band)