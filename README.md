# Type IT - Offline AI Typing Assistant

Automatically correct typos, capitalization, grammar errors, and casing using a large language model, accessible via convenient keyboard shortcuts.

# Features

- **Offline AI Correction**: Leverages a local large language model (LLM) for real-time text correction, no internet connection is required.
- **Hotkey Integration**: Trigger text correction seamlessly using F9 (for selected text) and F10 (for the current line).
- **Clipboard Interaction**: Copies corrected text to the clipboard for effortless pasting.
- **Customizable**: Potentially adapt to different LLM endpoints and models for specific needs.

# Installation

Ensure you have Python and the required libraries installed:

```Bash
pip install -r requirements.txt
```

Set up a supported local LLM endpoint (see notes for configuration).

- Download Ollama: https://ollama.com/
- Run:
- ```Bash
  ollama run gemma:2b-instruct-q4_K_S
  ```

# Usage

- Run the script:

```Bash
python main.py
```

- Use the keyboard shortcuts:
  - **F9**: Correct the currently selected text.
  - **F10**: Correct the entire line of text where your cursor is positioned.

# Technical Details

Key Libraries:

- _pynput_: Listens for keyboard events and triggers text correction.
- _pyperclip_: Interacts with the clipboard to copy and paste text.
- _httpx_: Communicates with the local LLM endpoint for text processing.
- _logging_: Logs events and potential errors for debugging.
- _LLM Configuration_:

  - Ollama REST API
  - Default model: _gemma:2b-instruct-q4_K_S_

.

# Author

Abdulmunim Jundurahman Jemal (https://github.com/abdulmunim-jemal)

## NOTES:

- Replace any placeholder LLM information with your specific setup. (Explore Ollama.com for more details.)
- Consider adding more detailed configuration instructions for users unfamiliar with LLMs.
- Explore incorporating a visual interface or additional features to enhance user experience.
