from pynput import keyboard
import pynput
import pyperclip
from string import Template
import httpx

controller = keyboard.Controller()

PROMPT_TEMPLATE = Template(
    """
    Fix All the typos, capitalization, grammar errors, and casing in the following text
    but preserve all new line characters and extra spaces and other formatting characters.
    
    $text
    
    Return only the corrected text, don't include the preamble.
    """
)

LLM_ENDPOINT = "http://localhost:11434/api/generate"
LLM_CONFIG = {
    "model": "gemma:2b-instruct-q4_K_S",
    "keepalive": "10m",
    "stream": False,
}

def process_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    
    response = httpx.post(
        LLM_ENDPOINT,
        json={"prompt": prompt, **LLM_CONFIG},
        header={"Connection-Type": "Keep-alive",
                "Content-Type": "application/json"
                    }
    )
    if not response.status_code == 200:
        return text
    
    return response.json()["text"].strip()


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