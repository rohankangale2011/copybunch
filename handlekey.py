from context_menu import *
from pynput.keyboard import Listener, Key, KeyCode, Controller
import time
import pyperclip
import os.path
from os import path
import pandas as pd

keyboard = Controller()

with open('bcopy_1','w+') as f1:
    f1.write("    ")
with open('bcopy_2','w+') as f2:
    f2.write("    ")
with open('bcopy_3','w+') as f3:
    f3.write("    ")
    

with open("buff_file_labels","w+") as bf:
    bf.write("    "+"..."+"\r")
    bf.write("    "+"..."+"\r")
    bf.write("    "+"..."+"\r")
    
def copy_buff():
    recent_buff = pyperclip.paste()
    with open("bcopy_1", "r+") as f1:
        f1_buff = f1.read()
        f1.seek(0)
        f1.write(recent_buff)
        f1.truncate()
    
    with open("bcopy_2", "r+") as f2:
        f2_buff = f2.read()
        f2.seek(0)
        f2.write(f1_buff)
        f2.truncate()
        
    with open("bcopy_3", "r+") as f3:
        f3_buff = f3.read()
        f3.seek(0)
        f3.write(f2_buff)
        f3.truncate()
    
    with open("bcopy_1", "r+") as f1:
        f1_label = f1.read()[0:16]
    with open("bcopy_2", "r+") as f2:
        f2_label = f2.read()[0:16]
    with open("bcopy_3", "r+") as f3:
        f3_label = f3.read()[0:16]    
          
    with open("buff_file_labels","w+") as bf:
        bf.write(f1_label+"..."+"\r")
        bf.write(f2_label+"..."+"\r")
        bf.write(f3_label+"..."+"\r")


#To detect ctrl + c combination ascii
flags={'ctl_flag':0,'c_flag':0,'shift_flag':0,'v_flag':0,'c_init_ascii_flag':0}
ascii_dict={'c':0}
    
def on_press(key):
    if key == Key.ctrl_l:
        flags['ctl_flag']=1

    if hasattr(key, 'char'):
        if flags['c_init_ascii_flag'] == 0:
            ascii_dict['c'] = int(ord(key.char))
            flags['c_init_ascii_flag']  = 1
            
        if str(ord(key.char)) == str(ascii_dict['c']):
            flags['c_flag']=1
            if flags['c_flag']==1 and flags['ctl_flag']==1: 
                time.sleep(0.3)
                copy_buff()
                
        if str(ord(key.char)) == str(ascii_dict['c'] - 1):
            flags['v_flag']=1
            if flags['v_flag']==1 and flags['ctl_flag']==1:
                with open("buff_file_labels","r") as bf:
                    labels= bf.readlines()
                    f1_label=labels[0][:-1]
                    f2_label=labels[1][:-1]
                    f3_label=labels[2][:-1]
                show_bunch(f1_label,f2_label,f3_label) 
                flags['v_flag']=0
                flags['ctl_flag']=0

    elif key == Key.esc : 
        exit(0) 
    else:
        pass


def on_release(key):
    try:
        if key == Key.ctrl_l:
            flags['ctl_flag']=0
        if key == Key.shift:
            flags['shift_flag']=0
        if hasattr(key, 'char'):
            if str(ord(key.char)) == str(ascii_dict['c']):
                flags['c_flag']=0
            if str(ord(key.char)) == str(ascii_dict['c'] - 1):
                flags['v_flag']=0
            
    except KeyError:
        pass

with Listener(on_press=on_press, on_release=on_release) as listener:  # Setup the listener
    time.sleep(5)
    keyboard.press('c')
    keyboard.release('c')
    listener.join()  # Join the thread to the main thread