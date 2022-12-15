# ライブラリインポート
import cv2
# グレースケール化
# 画像読み込み
img = cv2.imread('images/upload/Sample-image.jpeg')
# 読み込んだ画像グレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 画像保存
cv2.imwrite('images/result/grayscale-fillter/Sample-image.jpeg', img_gray)

# # 二値化
# img2 = cv2.imread('before_picture/Sample-image.jpeg',0)
# threshold = 100
# # 二値化(閾値100超えた画素を255)
# ret, img_thresh = cv2.threshold(img2, threshold, 255, cv2.THRESH_BINARY)
# cv2.imwrite('after_picture/nitiSample-image.jpeg', img_thresh)
