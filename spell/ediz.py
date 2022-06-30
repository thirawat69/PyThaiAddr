import os
from tokenize.tokenizer import word_tokenize as newmm_tokenize
from Levenshtein import ratio
import multiprocessing
from corpus.common import Thai_address

addresses = Thai_address()

"""
edit 
 distance
   zee
ediz
"""


def split_address(word, num=3):
    """
    Find words in addresses that word length is between the range of words entered.
    Available to reduce the size of the dictionary.

    Params: 
        addresses:  dictionary
                    the valuse of this dictionary is two dimesion.
                    first dimension as word length, and the second dimension as word distance.
        word:   str
                input word.
        num:    int
                the number that defines the range from the input word.
                defult as 3

    Return:
        {
            "word": distance,
            "word": distance,
            .
            .
            .
            "word": distance,
        }

    Example:
        split_address('ที่อยูล่')
        {
            'ที่อยู่': 0,
            'หมู่ที่': 0,
            .
            .
            .
            'ทับสะแก': 0
        }
    """
    n_char = len(word)
    return {k: v[1] for k, v in addresses.items() if v[0] in range(n_char-num, n_char+num)}


def candidates(word, show=10):
    """
    Find nearby words from input word.

    Params: 
        word:   str
                word to search for nearby words.
        show:   int
                size of return.
                default as 10

    Return: 
        [
            ("word": distance),
            ("word": distance),
            .
            .
            .
            ("word": distance),
        ]

    Example:
        candidates('ที่อยูล่')
        [
            ('ที่อยู่', 0.06666666666666665),
            ('ท่าอยู่', 0.19999999999999996),
            .
            .
            .
            ('ข่อยสูง', 0.4666666666666667)
        ]
    """
    address = split_address(word)
    dist = {key: 1-ratio(word, key) for key in address}
    n_address = len(addresses)
    if show > n_address:
        show = n_address
    return sorted(dist.items(), key=lambda x: x[1], reverse=False)[:show]


def correction(word, show=False):
    """
    Corrected the entered words to be spelled correctly.

    Params: 
        word:   str
                input word.
        show:   bool
                Variable for determining whether to display editdistance value or not.
                default as False

    Example:
        spell('ที่อยูล่')
        # "ที่อยู่"
        spell('ที่อยูล่',True)
        # ('ที่อยู่', 0.06666666666666665)
    """
    if show:
        return candidates(word, 1)[0][0], candidates(word, 1)[0][1]
    return candidates(word, 1)[0][0]


def worker(i, word, return_dict):
    # s = time.time()
    if word.isnumeric() or word == " " or word == "/":
        return_dict[i] = word
    else:
        edited, dist = correction(word, True)
        if dist > 0.3 and len(word) <= 2:
            return_dict[i] = ""
        else:
            return_dict[i] = edited
    # print(f"{word}->{return_dict[i]}   {time.time()-s}")


def correction_address(address):
    # tokenize
    words = newmm_tokenize(address)

    # multiprocess
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []

    for i, word in enumerate(words):
        p = multiprocessing.Process(
            target=worker, args=(i, word, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    return_dict = dict(sorted(return_dict.items()))

    return "".join(str(n) for n in return_dict.values())
