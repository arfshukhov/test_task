from peewee import *

spaces_db = "spaces.db"
forms_db = "forms.db"


class Form(Model):
    id = IntegerField()
    name = TextField()

    class Meta:
        database = forms_db


class Space(Model):
    form_id = IntegerField()
    type = TextField()
    question = TextField()

    class Meta:
        database = spaces_db


with spaces_db:
    spaces_db.create_tables([Space])

with forms_db:
    forms_db.create_tables([Form])


def create_new_form(id, name):
    ...


def add_new_space(form_id, type, question, *variants:list):
    ...