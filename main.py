from flask import Flask, request, render_template, jsonify,Blueprint
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import glob
import os


# add_static = Blueprint('images', __name__, static_url_path='/images/result', static_folder='./images/result')
add_images1 = Blueprint('images1', __name__, static_url_path='/images/upload', static_folder='./images/upload')

app = Flask(__name__)

app.register_blueprint(add_images1)
# app.register_blueprint(add_static)



UPLOAD_FOLDER = 'images/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024  ##画像のサイズ指定

@app.route("/upload", methods=["POST"])
def upload():
    try:
        img_file = request.files['img_file']
    except RequestEntityTooLarge as err: # 1MBを超えた場合
        return jsonify({
            'status': 'fasle',
            'message': "アップロード可能なファイルサイズは1MBまでです"
        })
    filename = secure_filename(img_file.filename)
    img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'status': 'true'})

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
