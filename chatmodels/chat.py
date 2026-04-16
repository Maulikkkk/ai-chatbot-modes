import os
from dotenv import load_dotenv
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

print("1 → Angry")
print("2 → Funny")
print("3 → Sad")

choice = input("Choose mode: ")

if choice == "1":
    mode = "You are an angry AI assistant..."
elif choice == "2":
    mode = "You are a funny AI assistant..."
elif choice == "3":
    mode = "You are a sad AI assistant..."
else:
    mode = "You are a helpful AI assistant."

messages = [SystemMessage(content=mode)]

while True:
    prompt = input("You: ")

    if prompt == "exit":
        break

    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)