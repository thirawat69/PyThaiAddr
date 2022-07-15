
"""
original code from Thai-sentence-correction
github: https://github.com/Mickzaa/Thai-sentence-correction
"""


class Preprocess():
    """Preprocess corpus to be used as a corrosion dictionary"""

    def __init__(self, corpus):

        self.corpus_dict = corpus.corpus_dict
        self.corpus_word = corpus.words
        dict_corrotion = dict()
        for n_gram in self.corpus_word:
            self.corrosion_to_dict(dict_corrotion, n_gram)
        self.dict_corrotion = dict_corrotion

    def corrosion_to_dict(self, dict_corrotion, n_gram):
        """convert dictionary of word to be corrosion dict 
            e.g.'เที่ย': {'เที่ยง', 'เที่ยม', 'เที่ยว'}
        Args:
            dict_corrotion (dict): corrosion dict of unigrame
            n_gram (str): word
        """
        for delete1 in self.edits1(n_gram):
            if dict_corrotion.get(delete1) is None:
                dict_corrotion.update({delete1: {n_gram}})
            else:
                dict_corrotion.get(delete1).add(n_gram)

        for delete2 in self.edits2(n_gram):
            if dict_corrotion.get(delete2) is None:
                dict_corrotion.update({delete2: {n_gram}})
            else:
                dict_corrotion.get(delete2).add(n_gram)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        return set(deletes)

    def edits2(self, word):
        "All edits that are two edits away from `word`."
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def candidate(self, word):
        """Find correct word choices of the misspell word
            e.g. candidate('ม้าลา') -> {'มาลา', 'ม้าล', 'ม้าลาย'}
        Args:
            word (str): A misspell word

        Returns:
            set: Correct word possible choices
        """
        candidates = set()
        # Misspell edit distance 1
        if word in self.dict_corrotion.keys():
            candidates.update(self.dict_corrotion[word])

        delete_set = self.edits2(word)
        for word_delete in delete_set:
            # typing exceed exactly 1 wrong
            if word_delete in self.corpus_word:
                candidates.add(word_delete)

            # typing exceed exactly 2 wrong
            if word_delete in self.dict_corrotion.keys():
                candidates.update(self.dict_corrotion[word_delete])
        if len(word) == 1 and word != " ":
            candidates.add("")

        return candidates