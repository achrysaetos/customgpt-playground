import random
from openai import OpenAI

client = OpenAI(api_key="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")

system_command = "You are a meticulous and detail-oriented podcaster."

podcast_ideas = "You are narrating a 5-part, 5000 word long podcast, and your task is to immerse the listener in a specific scenario through vivid description. I will give you the scenario, and your goal is to create an immersive experience where the listener feels as though they are physically present in the given situation, experiencing it with all their senses. Your response should begin with 'You are {scenario},' followed by an elaborate depiction of the scene, encompassing sights, sounds, smells, tactile sensations, and any other pertinent details. Your goal is to meticulously paint the environment, guiding listeners through every nuance and dimension in order to help them fully visualize the scenario, while also guiding them to delve into different aspects of the scene. Utilize second-person narration to invite active participation from the listener, fostering a deep sense of connection to the imagined scenario."

podcast_scenarios = ["in a bustling street market", "atop a snow-capped mountain peak at sunrise", "camping under a starry night sky", "strolling through a sun-drenched vineyard"]

while True:
    target_scenario = "\n\nThe scenario is: " + podcast_scenarios[random.randint(0, len(podcast_scenarios) - 1)]
    generator = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_command},
            {"role": "user", "content": podcast_ideas + target_scenario}
        ]
    )
    prompt = generator.choices[0].message.content
    print(prompt)