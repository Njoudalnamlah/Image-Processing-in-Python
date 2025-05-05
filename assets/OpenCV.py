import cv2
import matplotlib.pyplot as plt

# قراءة الصورة
img = cv2.imread(r'C:\Users\njoud\Downloads\Preview.jpg')  # تأكدي من المسار الصحيح للصورة

# تحويل من BGR إلى RGB حتى تطلع الألوان صحيحة
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# عرض الصورة باستخدام matplotlib
plt.imshow(img_rgb)
plt.show()

