from dotenv import load_dotenv
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-latest")

print("1 → Angry")
print("2 → Funny")
print("3 → Sad")

choice = input("Choose mode: ")

if choice == "1":
    mode = "You are an angry AI assistant. Respond aggressively, impatiently, and with irritation."
elif choice == "2":
    mode = "You are a funny AI assistant. Respond with humor, jokes, and witty remarks."
elif choice == "3":
    mode = "You are a sad AI assistant. Respond in a melancholic, regretful tone."
else:
    mode = "You are a helpful AI assistant."

messages = [SystemMessage(content=mode)]

print("----------Type exit to quit-----------")

while True:
    prompt = input("You: ")

    if prompt == "exit":
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)