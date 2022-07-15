# -*- coding: utf-8 -*-
"""
Spell checker, using Peter Norvig algorithm.
Based on Peter Norvig's Python code from http://norvig.com/spell-correct.html
"""
from collections import Counter
from pythaiaddr.corpus import Word_freq, _THAI_LETTERS
from pythaiaddr.tokenize import word_tokenize as newmm_tokenize


WORDS = Word_freq()
WORDS_TOTAL = sum(WORDS.values())


def P(word):
    "Probability of `word`."
    return WORDS[word] / WORDS_TOTAL


def correct(word):
    """
    Most probable spelling correction for word.
    """
    if word.isnumeric() or word == " " or word == "/":
        return word

    try:
        word = max(candidates(word), key=P)
    except:
        pass

    return word


def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return list(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in _THAI_LETTERS]
    inserts = [L + c + R for L, R in splits for c in _THAI_LETTERS]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))


def correct_addr(addr: str):
    """
    correct thai address

    Param:
        addt:   str
                thai address

    Return:
        corrected thai address
    """
    words = newmm_tokenize(addr)
    temp = []
    for word in words:
        temp.append(correct(word))
    return "".join(temp)
