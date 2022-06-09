from peewee import *
import time

spaces_db = SqliteDatabase("spaces.db")
forms_db = SqliteDatabase("forms.db")


class Forms(Model):
    form_uid = TextField(unique=True)
    name = TextField()
    data = TimeField()

    class Meta:
        database = forms_db


class Spaces(Model):
    form_uid = TextField()
    type = TextField()
    question = TextField()
    variants = TextField()

    class Meta:
        database = spaces_db


with spaces_db:
    spaces_db.create_tables([Spaces])

with forms_db:
    forms_db.create_tables([Forms])


def create_new_form(form_uid, name):
    Forms.insert(form_uid=form_uid, name=name).execute()


def add_new_space(form_uid, type, question, *variants: list):
    if type == "select":
        ready_variants = "#$#".join(*variants)
        Spaces.insert(form_uid=form_uid, type=type, question=question, variants=ready_variants).execute()
    else:
        Spaces.insert(form_uid=form_uid, type=type, question=question, variants="").execute()


def recieve_spaces(form_uid):
    elements: list = []
    f_id = Spaces.select().where(Spaces.form_uid==form_uid)
    for d in f_id:
        elements.extend([[d, d.type, d.question, d.variants]])
    return elements


def delete_space(form_uid, type, question):
    Spaces.delete().where(Spaces.form_uid == form_uid, Spaces.type == type,
                          Spaces.question == question).execute()



