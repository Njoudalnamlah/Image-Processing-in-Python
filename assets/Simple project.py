import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\njoud\Downloads\pexels-photo-1108099.jpeg')  
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

