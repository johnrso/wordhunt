import json

class Alphabet:

    def __init__(self, file):
        self.words = json.loads(open(file).read())
        self.dist = self.generate_dist();
        self.letters = self.generate_letters();

    def generate_dist(self):
        dict = self.words
        dist = {}

        for key in [*(self.words)]:
            for letter in key:
                if letter in dist and letter != '-' and letter != " ":
                    dist[letter] += 1
                else:
                    dist[letter] = 1

        return dist

    def generate_letters(self):
        letters = []
        for key in [*(self.words)]:
            for letter in key:
                if letter not in letters and letter != '-':
                    letters += [letter]

        return letters

    def generate_weights(self, alphabet):
        total = 0

        weights = {}

        for letter in alphabet:
            total += self.dist[letter]
            weights[letter] = self.dist[letter]

        for letter in weights:
            weights[letter] /= total

        return weights

    def get_words(self):
        return self.words

    def check_word(self, word):
        return word in self.words
