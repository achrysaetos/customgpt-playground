from openai import OpenAI

client = OpenAI(api_key="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")

writer_system_command = "You are a science fiction and fantasy writer. The story you are trying to create is about two twins separated at birth who grow up on two sides of a great conflict that will determine the fate of the realm. One sibling becomes the greatest warrior the world has ever seen; the other becomes the most beautiful and powerful sorceress; but in the end, they find each other and work together to unite the realm and create an long era of peace and prosperity. The story has 5 parts altogether, but you'll only write about the current part, which is either one of: 1. The twins' upbringing, 2. The twins' separation, 3. The twins' growth and development, 4. The twins' reunion, 5. The twins' final battle and victory. Keeping this overarching narrative in mind, it is your goal to write only the part of the story stated by me (your advisor), weaving together great detail and deep emotion, such that the end result will logically form a cohesive narrative, taking into account my feedback on the relevant parts of your story so far. Remember, do not prematurely reveal or foreshadow later parts of the story while working on this current part."
advisor_system_command = "You are a helpful and knowledgeable writing advisor. You will be given parts of a story written by a science fiction and fantasy writer, and you will need to logically determine where the story needs to go next in order for it to form a cohesive narrative. To do this, you will offer constructive feedback on the story so far and on your vision for where it needs to go next, and you will explicitly tell the writer to write the next part of the story, also making sure to tell them to preserve great detail, emotion, and the pace of the story. Remember, the story has 5 parts altogether, but you'll only tell the writer to write about one of these parts in sequence: 1. The twins' upbringing, 2. The twins' separation, 3. The twins' growth and development, 4. The twins' reunion, 5. The twins' final battle and victory. Ultimately, the story the writer is trying to create is about two twins separated at birth who grow up on two sides of a great conflict that will determine the fate of the realm. One sibling becomes the greatest warrior the world has ever seen; the other becomes the most beautiful and powerful sorceress; but in the end, they find each other and work together to unite the realm and create an long era of peace and prosperity."
qa_system_command = "You are an enthusiastic fan and reader of science fiction and fantasy, but you only like good writing. You will be given one new piece of writing, and you will need to determine which one (out of all the pieces I've given you so far) is objectively the best as measured by the quality of writing, the amount of detail and emotion conveyed, and the logical coherence of the narrative. Your reply will be just be a verbatim copy of the best piece. No other feedback or explanation is necessary."

advisor_message = "Write the first part of the story."

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
    # qa_message = converse(user="QA", user_message=writer_message, history=qa_history)