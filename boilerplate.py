'''
Author : your_name
Project Name : Keylogger
Date Created : date '''

# Problem Statement : write a function for sending log file to an email

''' Import Libraries - pynput'''
import #type libs required


''' Intialize a counter(count) with 0 
    create an empty list named (keys)'''
count = 0
keys = []  # each key will be appended to the list then to key log file

''' Create a function (name = on_press) (parameters = key) now create global variable (keys,count) now append key in 
keys list then increase count by 1  '''
def on_press(key):
    #create function here

''' Create a function (write_file) (parameters= keys)
     '''
def write_file(keys): ''' This is Task - 1'''
    #write the function here

''' Create a function(on_release) (parameters= key)
    intiate an if statement for checking esc key pressed, return False ,then it will stop the keylogger '''
def on_release(key):
    #write a function here

''' create listener and assign on_press to on_press and on_release to on_release as listener 
    then use listeners join function. '''

''' Task-2 : Create a function to send the email .   '''


