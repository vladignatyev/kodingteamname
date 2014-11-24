import enchant
import random

_EN_ALPHABET = map(chr, range(97, 123))
_NUMBERS = map(str, range(0, 9))


class Names(object):
	def __init__(self, character_set=tuple(_NUMBERS + _EN_ALPHABET)):
		self.characters = character_set

	def generator(self, num_words=2, min_symbols=3, max_symbols=6, use_enchant=True, enchant_locale='en_US', separator=' '):
		if use_enchant:
			d = enchant.Dict(enchant_locale)
		else:
			d = None

		while True:
			result = []
			characters_length = len(self.characters)

			for word_i in range(0, num_words):
				word_len = random.randint(min_symbols, max_symbols)
				word = ''
				for i in range(0, word_len):
					word += self.characters[random.randint(0, characters_length-1)]
				
				if d:
					suggestions = d.suggest(word)
					if suggestions:
						word = str(suggestions[random.randint(0, len(suggestions) - 1)])

				result += [word]

			yield separator.join(result)


if __name__ == '__main__':
	names = Names()
	g = names.generator()
	for i in range(0, 10):
		print g.next()