# -*- coding: utf-8 -*-
import random

EN_ALPHABET = map(chr, range(97, 123))
DIGITS = map(str, range(0, 9))


class Names(object):
    def __init__(self, character_set=tuple(DIGITS + EN_ALPHABET)):
        self.characters = character_set

    def generator(self, num_words=2, min_symbols=3, max_symbols=6, use_words=True, words=(), use_enchant=True, enchant_locale='en_US', separator=' '):
        if use_enchant:
            import enchant
            d = enchant.Dict(enchant_locale)
        elif use_words:
            words_len = len(words)
        else:
            d = None

        characters_length = len(self.characters)

        while True:
            result = []

            for word_i in range(0, num_words):
                word_len = random.randint(min_symbols, max_symbols)
                word = u''

                if use_words:
                    dictionary = filter(lambda w: len(w) == word_len, words)
                    word = words[random.randint(0, len(dictionary) - 1)]
                else:
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