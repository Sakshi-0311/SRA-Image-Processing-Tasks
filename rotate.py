import numpy as np
import math
import matplotlib.pyplot as plt


img=plt.imread('rotate.png')
#shape=img.shape
height,width,num_channels=img.shape
rotation_in_degree=int(input("Enter the angle in degree: "))
rotation_in_radian=math.radians(rotation_in_degree)   #Converting the angle from degrees into radians
max_len=int(math.sqrt(height**2+width**2))            #Maximum Length of the output_image
rotated_img=np.zeros((max_len,max_len,num_channels))
#print(rotated_img)
rotated_height,rotated_width,_ = rotated_img.shape
mid_row=int((rotated_height+1)/2)
mid_col=int((rotated_width+1)/2)
#Applying Rotation Matrix [[cos(theta) -sin(theta)
 #                          sin(theta)  cos(theta)]]
for r in range(rotated_height):
    for c in range(rotated_width):
        y=(r-mid_col)*math.cos(rotation_in_radian)+(c-mid_row)*math.sin(rotation_in_radian)
        x=-(r-mid_col)*math.sin(rotation_in_radian)+(c-mid_row)*math.cos(rotation_in_radian)
        y+=mid_col
        x+=mid_row
        y=int(y)
        x=int(x)
        if(x>=0 and y>=0 and x<width and y<height):
            rotated_img[r][c][:] = img[y][x][:]


plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(rotated_img,cmap='gray')
plt.show()
