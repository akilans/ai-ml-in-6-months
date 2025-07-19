from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_llm(messages):
    return client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=messages
    )

messages = [
        {"role": "system","content":"You are nerd AI agent"}
    ]

while True:
    user_input = input("Ask me anything!: ")
    if user_input == "exit":
        break
    else:
        messages.append({"role": "user","content":user_input})
        response = call_llm(messages)
        answer = response.choices[0].message.content
        print(answer)
        messages.append({"role": "system","content":answer})
