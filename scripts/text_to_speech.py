text = """

The success of their steam engine project marked a turning point for Adelaide and Alexander. Society's resistance to their union and work persisted, but with tangible proof of their achievements, opinions began to shift slowly. Adelaide's reputation as an engineer grew, her name becoming synonymous with innovation and determination.

For Alexander, the success strengthened his resolve in his covert endeavors for social change. His involvement with the social reform group, once a source of internal conflict, now became an integral part of his identity, shared openly with Adelaide.

The challenges they faced together served to strengthen their relationship. They learned to navigate the intricacies of their public and private lives, becoming adept at balancing their social responsibilities with their personal ambitions.

As Adelaide and Alexander grew closer, they found that their love was not just a product of mutual respect and shared goals but also of a deep understanding of each other's vulnerabilities and strengths. They became each other's confidant, supporter, and most importantly, equal partner in all endeavors.

Their relationship, once a source of contention, became a symbol of progress and possibility. They showed that love could thrive amidst ambition and that societal norms could be challenged and redefined.

Their bond was not without its trials, but each obstacle only served to deepen their commitment to each other and their causes. They became a testament to the power of unity in the face of adversity, inspiring others in their circles to rethink their perceptions and biases.

Years later, Adelaide and Alexander remained at the forefront of social and technological progress. Their steam engine innovation paved the way for new advancements, transforming industries and societal norms alike. They continued to work tirelessly, both in their professional fields and within the social reform movement, driven by a shared vision of a more equitable and progressive world.

Their love story, interwoven with their professional achievements, became a tale recounted in households and workshops throughout London. It served as a beacon of hope and inspiration, a reminder that the heart and the mind need not be at odds, and that true progress is born from the courage to pursue one's dreams, regardless of societal constraints.

In the quiet moments of reflection, Adelaide and Alexander would often gaze upon the city they had helped transform. Their legacy was not just in the machines that powered it or the social reforms they championed, but in the indelible mark they left on the hearts and minds of those who dared to dream of a better world.

"""

from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key="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")

# Run `cat 1.mp3 2.mp3 3.mp3 4.mp3 > historical_fiction.mp3` to merge the audio files
speech_file_path = Path(__file__).parent / "4.mp3"
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="fable",
    input=text
)
response.stream_to_file(speech_file_path)