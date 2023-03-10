def Choice():
    print ("Select an action: 1 - add entry, 2 - list notes, 3 - read note, 4 - edit note, 5 - delete note")
    return int(input())

def Choice_find():
    print ("Select an action: 1 - search by last name")
    return int(input())

def id_input():
    return int(input('Enter note index: '))

def Name_input():
    return input('Enter title: ')

def Description_input():
    return input('Enter a description:') 

def Find(a):
    print ("Enter a search term: ")
    if (a != 3):
        return input()
    else:
        return int(input())