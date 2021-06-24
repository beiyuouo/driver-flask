# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/6/24 11:42
# Description:

__author__ = "BeiYu"

from flask import Flask
import os
from flask import send_from_directory

app = Flask(__name__)

# 新建images文件夹，UPLOAD_PATH就是images的路径
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.makedirs(UPLOAD_PATH, exist_ok=True)


# 访问上传的文件
# 浏览器访问：http://127.0.0.1:5000/images/django.jpg/  就可以查看文件了
@app.route('/files/<filename>/', methods=['GET', 'POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7777)
