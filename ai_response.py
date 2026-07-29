import os
from dotenv import load_dotenv
from cohere import ClientV2

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

client = ClientV2(api_key=api_key)

# قراءة السؤال من الملف
with open("recognized_text.txt", "r", encoding="utf-8") as file:
    question = file.read()

print("Question:")
print(question)

# إرسال السؤال إلى Cohere
response = client.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

answer = response.message.content[0].text

print("\nAnswer:")
print(answer)

# حفظ الإجابة في ملف
with open("answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("\nAnswer saved in answer.txt")