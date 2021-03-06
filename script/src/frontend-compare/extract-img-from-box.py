import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


import skimage
from skimage import data
from skimage import io
from skimage.filter import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb


filename = os.path.join('.', 'page-1.png')
image = io.imread(filename)

# 571 81 625 107

skimage.io.imsave('output.png', image)
io.imshow(image)

sys.exit(1)

# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = bw.copy()
clear_border(cleared)

# label image regions
label_image = label(cleared)
borders = np.logical_xor(bw, cleared)
label_image[borders] = -1
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image, ['Area', 'BoundingBox']):

    # skip small images
    if region['Area'] < 100:
        continue

    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region['BoundingBox']
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

plt.show()
