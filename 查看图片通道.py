from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img = Image.open(r"1.jpg")
img = img.resize((1300,650))
# img.save("2.jpg")
print(img.size)
# img.show()
# plt.imshow(img)
photo2 = np.array([[[1,0,0],
                    [0,1,0],
                    [0,0,1]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]
                   ])
photo1 = np.array([[1,0,0.2],
                    [0,1,0.2],
                    [0,0,0]],dtype=np.uint8)
# photo1 = np.ones((3,3),dtype=np.uint8)
img_data = np.array(img)
print(img_data.shape)
img_data1 = (img_data.dot(photo1))
print(img_data1.shape)
img1 = Image.fromarray(img_data1)
plt.imshow(img_data1)
plt.show()
# r,g,b = img.split()
# # plt.imshow(b)
#
#查看通道图片
# img0 = Image.merge("RGB",(r,g,b.point(lambda i:i==i*0)))
# plt.imshow(img0)
# img0.show()
# plt.show()