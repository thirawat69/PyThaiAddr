import os
from typing import Union

_CORPUS_DIRNAME = "corpus"


def get_corpus(filename: str, as_is: bool = False) -> Union[frozenset, list]:
    """
    Read corpus data from file and return a frozenset or a list.
    Each line in the file will be a member of the set or the list.

    Param:
        filename:   str 
                    filename of the corpus to be read
        as_is:      bool
                    Variables for configuration of return type
                    Default as False, a frozenset will be return. 
                    If as_is is True, a list will be return.

    Return: 
        class:  `frozenset`
                a frozenset will be return, with whitespaces stripped, and
                empty values and duplicates removed.
        class:  `list` 
                a list will be return, with no modifications
                in member values and their orders.

    Example:
        get_corpus('negations_th.txt')
            # output:
            # frozenset({'แต่', 'ไม่'})
        get_corpus('ttc_freq.txt')
            # output:
            # frozenset({'โดยนัยนี้\\t1',
            #    'ตัวบท\\t10',
            #    'หยิบยื่น\\t3',
            #     ...})
    """

    path = os.path.join(os.path.dirname(__file__), filename)

    lines = []
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()

    if as_is:
        return lines

    lines = [line.strip() for line in lines]

    return frozenset(filter(None, lines))


def get_address(filename: str):
    """
    Read Thai address and create a dictionary that values have two dimensions.
    first dimension as word length, and the second dimension as word distance.
    by default, word distance is zero.

    Param:
        filename:   str 
                    filename of the corpus to be read

    Return: dictionary
            {
                "word": [wordLength, distance],
                "word": [wordLength, distance],
                .
                .
                .
                "word": [wordLength, distance]
            }

    Example:
            {   'ที่อยู่': [7, 0],
                'หมู่ที่': [7, 0],
                .
                .
                .
                'เมืองสุโขทัย': [12, 0]
            }
    """
    path = os.path.join(os.path.dirname(__file__), filename)

    lines = []
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()

    return {i: [len(i), 0] for i in lines}


def get_word_freq(filename: str):
    """
    Param:
        filename:   str 
                    filename of the corpus to be read
    """
    path = os.path.join(os.path.dirname(__file__), filename)

    lines = []
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()

    word = ["".join(x.split("\t")[:-1]) for x in lines]
    freq = [int("".join(x.split("\t")[-1])) for x in lines]
    dict_corpus = dict(zip(word, freq))
    return dict_corpus


# ----------------------------------------------------------------------------------------
thai_consonants = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ"  # 44 chars

thai_vowels = (
    "\u0e24\u0e26\u0e30\u0e31\u0e32\u0e33\u0e34\u0e35\u0e36\u0e37"
    + "\u0e38\u0e39\u0e40\u0e41\u0e42\u0e43\u0e44\u0e45\u0e4d\u0e47"
)  # 20
thai_lead_vowels = "\u0e40\u0e41\u0e42\u0e43\u0e44"  # 5
thai_follow_vowels = "\u0e30\u0e32\u0e33\u0e45"  # 4
thai_above_vowels = "\u0e31\u0e34\u0e35\u0e36\u0e37\u0e4d\u0e47"  # 7
thai_below_vowels = "\u0e38\u0e39"  # 2

thai_tonemarks = "\u0e48\u0e49\u0e4a\u0e4b"  # 4

# Paiyannoi, Maiyamok, Phinthu, Thanthakhat, Nikhahit, Yamakkan:
# These signs can be part of a word
thai_signs = "\u0e2f\u0e3a\u0e46\u0e4c\u0e4d\u0e4e"  # 6 chars

# Any Thai character that can be part of a word
thai_letters = "".join(
    [thai_consonants, thai_vowels, thai_tonemarks, thai_signs]
)  # 74
