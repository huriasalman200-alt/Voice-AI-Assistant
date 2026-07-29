import sounddevice as sd
import whisper
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
RECORD_SECONDS = 5
AUDIO_FILE = "user_audio.wav"
TEXT_FILE = "recognized_text.txt"


def record_audio():
    print("Speak now for 5 seconds...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()
    write(AUDIO_FILE, SAMPLE_RATE, audio)

    print("Audio recorded successfully.")


def convert_audio_to_text():
    print("Loading Whisper model...")

    model = whisper.load_model("base")

    print("Converting audio to text...")

    result = model.transcribe(
        AUDIO_FILE,
        language="ar",
        fp16=False
    )

    return result["text"].strip()


def save_text(text):
    with open(TEXT_FILE, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    record_audio()

    recognized_text = convert_audio_to_text()

    if recognized_text:
        save_text(recognized_text)

        print("Speech recognized successfully.")
        print(f"Arabic text was saved in: {TEXT_FILE}")
    else:
        print("No speech was recognized. Please try again.")