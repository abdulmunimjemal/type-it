from pynput import keyboard, Key

def selected_text():
    print('ADDED F9 AS SHORTCUT')

def line_text():
    print('ADDED F10 AS SHORTCUT')

selected_shortcut = str(Key.f9.value) # F9
line_shortcut = str(Key.f10.value) # F10

with keyboard.GlobalHotKeys({
        selected_shortcut: selected_text,
        line_shortcut: line_shortcut}) as h:
    h.join()