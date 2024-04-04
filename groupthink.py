from openai import OpenAI

client = OpenAI(api_key="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")

writer_system_command = "You are a hedge fund investor. You are talking to the user, who is a knowledgeable and experienced financial advisor. You want to invest in NVDA, and you will need to provide a detailed explanation of why you think it is a good investment in response to his concerns about the company's future prospects."
advisor_system_command = "You are a helpful and knowledgeable financial advisor. You are talking to the user, who is a hedge fund investor wanting to invest in NVDA. Your goal is to provide a detailed critique of his assumptions and explain why you think it is not a good investment right now."
qa_system_command = "You are a knowledgeable and experienced investor. You don't know whether NVDA is a good investment or not, but you're talking to another investor, and it's your goal to determine whether his analysis is becomming more or less comprehensive over time."

advisor_message = "NVDA might not be a good buy currently."

writer_history = [{ "role": "system", "content": writer_system_command }]
advisor_history = [{ "role": "system", "content": advisor_system_command }]
qa_history = [{ "role": "system", "content": qa_system_command }]

def converse(user, user_message, history):
    history.append({ "role": "user", "content": user_message })
    model = "gpt-3.5-turbo" if user == "WRITER" else "gpt-3.5-turbo" # or gpt-4-turbo-preview
    response = client.chat.completions.create(model=model, messages=history)
    content = response.choices[0].message.content
    history.append({"role": "assistant", "content": content})
    print(f"{user.upper()}: ", content, "\n\n") # or history to debug
    return content

while True:
    writer_message = converse(user="WRITER", user_message=advisor_message, history=writer_history)
    advisor_message = converse(user="ADVISOR", user_message=writer_message, history=advisor_history)
    qa_message = converse(user="QA", user_message=writer_message, history=qa_history)