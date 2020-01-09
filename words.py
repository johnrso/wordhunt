import json

def gen_words():
    return json.loads(open('words_dictionary.json').read())
