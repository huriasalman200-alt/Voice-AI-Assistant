from gtts import gTTS
from playsound import playsound
import os

ANSWER_FILE = "answer.txt"
OUTPUT_AUDIO = "answer.mp3"

def speak():
    if not os.path.exists(ANSWER_FILE):
        print("answer.txt not found!")
        return

    with open(ANSWER_FILE, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("No text found!")
        return

    print("Converting text to speech...")

    tts = gTTS(text=text, lang="ar")
    tts.save(OUTPUT_AUDIO)

    print("Playing audio...")
    playsound(OUTPUT_AUDIO)


if __name__ == "__main__":
    speak()