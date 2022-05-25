# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:

# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."
sentence2 = 'This is a brown fox'
sentence3 = 'Richard Of York Gave Battle In Vain'
sentence4 = 'If a dog chews shoes, whose shoes does he choose?'

def replace_words(text, length_to_replace, word):
    text = text.split(' ')
    for i, v in enumerate(text):
        if len(v) == length_to_replace:
            text[i] = word
    return ' '.join(text)

print(replace_words(sentence4, 5, 'ping pong'))

assert replace_words(sentence, 3, "test") == "Beginners when start programming often test bored if they do test test a chance " \
                                "to play with some interesting code."
assert replace_words(sentence2, 3, 'hi') == 'This is a brown hi'
assert replace_words(sentence3, 4, 'Kiev') == 'Richard Of Kiev Kiev Battle In Kiev'
assert replace_words(sentence4, 5, 'ping pong') == 'If a dog ping pong shoes, ping pong ping pong does he choose?'

