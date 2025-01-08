import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Read the picture from file
myphoto = imageio.imread("myphoto.jpg")

# Scale the values to be between 0.0 and 1.0
photo1 = myphoto.copy() / 255.0

# Get the intensity of red, green, blue
red =photo1[:, :, 0]
green =photo1[:, :, 1]
blue = photo1[:, :, 2]
n = red.shape[0]
m = red.shape[1]

# Generate x and y coordinates
x = np.arange(0.0, n, 1.0)
y = np.arange(0.0, m, 1.0)

# Create interpolating functions
better_red = RegularGridInterpolator((x, y), red, method='cubic', bounds_error=False, fill_value=None)
better_green = RegularGridInterpolator((x, y), green, method='cubic', bounds_error=False, fill_value=None)
better_blue = RegularGridInterpolator((x, y), blue, method='cubic', bounds_error=False, fill_value=None)

# Generate dense xx and yy coordinates
xx = np.arange(0.0, n, 0.1)
yy = np.arange(0.0, m, 0.1)
yy, xx = np.meshgrid(yy, xx)   # Ensure the orientation matches

# Interpolate the data
photo2 = np.zeros((xx.shape[0], xx.shape[1], 3))
photo2[:, :, 0] = better_red((xx, yy))
photo2[:, :, 1] = better_green((xx, yy))
photo2[:, :, 2] = better_blue((xx, yy))

# Clip the interpolated values to be between 0.0 and 1.0
photo2 = np.clip(photo2, 0.0, 1.0)

# Save the interpolated image
imageio.imwrite('Interpolated_myPhoto.png', (photo2 * 255).astype(np.uint8))

# Display original and interpolated images
f, axs = plt.subplots(1, 2, figsize=(15, 15))
axs[0].imshow(photo1)
axs[1].imshow(photo2)

# Choose a square of your choise such as [50, 80]x[50, 80]
zoom1 = photo1[90:140, 50:130, :]
zoom2 = photo2[900:1400, 500:1300, :]   # Adjusted to correct range for zooming in

# Compare the different data
f, axs = plt.subplots(1, 2, figsize=(15, 15))
axs[0].imshow(zoom1)
axs[1].imshow(zoom2)
plt.show()
