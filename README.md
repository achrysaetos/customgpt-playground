# Playground for GPT API's

Simple, cool, and useful mini-projects.

## Custom language learning

Simple tool to learn vocab (and grammar) for any language using an infinite number of dynamically generated, easy-to-understand examples. The guiding principle is that it makes more sense to learn new vocab words by rephrasing them in the target language, rather than by translating them to English.

Each speech file consists of the following structured components:
* Word and pronunciation
* Meaning (including synonyms)
* Example sentence

The files are stored as mp3 in the `speech_files` directory, so you can transfer them to your phone or start a podcast or whatever.

## GPT groupthink

Recursively iterates on ideas (given feedback) to reach the optimal conclusion.

3 components:
* Writer - generates main ideas
* Advisor - provides feedback
* QA - determines improvement

Though to be clear, the result is not that great in practice, especially for long context windows.
