# 11

画像のアップロードを行うWebインターフェイスと、アップロードされた画像のファイル変更を検知して画像処理を行う画像処理プログラムを組み合わせたシステムの構築

## Main function
1. canny-fillter
    ：アップロードされた画像をCannyフィルタによって輪郭抽出する
2. facerectangle-fillter
    ：アップロードされた画像を顔検出して枠で加工する
3. grayscale-fillter
   ：アップロードされた画像をグレースケール化する

## Initial Setting

```
$ git clone https://github.com/2022AIT-OOP2-G07/11.git
$ cd 11
```

<!-- (.env) $ pip install -r requirements.txt これいるかな？？ -->

## Require
Python version : 3.10 or higher
```Text
Flask==2.2.2
opencv-python==4.6.0.66
numpy==1.23.5
matplotlib==3.6.2
tkinter==8.6
```

## Usage
```
$ python main.py
```

## 未実装
* watchdogによるディレクトリの監視
* アップロードされた画像の加工
    (watchdogが未実装のため)
* アップロードされた画像の表示
* 加工された画像の表示


## ディレクトリ構造
<pre>
11
├── GrayScale.py
├── Kuroi_Canny.py
├── README.md
├── Sato_rectangle.py
├── haarcascade_frontalface_alt.xml
├── images
│   ├── result
│   │   ├── canny-fillter
│   │   ├── facerectangle-fillter
│   │   └── grayscale-fillter
│   └── upload
├── main.py
├── static
│   ├── index.css
│   └── main.js
└── templates
    ├── filelist.html
    └── index.html
</pre>
