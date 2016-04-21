'''
Py-Room Service, a simple application to order breakfast
Coded by: Tyler Linne
Version: 1.1
Date: 4/21/16
'''

import os
import sys
from datetime import datetime


def clear():
  '''clears the screen'''
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')
      
def welcome():
  '''prints out a welcome screen'''
  print('Welcome to Py-Room Service!')
  print('')
  print('Date: ' + str(datetime.now()))
  print('')
  start = input("Press Enter/Return to order or Q to quit ").lower()
  if start == 'q':
      clear()
      print('-' * 30)
      print("Thank you, enjoy your stay!")
      print('-' * 30)
      sys.exit()
  else:
      clear()
clear()
welcome()
while True:
    print("Hello, Please Select a Menu Item by Number")
    print("1. Fried Eggs")
    print("2. Pancakes")
    print("3. Breakfast Meats")
    print("4. Cereal")
    
    on = (""" 
--------------------------
Your order is on it's Way!""")
    end = ("""
---------------------------
Thank You, Enjoy Your Stay!""")
    
    try:
        selection = int(input("Type Your Choice Here: "))
    except ValueError:
        print("Please Enter a Number, Try Again")
        continue
    else:
        clear()
        
        if selection == 1:
            clear()
            print("How Would You Like Your Eggs Cooked?")
            print("1. Over Easy")
            print("2. Over Hard")
            print("3. Scrambeled")
            e_cooked = int(input("Type Your Choice Here: "))
            
            if e_cooked == 1:
                clear()
                print("You Chose Eggs, Cooked Over Easy." + on + end)
                break
            elif e_cooked == 2:
                clear()
                print("You Chose Eggs, Cooked Over Hard." + on + end)
                break
            elif e_cooked == 3:
                clear()
                print("You Chose Eggs, Scrambeled." + on + end)
                break
            else:
                print('')
                print("Wrong Input, Please select 1-3")
                print('')
        elif selection == 2:
            clear()
            print("What Kind of Pancakes Would You Like?")
            print("1. Plain")
            print("2. Chocolate Chip")
            print("3. Berries")
            pcake = int(input("Type Your Choice Here: "))
            
            if pcake == 1:
                clear()
                print("You Chose Plain Pancakes." + on + end)
                break
            elif pcake == 2:
                clear()
                print("You Chose Chocolate Chip Pancakes." + on + end)
                break
            elif pcake == 3:
                clear()
                print("You Chose Berry-Mix Pancakes." + on + end)
                break
            else:
                print('')
                print("Wrong Input, Please select 1-3")
                print('')
        elif selection == 3:
            clear()
            print("What Meat Would You Like?")
            print("1. Bacon")
            print("2. Ham")
            print("3. Sausage")
            m_choice = int(input("Type Your Choice Here: "))
            
            if m_choice == 1:
                clear()
                print("You Chose to Have Bacon." + on + end)
                break
            elif m_choice == 2:
                clear()
                print("You Chose to Have Ham." + on + end)
                break
            elif m_choice == 3:
                clear()
                print("You Chose to Have Sausage." + on + end)
                break
            else:
                print('')
                print("Wrong Input, Please select 1-3")
                print('')
                continue
        elif selection == 4:
            clear()
            print("What Kind of Cereal Would You Like?")
            print("1. Happy-o's")
            print("2. Admiral Chomp")
            print("3. Oatmeal")
            c_choice = int(input("Type Your Choice Here: "))
            
            if c_choice == 1:
                clear()
                print("You Chose to Have Happy-o's" + on + end)
                break
            elif c_choice == 2:
                clear()
                print("You Chose to have Admiral Chomp" + on + end)
                break
            elif c_choice == 3:
                clear()
                print("You Chose to Have Oatmeal" + on + end)
                break
            else:
                print("Wrong Input, Please select 1-3")
                continue
        else:
            print("Please Try again, Choose a Listed Number")
            clear()
            continue
    
