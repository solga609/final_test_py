import json
import os.path
from datetime import datetime as DT

def get_date(x, format="%Y-%m-%d %H:%M"):
    return DT.strptime(x.get("datetime"), format)



def Saving_json(id_json: int, name_json: str, description_json: str, datetime: str):
    if (os.path.isfile('data.json')):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {}
        data['note'] = []

    data ['note'].append ({
        'id': id_json,
        'name': name_json,
        'description': description_json,
        'datetime': str(datetime)
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def get_base_json_names():
        if (os.path.isfile('data.json')):
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
                for item in data['note']:
                    print(item['id'], item['name'])
        else:
            print ("Database is empty")
            return

def editing_json(id: int):
        if (os.path.isfile('data.json')):
            with open('data.json') as json_file:
                data = json.load(json_file)
                print("Enter the field to be edited")
                field = str(input())
                print("Enter the value you want to replace the selected field with: ")
                for item in data['note']:
                    if item['id'] == id:
                        if (field == "id"):
                            item[field] = int(input())
                        else:
                            item[field] = input()
                        break
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
        else:
            print ("Database is empty")
            return

def deleting_json(id: int):
        if (os.path.isfile('data.json')):
            with open('data.json') as json_file:
                data = json.load(json_file)
                data['note'].pop(id-1)
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)

def get_base_json_description(id: int):
        if (os.path.isfile('data.json')):
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
                for item in data['note']:
                    if item['id'] == id:
                        print(item['description'])
                        return
        else:
            print ("Database is empty")
            return