text = """

In the realm of Aldoria, where the winds carried whispers of war and the land trembled with the echoes of conflict, two infants were born on a fateful night. Alaric, with hair as dark as a moonless night and eyes that gleamed like steel, was taken to the formidable Northern Army by the order of the king. Meanwhile, Elara, with locks of silver that seemed to shimmer with their own light and eyes ablaze with a mysterious allure, was entrusted to the secretive Order of the Enchanted Flame in the Southern Kingdom.

Alaric grew up amidst the clang of swords and the heavy footfalls of seasoned warriors. He trained tirelessly, his muscles honed to steel and his mind sharpened with the teachings of discipline and strategy. The Northern Army stood as a bastion of strength and valor, their resilience forged in the harsh winters and unforgiving landscapes of their homeland. Alaric's name soon became synonymous with courage and leadership, his every move on the battlefield a testament to his skill and unwavering resolve.

On the other end of the realm, Elara delved into the mysteries of magic within the opulent walls of the Order of the Enchanted Flame. She studied under the tutelage of the most powerful sorcerers, her fingertips tracing sigils of ancient power and her voice weaving spells that danced like wildfire. In the Southern Kingdom, where beauty held sway and power was as intoxicating as the rarest of wines, Elara blossomed into a sorceress of unparalleled grace and prowess. Whispers of her abilities spread far and wide, carrying tales of storms called forth at a flick of her wrist and illusions that ensnared the senses.

As the years passed, Alaric rose through the ranks of the Northern Army, his leadership inspiring loyalty in his soldiers and fear in his enemies. Battles raged across the realm, each clash leaving scars on the land and sorrow in the hearts of the people. The war between the North and the South seemed endless, fueled by ancient rivalries and unspoken grievances that festered like wounds that refused to heal.

Alaric and Elara, unknowing of each other's existence, followed their separate paths with determination and conviction, each bound by duty to their factions and driven by a sense of purpose that burned bright within their souls. Little did they know that destiny, like a tapestry woven by unseen hands, was preparing to draw them together in a web of fate that neither could escape.

And so, as Alaric stood at the head of his army, sword raised high and eyes steely with resolve, and Elara channeled the elements with a grace that spoke of ancient power, the stage was set for their paths to converge in a clash of strength and magic that would shake the very foundations of Aldoria.

"""

from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key="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")

speech_file_path = Path(__file__).parent / "story.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text
)
response.stream_to_file(speech_file_path)