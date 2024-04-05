import random
from openai import OpenAI

client = OpenAI(api_key="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")

system_command = "You are a helpful brainstorming assistant."

novel_ideas = "You are brainstorming ideas for a new novel. I will give you a genre, and your task is to create an original story idea that will captivate readers and resonate with their interests and emotions. The story idea you generate should be imaginative, creative, and well-thought out, with a logical beginning, middle, and end. Make sure to incorporate nuanced characters and places to bring the world to life. The format of your response should be a short but detailed, one-paragraph description of the story idea, beginning with this sentence: 'You are a {genre} writer. The story you will write is about {idea}', and ending with this sentence: 'Keeping this overarching narrative in mind, it is your goal to write a 5000 word long story, weaving together intricate details and meaningful emotions, such that the end result will logically form a cohesive narrative.'"

novel_genres = ["science fiction", "fantasy", "romance", "historical fiction"]

while True:
    target_genre = "\n\nThe genre is: " + novel_genres[random.randint(0, len(novel_genres) - 1)]
    generator = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_command},
            {"role": "user", "content": novel_ideas + target_genre}
        ]
    )
    prompt = generator.choices[0].message.content
    print(prompt)