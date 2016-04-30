'''
PyDomitor Step Counter V.1
    A basic health diary using a SQLight database to store and retrieve information
    
Coded By: Tyler Linne
Date: 4/29/16
'''
from peewee import *
from collections import OrderedDict
import datetime
import sys
import os



db = SqliteDatabase('diary.db')

steps_total = [0]


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        

def initialize():
    """Create the database and table"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    print("PyDomitor Step Diary!")
    print("")
    choice = None
    
    while choice != 'q':
        print("Enter 'q' to quit.")
        print('=' * 20)
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print('=' * 20)
        choice = input('What would you like to do?: ').lower().strip()
        
        if choice in menu:
            menu[choice]()

def clear():
  """clears the screen"""
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')

            
def add_entry():
    """Add a step entry."""
    print("Type in your number of daily steps. Press ctrl+d when finished.")
    print('')
    data = sys.stdin.read().strip()
    
    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")
            steps = int(data)
            steps_total.append(steps)
            clear()
    
    
def view_entries(search_query=None):
    """View previous step entries."""
    clear()
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('d) delete entry')
        print('q) return to menu')
        
        next_action = input('Action: [N|d|q] ').lower().strip()
        clear()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
    clear()


def search_entries():
    """Search previous entries."""
    print('=' * 20)
    view_entries(input('Search query: '))
    clear()

    
def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [yN] ").lower() == 'y':
        entry.delete_instance()
        print("Entry deleted!")
        clear()
        

def display_total_steps():
    """Display lifetime steps"""
    clear()
    print("Here is your total steps!")
    print(sum(steps_total))
    print('=' * 20)
     


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('t', display_total_steps),
])
  
if __name__ == '__main__':
    initialize()
    clear()
    menu_loop()