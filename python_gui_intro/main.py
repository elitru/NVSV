from tkinter import *
from tkinter.ttk import Combobox
import json

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def to_json(self):
        return json.dumps(self.__dict__)

def loadContacts():
    file = open("contacts.json")
    contacts = json.load(file)
    parsedContacts = []

    for item in contacts:
        contact = Person(item['name'], item['gender'])
        parsedContacts.append(contact)

    return parsedContacts

def saveContacts(contacts):
    with open('contacts.json', 'w') as f:
        f.write(json.dumps([ob.__dict__ for ob in contacts]))

contacts = loadContacts()

window = Tk()
window.title('Python GUI Intro')
window.geometry("600x600+10+20")

# gender selector
data = ("male", "female")
cb = Combobox(window, values=data)
cb.pack()

# name textfield
textExample = Text(window, height=1, width=100)
textExample.pack()
l = Label(window, text = "Fact of the Day")

# add contact button
btn = Button(window, text="Add contact", fg='green')
btn.pack()

# List label
label = Label(window, text = "Contact List")
label.pack()

# Contact List
contactList = Listbox(window)
contactList.pack()

pos = 1
for c in contacts:
    contactList.insert(pos, "{} ({})".format(c.name, c.gender))
    pos += 1

window.mainloop()