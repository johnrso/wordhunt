import words

def gen_dist():
    dict = words.gen_words()
    weights = {}

    for key in [*dict]:
        for letter in key:
            if letter in weights:
                weights[letter] += 1
            else:
                weights[letter] = 1

    del weights['-']

    return weights

def gen_weights(alpha):
    weights = gen_dist()
    total = sum([weights[i] for i in weights])
    p = []

    for letter in alpha:
        p.append(weights[letter] / total)

    return p
