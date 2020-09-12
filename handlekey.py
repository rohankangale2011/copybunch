from pynput.keyboard import Listener, Key
    
def on_press(key):
    if hasattr(key, 'char'):
        if str(ord(key.char)) == "3": # detect for "c" keypress event
            print("C Pressed")
                
        if str(ord(key.char)) == "2": # detect for "b" keypress event
            print("B Pressed")
    elif key == Key.esc : 
        exit(0) 
    else:
        pass

with Listener(on_press=on_press) as listener:  # Setup the keypress listener
    listener.join()