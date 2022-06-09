from flask import *
from source import *
from random import *
from db_ops import *

app = Flask(__name__)


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
    def remove_a_space(cls, type, question):
        delete_space(form_uid=request.cookies.get("form_uid"), type=type, question=question)
        return draw_home_page(form_uid=request.cookies.get("form_uid"))

    @classmethod
    def render_spaces(cls):
        spaces = []  # Список из полей, которые будут
        # отобображаться на странице редактора форм
        form_uid = str(request.cookies.get("form_uid"))
        print(form_uid)
        elements = recieve_spaces(form_uid)
        print(elements)
        for segment in elements:
            print(segment, 12345)

            match segment[1]:
                case "input":
                        spaces.append(Input(segment[2]).code)
                case "textarea":
                        spaces.append(TextArea(segment[2]).code)
                case "select":
                        pass
                case _:
                    pass
        print(spaces)
        return "".join(spaces)

    @classmethod
    def reg_new_space(cls, type, question, *variants):
        form_uid = str(request.cookies.get("form_uid"))
        add_new_space(form_uid, type, question, *variants)
        return draw_home_page(form_uid)

class Form_id:
    def __init__(self, id):
        pass


class Input:
    def __init__(self, question: str):
        self.question = question
        self.code = render_template("input_space.html", question=self.question, type="input")


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
    return page

@app.route("/spaces/")
def draw_spaces():
    return Constructor.render_spaces()


@app.route("/form_editor:<form_uid>")
def draw_home_page(form_uid):
    return render_template("form_editor_home_page.html", form_uid=form_uid)


@app.route("/remove_space/type:<type>;question:<question>/", methods=["GET", "POST"])
def remove_space(type, question):
    return Constructor.remove_a_space(type, question)



@app.route("/add_input_page:<form_uid>/")
def draw_add_input_page(form_uid):
    return render_template("add_input_page.html", form_uid=form_uid)


@app.route("/registration_input_page:<form_uid>/", methods=["GET", "POST"])
def draw_reg_input_page(form_uid):
    return Constructor.reg_new_space("input", request.form.get("question"))


if __name__ == '__main__':
    app.run()
