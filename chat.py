from openai import OpenAI
client = 'Insert API Key Here'
chat_history = [{"role": "system", "content": "You are a helpful assistant."}]


while True:
    user_input =input("You: ")
    if user_input.lower() in ["die","quit"]:
        break
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    print("GPT:", reply)