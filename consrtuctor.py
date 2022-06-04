from flask import *
from source import *


elements: list = []

app = Flask(__name__)


class Constructor:
    def __init__(self):
        super().__init__()

    @staticmethod
    @app.route('/')
    def draw_main_page():
        return "".join([opening_html_tag, default_style_set, header, open_workspace, Input("почему вы пидор обоссанный?").code,
                        close_workspace, closer_html_tag])
    @staticmethod
    @app.route("")
    def add_input_page(self):


class Input:
    def __init__(self, question):
        self.question = question
        self.code = """<div style="position: absolute; width: 120%; left: 18%; z-index: 2">"""\
                    f"<p>{self.question}</p>" \
                    f"<input name={self.question} >" \
                    "</input>"\
                    "</div>"


class TextArea:
    def __init__(self, question):
        self.question = question
        self.code = "<form>" \
                    f"<p>{self.question}</p>"\
                    f"<textarea name={self.question}>"\
                    "</textarea>"\
                    "</form>"

    ...

class Select():
    ...


if __name__ == '__main__':

    constructor = Constructor()
    constructor.run()