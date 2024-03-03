from pynput import keyboard
import pynput
import pyperclip

controller = keyboard.Controller()

def process_text(text):
    return text[::-1]


def selected_text():
    with (controller.pressed(keyboard.Key.ctrl)):
        controller.tap("c")
    text = pyperclip.paste()
    text = process_text(text)
    pyperclip.copy(text)
    
    with (controller.pressed(keyboard.Key.ctrl)):
        controller.tap("v")
   

def line_text():
    controller.tap(keyboard.Key.home)
    with (controller.pressed(keyboard.Key.shift)):
        controller.tap(keyboard.Key.end)
    
    with (controller.pressed(keyboard.Key.ctrl)):
        controller.tap("c")
    
    text = pyperclip.paste()
    text = process_text(text)
    
    pyperclip.copy(text)
    with (controller.pressed(keyboard.Key.ctrl)):
        controller.tap("v")

selected_shortcut = str(keyboard.Key.f9.value) # F9
line_shortcut = str(keyboard.Key.f10.value) # F10

with keyboard.GlobalHotKeys({
        selected_shortcut: selected_text,
        line_shortcut: line_shortcut}) as h:
    h.join()