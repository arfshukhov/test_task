from flask import *
from source import *

app = Flask(__name__)


class Constructor:
    def __init__(self):
        super().__init__()

    elements: list = []

    @staticmethod
    @app.route('/')
    def draw_main_page():
        return "".join([opening_html_tag, default_style_set, header, open_workspace, add_space_buttons,
                        Input("how are you?").code, close_workspace, closer_html_tag])

    @staticmethod
    @app.route("/add_input_page/")
    def draw_add_input_page():
        return add_input_page


class Input:
    def __init__(self, question):
        self.question = question
        self.code = """<div style="position: absolute; width: 120%; left: 18%; z-index: 2">""" \
                    f"<p>{self.question}</p>" \
                    f"<input name={self.question} >" \
                    "</input>" \
                    "</div>"


class TextArea:
    def __init__(self, question):
        self.question = question
        self.code = "<form>" \
                    f"<p>{self.question}</p>" \
                    f"<textarea name={self.question}>" \
                    "</textarea>" \
                    "</form>"

    ...


class Select():
    ...


if __name__ == '__main__':
    constructor = Constructor()
    constructor.run()
