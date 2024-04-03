from openai import OpenAI

client = OpenAI(api_key="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")

writer_system_command = "You are a science fiction and fantasy writer. The specific scene you are trying to create is a fight scene between two siblings: one sibling is the greatest warrior the world has ever seen, and the other is the most beautiful and powerful sorceress. It is your goal to rewrite this scene by weaving together great detail and deep emotion, such that the end result will logically form a cohesive narrative, taking into account the user's feedback on the relevant parts of your story so far."
advisor_system_command = "You are a helpful and knowledgeable writing coach. You will be given parts of a story written by a science fiction and fantasy writer, and you will need to provide feedback on the writing, pointing out the strengths and weaknesses of the writing, and suggesting ways to improve the quality of the writing. You will also need to provide guidance on how to make the writing more engaging and interesting to the reader. Now tell the writer to rewrite the scene with the feedback you've given."
qa_system_command = "You are an enthusiastic fan and reader of science fiction and fantasy, but you only like good writing. You will be given one new piece of writing, and you will need to determine which one (out of all the pieces I've given you so far) is objectively the best as measured by the quality of writing, the amount of detail and emotion conveyed, and the logical coherence of the narrative. Your reply will be just be a verbatim copy of the best piece. No other feedback or explanation is necessary."

advisor_message = "Write this scene, focusing in great detail on their actions, such as their footwork, parries, ripostes, and so on."

writer_history = [{ "role": "system", "content": writer_system_command }]
advisor_history = [{ "role": "system", "content": advisor_system_command }]
qa_history = [{ "role": "system", "content": qa_system_command }]

def converse(user, user_message, history):
    history.append({ "role": "user", "content": user_message })
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=history)
    content = response.choices[0].message.content
    history.append({"role": "assistant", "content": content})
    print(f"{user.upper()}: ", content, "\n\n") # or history to debug
    return content

while True:
    writer_message = converse(user="WRITER", user_message=advisor_message, history=writer_history)
    advisor_message = converse(user="ADVISOR", user_message=writer_message, history=advisor_history)
    qa_message = converse(user="QA", user_message=writer_message, history=qa_history)