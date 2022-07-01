from .corpus import get_corpus, get_address, get_word_freq, thai_letters

_THAI_LETTERS = thai_letters

_THAI_ADDRESS_INDICATION_FILENAME = "Thai_address_indication.txt"
_THAI_ADDRESS_INDICATION = get_corpus(_THAI_ADDRESS_INDICATION_FILENAME)

_THAI_ADDRESS_FILENAME = "Thai_address_with_BKKraod.txt"
_THAI_ADDRESS = get_address(_THAI_ADDRESS_FILENAME)

_WORD_FREQ_FILENAME = "Thai_addr_word_frequency.txt"
_WORD_FREQ = get_word_freq(_WORD_FREQ_FILENAME)

_UNIGRAM = "Thai_addr_uiigrame_frequency.txt"
_BIGRAM  = "Thai_addr_bigrame_frequency.txt"
_TRIGRAM = "Thai_addr_trigrame_frequency.txt"


def Thai_address_indication() -> frozenset:
    """
    Return a frozenset of Thai address indication such as "ที่อยู่", "หมู่ที่", "แขวง".

    Return: 
        class:  `frozenset`
                containing Thai address indication in Thai language.
    """
    return _THAI_ADDRESS_INDICATION


def Thai_address():
    """
    Return a frozenset of Thai address indication such as "ที่อยู่", "หมู่ที่", "แขวง".

    Return: 
        class:  `frozenset`
                containing Thai address indication in Thai language.
    """
    return _THAI_ADDRESS

def Word_freq():
    """
    Return dictionary of frequency.
    {   
        'จ.': '7437', 
        'ที่อยู่': '7436',
        .
        .
        .
        'ปากเกร็ด': '13'
    }
    """
    return _WORD_FREQ

class Corpus_gram():
    """
        Param:
            n:  str
                - "uni"
                - "bi"
                - "tri"
    """
    def __init__(self,n):
        if self.n=="bi":
            corpus_dict = get_word_freq(_BIGRAM)
        elif self.n == "tri":
            corpus_dict = get_word_freq(_TRIGRAM)
        else:
            corpus_dict = get_word_freq(_UNIGRAM)
        self.corpus_dict = corpus_dict
        self.words = list(self.corpus_dict.keys())
        self.freqs = list(self.corpus_dict.values())

    def __len__(self):
        return len(self.dict_corpus)

    def __getitem__(self, word):
        return self.dict_corpus[word]