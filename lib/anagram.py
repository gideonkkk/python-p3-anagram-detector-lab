class Anagram :
    def __init__(self, word):
        self.word = word.lower()
    def match(self, word_list):
        sorted_word = sorted(self.word)
        matches = []
        for word in word_list:
            if sorted(word.lower()) == sorted_word:
                matches.append(word)
        return matches
finder = Anagram("finder")
print(finder.match(['friend', 'refind', 'rindef', 'fired']))

