# Playground for GPT API's

Simple, cool, and useful mini-projects. Audio files are in the `language/podcast/story_files` folder. Text to speech is in the `scripts` folder. Instructions to create prompts to run on relevant GPT versions online are in the `prompts` folder (makes the story generator below somewhat redundant unless you want greater length and customizability for your narrative).

## Custom language learning

Simple tool to learn vocab (and grammar) for any language using an infinite number of dynamically generated, easy-to-understand examples. The guiding principle is that it makes more sense to learn new vocab words by rephrasing them in the target language, rather than by translating them to English.

Each speech file consists of the following structured components:
* Word and pronunciation
* Meaning (including synonyms)
* Example sentence

The files are stored as mp3 in the `speech_files` directory, so you can transfer them to your phone or start a podcast or whatever.

## GPT groupthink

Recursively iterates on an idea (given feedback) to reach the optimal conclusion. Use case is for delving into debate or brainstorm sessions.

3 components:
* Writer - generates main ideas
* Advisor - provides feedback
* QA - determines improvement

Though to be clear, the result is not that great in practice, especially after many iterations.

## Story generator

Generates a cohesive story from a given genre, topic, and length. Use case is for creating articles, podcasts, or novels.

3 phases:
* Generate idea and outline
* Create story draft
* Revise and finalize story

An expansion of GroupThink, but the result is still way too cliched and the parts don't fit together as well as they need to.