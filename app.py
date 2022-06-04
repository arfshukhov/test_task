from flask import Flask, render_template, url_for, request
import requests

import consrtuctor
from consrtuctor import *


#app = Flask(__name__)


"""@app.route('/')
def hello():
    return """"""<form action="/hello/" method="get">
  <div>
    <button>go to next</button>
  </div>
</form>"""


"""@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return "".join([TextArea("1234556").code, Input("qasdfwq").code])"""


"""<form action="/hello/send/" method="post">
   <p><input name="login"> <input type="password" name="pass"></p>
   <p><input type="submit"></p>
  </form>

@app.route("/hello/send/", methods=['GET', 'POST'])
def b():
    res = request.form['login']
    print(res)
    return hello_world()"""












if __name__ == '__main__':
    constructor = Constructor()
