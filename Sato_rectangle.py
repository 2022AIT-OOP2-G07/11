#(1)モジュールをインポート
import matplotlib.pyplot as plt
import cv2
 
#(2)カスケードファイルを使って認識器を作成
cascade_file= "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)
 
#(3)画像を読み込みグレイスケールに変換
img = cv2.imread("./image/ari.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("grayscale.jpg", img_gray)
 
#(4)顔認識
face_list = cascade.detectMultiScale(img_gray, minSize=(150,150))
#認識失敗時の処理
if len(face_list) == 0:
    print("失敗")
    quit()
#(5)認識した顔の座標、位置を視覚化
for (x,y,w,h) in face_list:
    print("顔の座標(x,y,w,h):", x, y, w, h)
    red=(0,0,255)
    cv2.rectangle(img, (x,y), (x+w, y+h), red, thickness=20)
 
#(6)顔認識した画像を表示、出力
cv2.imwrite("./images/result/facerectangle-fillter/face-recognition.jpg", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()