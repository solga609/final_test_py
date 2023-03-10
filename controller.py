import db, gui
from datetime import datetime


def button_click():
    a = gui.Choice()
    if (a == 1):
        id = gui.id_input()
        name = gui.Name_input()
        description = gui.Description_input()
        print("The data will be written in json format:")
        current_datetime = str(datetime.now())
        db.Saving_json(id, name, description, current_datetime)
    elif (a == 2):
        db.get_base_json_names()
    elif (a == 3):
        print("Enter the id of the note you want to read")
        id_found = int(input())
        db.get_base_json_description(id_found)
    elif (a == 4):
        print("Enter the id of the note you want to edit")
        id_found = int(input())
        db.editing_json(id_found)
    elif (a == 5):
        print("Enter the id of the note you want to delete")
        id_found = int(input())
        db.deleting_json(id_found)
