from openai import OpenAI

client = OpenAI(api_key="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")

####################################################################################################

### User input here

genre = "science fiction and fantasy"
story = "The story is about two twins separated at birth who grow up on two sides of a great conflict that will determine the fate of the realm. One sibling becomes the greatest warrior the world has ever seen; the other becomes the most beautiful and powerful sorceress; but in the end, they find each other and work together to unite the realm and create an long era of peace and prosperity."
num_parts = 3

####################################################################################################

### Generate idea and outline

story_command=[{"role": "system", "content": f"You are a prolific {genre} brainstormer. You will be given a few brief sentences about what a story should be about, and you will need to extrapolate and create an original and engaging story idea for what the user should write about, based on their input. The story should be imaginative, creative, and well thought out, with a logical beginning, middle, and end. The format of your response should be: 'The story you are trying to write is about...' followed by a short but detailed, one-paragraph description of the story idea."},{"role": "user", "content": story}]
story_idea = client.chat.completions.create(model="gpt-3.5-turbo", messages = story_command).choices[0].message.content.replace('\n', ' ')
story_command.extend([{"role": "assistant", "content": story_idea}, {"role": "user", "content": f"Now create an outline for the story, with {num_parts} numbered parts in total, each part logically leading to the next part and logically following from the previous part, with the ultimate goal of creating a complete and cohesive narrative. The format of your response should simply be a list of {num_parts} parts, each part starting with a number and a period, followed by a brief one-sentence description of the part and ending with a comma, like this: '1. , 2. , 3. ,' and so on."}])
story_parts = client.chat.completions.create(model="gpt-3.5-turbo", messages = story_command).choices[0].message.content.replace('\n', ' ')

### Create story draft

writer_command = f"You are a {genre} writer. {story_idea} The story has {num_parts} parts altogether, but you'll only write about the current part, which is either one of: {story_parts} Keeping this overarching narrative in mind, it is your goal to write only the part of the story stated by me (your advisor), weaving together intricate details and meaningful emotions, such that the end result will logically form a cohesive narrative, taking into account my feedback on the relevant parts of your story so far. Remember, do not prematurely reveal or foreshadow later parts of the story while working on this current part, as we'll get to those other parts in the future."
advisor_command = f"You are a helpful and knowledgeable writing advisor. You will be given parts of a story written by a {genre} writer, and you will need to logically determine where the story needs to go next in order for it to form a cohesive narrative. To do this, you will offer constructive feedback on the story so far and on your vision for where it needs to go next. You will explicitly tell the writer to write the next part of the story, also making sure to tell them to preserve relevant details, emotions, and the pace of the story. Remember, the story has {num_parts} parts altogether, but you'll only tell the writer to write about the next part of the story in this relevant sequence: {story_parts} Keep in mind that ultimately, {story_idea}"
qa_command = f"You are an enthusiastic fan and reader of science fiction and fantasy, but you only like good writing. You will be given one new piece of writing, and you will need to determine which one (out of all the pieces I've given you so far) is objectively the best as measured by the quality of writing, the amount of detail and emotion conveyed, and the logical coherence of the narrative. Your reply will be just be a verbatim copy of the best piece. No other feedback or explanation is necessary."

advisor_message = "Write the first part of the story."

writer_history = [{ "role": "system", "content": writer_command }]
advisor_history = [{ "role": "system", "content": advisor_command }]
qa_history = [{ "role": "system", "content": qa_command }]

def converse(user, user_message, history):
    history.append({ "role": "user", "content": user_message })
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=history)
    content = response.choices[0].message.content
    history.append({"role": "assistant", "content": content})
    print(f"{user.upper()}: ", content, "\n\n")
    return content

print("GOAL: ", writer_command, "\n\n")
for _ in range(num_parts):
    writer_message = converse(user="WRITER", user_message=advisor_message, history=writer_history)
    advisor_message = converse(user="ADVISOR", user_message=writer_message, history=advisor_history)

### Revise and finalize story

editor_command = f"You are a meticulous and detail-oriented {genre} writer. You will be given a paragraph written by the user, and you will need to rewrite the paragraph into a full page, in order to make it more engaging, detailed, and emotionally resonant. Your goal is to enhance the user's writing by adding more depth, complexity, and vividness to the story, thus making it more compelling and immersive for potential readers. Be sure to add meticulous details, such as extremely detailed descriptions of relevant characters or objects, movements, sights, sounds, and so on, and also add any dialog if necessary. Always be sure to show, not tell. But be sure to avoid repeating ideas and descriptions, and refrain from using too many cliches, adjectives, and adverbs! Also, do not use too many commas or dependent phrases because this makes the sentences too long and too hard to read. The goal is to make them easy to read, while still retaining core details. Most importantly, always make sure that each paragraph follows logically from the previous one, and that each paragraph also leads logically into the next one. Lastly, your response should follow logically from your last response in order to form a cohesive narrative."
editor_history = [{ "role": "system", "content": editor_command }]

for message in writer_history:
    if message["role"] == "assistant":
        paragraphs = [p for p in message["content"].split("\n") if len(p) > 100]
        for paragraph in paragraphs:
            # completion = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "system", "content": editor_command},
            #         {"role": "user", "content": paragraph}
            #     ]
            # )
            # edited_paragraph = completion.choices[0].message.content
            # print(edited_paragraph, "\n\n")
            editor_message = converse(user="EDITOR", user_message=paragraph, history=editor_history)
            