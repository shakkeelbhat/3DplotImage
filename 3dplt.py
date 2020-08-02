from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import cv2
import numpy as np
img=cv2.imread('file.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
r,g,b=cv2.split(img1)
fig=plt.figure()
axis=fig.add_subplot(1,1,1,projection="3d")

pixel_colors=img1.reshape((np.shape(img1)[0] * np.shape(img1)[1],3))
norm=colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors=norm(pixel_colors).tolist()

axis.scatter(r.flatten(),g.flatten(),b.flatten(),facecolors=pixel_colors,marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel('Blue')
plt.show()
