# Mashal Text to Speech 🎙️

A simple Python Text-to-Speech (TTS) project created by **Mashal Khan**. This project converts written text into spoken audio and saves it as an MP3 file using the Google Text-to-Speech (gTTS) library.

## About the Project

This project demonstrates how Python can convert text into speech. It takes a text message, generates spoken audio in English, and saves the result as `voice.mp3`.

## Features

- Convert text into speech using Python.
- Generate English voice audio.
- Save the generated audio as an MP3 file.
- Simple and beginner-friendly code.

## Requirements

- Python 3
- gTTS library
- Internet connection

## Installation

Install the required Python library:

```bash
pip install gTTS
```

## Usage

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Run the Python script:

```bash
python text_to_speech.py
```

4. The generated audio will be saved as `voice.mp3` in the project folder.

## Python Code

```python
from gtts import gTTS

text = "Hey, I am Mashal Khan from Pakistan, KPK. I am a Python developer and a future AI engineer. Thank you!"

tts = gTTS(text=text, lang="en")

tts.save("voice.mp3")

print("Audio saved successfully. Thank you!")
```

## Example Output

```text
Audio saved successfully. Thank you!
```

The program generates an audio file named `voice.mp3`.

## Author

**Mashal Khan**

Python Developer | AI Student | Future AI Engineer

GitHub: [mashalkhanai11222-dotcom](https://github.com/mashalkhanai11222-dotcom)

## Learning Purpose

This project was created for learning Python programming and exploring text-to-speech technology.
