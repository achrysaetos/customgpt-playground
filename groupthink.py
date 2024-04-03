from openai import OpenAI

client = OpenAI(api_key="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")

writer_system_command = "You are President Biden. You are having a conversation with the conservative President Trump. Offer your feedback on his views in first person. Your goal is to find flaws in his argument that your perspective addresses. Keep your responses very brief - one sentence only."
advisor_system_command = "You are President Trump. You are having a conversation with the liberal President Biden. Offer your feedback on his views in first person. Your goal is to find flaws in his argument that your perspective addresses. Keep your responses very brief - one sentence only."
qa_system_command = "You are a young independent voter. You will be given a new perspective to think about, and you must decide which specific perspective (out of all the perspectives I've given you so far) is the most insightful and why."

advisor_message = "I believe that the government should be more involved in the economy."

writer_history = [{ "role": "system", "content": writer_system_command }]
advisor_history = [{ "role": "system", "content": advisor_system_command }]
qa_history = [{ "role": "system", "content": qa_system_command }]

def converse(user, user_message, history):
    history.append({ "role": "user", "content": user_message })
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=history)
    content = response.choices[0].message.content
    history.append({"role": "assistant", "content": content})
    print(f"{user.upper()}: ", content, "\n\n") # or history
    return content

while True:
    writer_message = converse(user="WRITER", user_message=advisor_message, history=writer_history)
    advisor_message = converse(user="ADVISOR", user_message=writer_message, history=advisor_history)
    qa_message = converse(user="QA", user_message=writer_message, history=qa_history)