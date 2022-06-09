from flask import *
from source import *
from random import *


app = Flask(__name__)

# Список из полей, которые будут
# отобображаться на странице редактора форм
spaces = []

# Список из последовательностей type, question, variants(опционально),
# которые попадут в БД
elements = []


class Constructor:
    def __init__(self):
        super().__init__()

    @classmethod
    def get_form_id_for_input(cls):
        form_id = request.form["form_id"]
        return form_id

    @classmethod
    def build_id_element(cls, id):
        return f"""<div style="position:relative; left:18%">
        <label name="form_id">{id}</label>
        <p></p>
        """

    @classmethod
    def render_spaces(cls):
        elements = str(request.cookies.get("elements")).split("#$#")
        for tmp in elements:
            ready_tmp = tmp.split(",")
            match ready_tmp[1]:




    @classmethod
    def reg_new_input_space(cls, question):
        form_uid = str(request.cookies.get("form_uid"))
        elements = str(request.cookies.get("elements"))
        elements += f"""""{form_uid}", "input", "{question}", ""#$#"""
        page = make_response(draw_home_page(form_uid=form_uid))
        page.set_cookie("elements", str(elements), max_age=60)
        return page


class Form_id:
    def __init__(self, id):
        pass


class Input:
    def __init__(self, question: str):
        self.question = question
        self.code = f"""
                    <div style="position: relative; width: 120%; left: 18%; top:140px; z-index: 3">
                    <p1></p1>
                    <p2>{self.question}</p2>
                    <input name="{self.question}">
                    </input> 
                    </div>
                    <p3></p3>"""


class TextArea:
    def __init__(self, question: str):
        self.question = question
        self.code = f"""<form>
                    <p>{self.question}</p>" \
                    <textarea name={self.question}>
                    </textarea>
                    </form>
                    <p></p>"""


class Select:
    def __init__(self, question: str, variants: list):
        self.question = question
        self.variants = variants


        self.code = "".join(["""<div style="position:absolute; left:18%; top:10%; z-index:3">""",
                             f"<p>{self.question}</p>", "<form>", self.compile_variants(), "</form>", "</div>"])

    def compile_variants(self):
        code = ""
        for i in self.variants:
            code += f"""<input type="radio" name="{i}" value="{i}"> {i}<br>\n"""
        return code


def generate_id():
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    form_id = ""
    for _ in range(10):
        form_id += choice(symbols)
    return form_id


@app.route('/')
def draw_start_page():
    form_uid = generate_id()
    page = make_response(draw_home_page(form_uid=form_uid))
    page.set_cookie("form_uid", form_uid, max_age=60)
    page.set_cookie("elements", "", max_age=60)
    return page


@app.route("/form_editor:<form_uid>")
def draw_home_page(form_uid):
    return render_template("form_editor_home_page.html", form_uid=form_uid, spaces=f"""{request.cookies.get("form_uid")}""")


@app.route("/add_input_page:<form_uid>/")
def draw_add_input_page(form_uid):
    return render_template("add_input_page.html", form_uid=form_uid)


@app.route("/registration_input_page:<form_uid>", methods=["GET", "POST"])
def draw_reg_input_page(form_uid):
    return Constructor.reg_new_input_space(request.form["question"])


if __name__ == '__main__':
    app.run()
