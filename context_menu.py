import tkinter as tk
import pynput.keyboard  as kb
import pynput.mouse as ms
import pyperclip
import time
from tooltip import CreateToolTip

def show_bunch(f1,f2,f3):
    def OnButtonClick(button_id):
       if button_id == 1:
           with open('bcopy_1','r') as f:
            pyperclip.copy(f.read())
           window.destroy() # first destroy window then paste
           time.sleep(0.1)
           with keyb.pressed(kb.Key.ctrl):
            keyb.press('v')
            keyb.release('v')
            
       elif button_id == 2:
        with open('bcopy_2','r') as f:
            pyperclip.copy(f.read())
        window.destroy() # first destroy window then paste
        time.sleep(0.1)
        with keyb.pressed(kb.Key.ctrl):
         keyb.press('v')
         keyb.release('v')

       elif button_id == 3:
        with open('bcopy_3','r') as f:
            pyperclip.copy(f.read())
        window.destroy() # first destroy window then paste
        time.sleep(0.1)
        with keyb.pressed(kb.Key.ctrl):
            keyb.press('v')
            keyb.release('v')

       elif button_id == 4:
        window.destroy()
       
       else:
           pass

    mouse = ms.Controller()
    keyb = kb.Controller()
    
    window = tk.Tk()
    
    co= mouse.position
    window.geometry('+%d+%d'%(co[0],co[1])) 
    window.lift()
    window.attributes("-topmost", True)
    window.overrideredirect(1) #remove title bar
    
    button1 = tk.Button(text=f1,width=20,height=1, command=lambda: OnButtonClick(1))
    button2 = tk.Button(text=f2,width=20,height=1, command=lambda: OnButtonClick(2))
    button3 = tk.Button(text=f3,width=20,height=1, command=lambda: OnButtonClick(3))
    button4 = tk.Button(text='  X  ',width=20,height=1, command=lambda: OnButtonClick(4))
    
    if f1 != "    ...":
        button1.pack()
    if f2 != "    ...":
        button2.pack()
    if f3 != "    ...":
        button3.pack()
    button4.pack()
    
    with open("bcopy_1", "r") as f1:
        f1_cont = f1.read()[0:100]
    with open("bcopy_2", "r") as f2:
        f2_cont = f2.read()[0:100]
    with open("bcopy_3", "r") as f3:
        f3_cont = f3.read()[0:100]  
        
    CreateToolTip(button1, text = f1_cont)
    CreateToolTip(button2, text = f2_cont)
    CreateToolTip(button3, text = f3_cont)
    
    window.mainloop()