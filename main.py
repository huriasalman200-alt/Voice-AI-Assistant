from speech_to_text import record_audio, convert_audio_to_text
from text_to_speech import speak
from dotenv import load_dotenv
from cohere import ClientV2
import os


load_dotenv()

API_KEY = os.getenv("COHERE_API_KEY")


def get_ai_response(question):
    if not API_KEY:
        raise ValueError("COHERE_API_KEY was not found in the .env file.")

    client = ClientV2(api_key=API_KEY)

    response = client.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": (
                    "أجب باللغة العربية بإجابة قصيرة وواضحة. "
                    f"السؤال: {question}"
                )
            }
        ]
    )

    return response.message.content[0].text.strip()


def save_answer(answer):
    with open("answer.txt", "w", encoding="utf-8") as file:
        file.write(answer)


def main():
    print("Voice AI Assistant started.")

    record_audio()

    question = convert_audio_to_text()

    if not question:
        print("No speech was recognized.")
        return

    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(question)

    print("Sending question to Cohere...")

    answer = get_ai_response(question)

    save_answer(answer)

    print("Answer saved successfully.")

    speak()


if __name__ == "__main__":
    main()