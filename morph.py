# Siddharth Vadgama
# UTA ID-1001397508
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def intermediate(firstImage, lastImage, N, display):
    """
        if display is True
            display the images
        otherwise
            save as a file with the names mid01.jpg, mid02.jpg, ...
    """

    img1 = plt.imread(firstImage)
    img2 = plt.imread(lastImage)
    delt = (img2.astype(np.float) - img1.astype(np.float)) / N
    imgs = []
    for j in range(1, N):

        temp = img1.astype(float) + (j * delt.astype(float))

        temp = temp.astype(np.uint8)
        im = Image.fromarray(temp)
        imgs.append(im)

    imgs[0].save("out.gif", save_all=True, append_images=imgs[1:])


###############  main  ###############
if __name__ == "__main__":
    import sys

    name1 = sys.argv[1]
    name2 = sys.argv[2]

    N = 10  # should produce N-1 intermediate images

    display = False  # True means display intermediate images
    # False means save intermediate images
    intermediate(name1, name2, N, display)
