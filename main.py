from pynput import keyboard
import pyperclip
import httpx
import logging
from string import Template
# Logging Configs
logging.basicConfig(level=logging.DEBUG, filename='log.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# LLM Constants
PROMPT_TEMPLATE = Template(
    """
    Fix All the typos, capitalization, grammar errors, and casing in the following text
    but preserve all newline characters, extra spaces and other formatting characters.
    
    $text
    
    Return only the corrected text, excluding the preamble.
    """
)

LLM_ENDPOINT = "http://localhost:11434/api/generate"
LLM_CONFIG = {
    "model": "gemma:2b-instruct-q4_K_S",
    "keepalive": "10m",
    "stream": False,
}

# Logging instance
logger = logging.getLogger(__name__)

def process_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    
    try:
        response = httpx.post(
            LLM_ENDPOINT,
            json={"prompt": prompt, **LLM_CONFIG},
            headers={"Connection-Type": "Keep-alive",
                    "Content-Type": "application/json"
                        }
        )
        response.raise_for_status()
        return response.json()["text"].strip()
    except httpx.HTTPError as http_err:
        logger.error(f"HTTP error occured Connecting to the LLM Endpoint: {http_err}")
    except Exception as e:
        logger.error(f"An Error occured Connecting to the LLM Endpoint: {e}")
    return text


controller = keyboard.Controller()

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
        line_shortcut: line_text}) as h:
    h.join()