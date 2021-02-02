from PIL import Image
import numpy as np

h = 150 # Height
w = 150 # Width

rand = True

if rand:
    # Random
    data=np.random.randint(low=0,high=256,size=h*w*3, dtype=np.uint8)
else:
    # Pattern
    data = []

    #for i in range(0,h):
    #    for j in range(0,w):
    #        data.append([i % 256,j % 256, i*j % 256])

    #for i in range(0,h):
    #    for j in range(0,w):
    #        data.append([i % 256,j % 256, i + j % 256])

    #for i in range(0,h):
    #    for j in range(0,w):
    #        data.append([i % 256,j % 256, i - j % 256])

    #for i in range(0,h):
    #    for j in range(0,w):
    #        data.append([i**2 % 256,j**2 % 256, i*j % 256])

    #for i in range(0,h):
    #    for j in range(0,w):
    #        data.append([i**2 % 256,j**2 % 256, i*j % 256])

    for i in range(0,h):
        for j in range(0,w):
            data.append([i**2 % 256,j**2 % 256, i*j % 256])
    data = np.array(data,dtype=np.uint8)

data=data.reshape(h,w,3)
Image.fromarray(data,'RGB').save("output.png")
