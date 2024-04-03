from openai import OpenAI

client = OpenAI(
    api_key="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"
)

writer_message = ""
writer_history = []
advisor_message = "Write the first chapter of the story."
advisor_history = []
qa_message = ""

optimal_story = "I sucky story. I don't know what to write. Please ignore me."

writer_system_command = f"You are a science fiction and fantasy writer. The story you are trying to create is about two twins separated at birth who grow up on two sides of a great conflict that will determine the fate of the realm. One sibling becomes the greatest warrior the world has ever seen; the other becomes the most beautiful and powerful sorceress; but in the end, they find each other and work together to unite the realm and create an long era of peace and prosperity. It is your goal to write only the first part of the story about their upbringing, weaving together great detail and deep emotion, such that the end result will logically form a cohesive narrative, taking into account the user's feedback on the relevant parts of your story so far."
writer_user_command = advisor_message

writer_history = [
        {"role": "system", "content": writer_system_command},
        {"role": "user", "content": writer_user_command}
    ]
writer = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=writer_history
)
writer_message = writer.choices[0].message.content
writer_history.append({"role": "assistant", "content": writer_message})
print("WRITER: ", writer_message, "\n\n")

advisor_system_command = f"You are a helpful and knowledgeable writing coach. You will be given parts of a story written by a science fiction and fantasy writer, and you will need to provide feedback on the writing, pointing out the strengths and weaknesses of the writing, and suggesting ways to improve the quality of the writing. You will also need to provide guidance on how to make the writing more engaging and interesting to the reader."
advisor_user_command = writer_message

advisor_history = [
        {"role": "system", "content": advisor_system_command},
        {"role": "user", "content": advisor_user_command}
    ]
advisor = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=advisor_history
)
advisor_message = advisor.choices[0].message.content
advisor_history.append({"role": "assistant", "content": advisor_message})
print("ADVISOR: ", advisor_message, "\n\n")

qa_system_command = f"You are an enthusiastic fan and reader of science fiction and fantasy, but you only like good writing. You will be given two pieces of writing, and you will need to determine which one is objectively better as measured by the quality of writing, the amount of detail and emotion conveyed, and the logical coherence of the narrative. Your reply will be either 'The first piece is better' or 'The second piece is better'. No other feedback is necessary."
qa_user_command = f"Which piece of writing is better? \n\n Here's the first piece: {optimal_story} \n\n Here's the second piece: {writer_message}"

qa = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": qa_system_command},
        {"role": "user", "content": qa_user_command}
    ]
)
qa_message = qa.choices[0].message.content
optimal_story = writer_message if "second" in qa_message else optimal_story
print("QUALITY ASSURANCE: ", optimal_story, "\n\n")

while True:
    writer_system_command = f"You are a science fiction and fantasy writer. The story you are trying to create is about two twins separated at birth who grow up on two sides of a great conflict that will determine the fate of the realm. One sibling will become the greatest warrior the world has ever seen; the other will become the most beautiful and powerful sorceress; but in the end, they will find each other and work together to unite the realm and create an long era of peace and prosperity. It is your goal to write only the first part (out of five total parts) of this story about their upbringing, weaving together great detail and deep emotion, such that the end result will logically form a cohesive narrative, taking into account the user's feedback on the relevant parts of your story so far. The five parts of the story are: 1. The twins' upbringing, 2. The twins' separation, 3. The twins' growth and development, 4. The twins' reunion, 5. The twins' final battle and victory. Remember, do not prematurely reveal later parts of the story while working on this part."
    writer_user_command = advisor_message

    writer_history.append({"role": "user", "content": advisor_message})
    writer = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=writer_history
    )
    writer_message = writer.choices[0].message.content
    writer_history.append({"role": "assistant", "content": writer_message})
    print("WRITER: ", writer_message, "\n\n")

    advisor_system_command = f"You are a helpful and knowledgeable writing coach. You will be given parts of a story written by a science fiction and fantasy writer, and you will need to provide feedback on the writing, pointing out the strengths and weaknesses of the writing, and suggesting ways to improve the quality of the writing. You will also need to provide guidance on how to make the writing more engaging and interesting to the reader."
    advisor_user_command = writer_message

    advisor_history.append({"role": "user", "content": writer_message})
    advisor = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=advisor_history
    )
    advisor_message = advisor.choices[0].message.content
    advisor_history.append({"role": "assistant", "content": advisor_message})
    print("ADVISOR: ", advisor_message, "\n\n")

    qa_system_command = f"You are an enthusiastic fan and reader of science fiction and fantasy, but you only like good writing. You will be given two pieces of writing, and you will need to determine which one is objectively better as measured by the quality of writing, the amount of detail and emotion conveyed, and the logical coherence of the narrative. Your reply will be either 'The first piece is better' or 'The second piece is better'. No other feedback is necessary."
    qa_user_command = f"Which piece of writing is better? \n\n Here's the first piece: {optimal_story} \n\n Here's the second piece: {writer_message}"

    qa = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": qa_system_command},
            {"role": "user", "content": qa_user_command}
        ]
    )
    qa_message = qa.choices[0].message.content
    optimal_story = writer_message if "second" in qa_message else optimal_story
    print("QUALITY ASSURANCE: ", optimal_story, "\n\n")
