# -*- coding: utf-8 -*-
"""
Spell checker, using symspell algorithm.
Inspiration from https://github.com/Mickzaa/Thai-sentence-correction
"""
import numpy as np
from pythaiaddr.corpus import Corpus_gram
from pythaiaddr.corpus.preprocess import Preprocess
from pythaiaddr.tokenize import word_tokenize

# data
unigram = Corpus_gram(gram="uni")
bigram = Corpus_gram(gram="bi")
trigram = Corpus_gram(gram="tri")
delete_dict = Preprocess(unigram)


def preprocess_input(addr: str):
    """
    Extract numbers from addresses and cut words.

    Param:
        addr:   str
                input
    Example:
        addr = "ที่อมยู่ 147/69 หมู่ทฌี่ 1"
        preprocess_input(addr)
        # output: ([' ', 'ที่อมยู่', ' ', '<n/>', '/', '<n/>', ' ', 'หมู่ทฌี่',' ', '<n/>', ' ',],['147', '69', '1'])
    """
    addr = " "+addr+" "
    words = word_tokenize(addr)
    numbers = list(filter(lambda word: str(word).isnumeric(), words))
    words = list(map(lambda word: "<n/>" if word.isnumeric() else word, words))
    return words, numbers


def word_trigram_choice(input_words):
    """
        Choice trigram  with the highest frequency
        Param:
            input_words: list of 3 word

        Return:
            list of 3 word from most frequency

    """
    if len(input_words) != 3:
        input_words = input_words[:3]

    # Find candidate word for each word
    record_candidate_word = []
    for word in input_words:
        # Corrosion set of a word
        each_word_list = delete_dict.candidate(word)
        each_word_list = [word, *each_word_list]
        record_candidate_word.append(each_word_list)

    # Combine each candidate words to possible trigram word
    all_posible_words = list()
    for word1 in record_candidate_word[0]:
        for word2 in record_candidate_word[1]:
            for word3 in record_candidate_word[2]:
                new_word = word1+word2+word3
                all_posible_words.append(new_word)
                # print(f"-> {new_word}")

    # Loop edit word in dict again to find most freq(prob)
    selected_words = []
    freq_words = []
    for item in all_posible_words:
        freq_word = 0
        if item in unigram.corpus_dict.keys():
            freq_word = unigram.corpus_dict[item]
            freq_word = freq_word*1
            selected_words.append(item)
            freq_words.append(int(freq_word))
        elif item in bigram.corpus_dict.keys():
            freq_word = bigram.corpus_dict[item]
            freq_word = freq_word*10
            selected_words.append(item)
            freq_words.append(int(freq_word))
        elif item in trigram.corpus_dict.keys():
            freq_word = trigram.corpus_dict[item]
            freq_word = freq_word*100
            selected_words.append(item)
            freq_words.append(int(freq_word))
        # if freq_word!=0:
        #     print(f"{item} {freq_word}")

    try:
        highest_freq_word = selected_words[np.argmax(freq_words)]
        return highest_freq_word
    except:
        return "".join(input_words)


def compare_bigram(wordList1, wordList2):
    """
    Choice bigram  with the highest frequency

    Param:
        wordList1,wordList2:    list srt
                                list of 2 word to compare

    Retrun:
        list of words with higher frequency

    Example:
        compare_bigram (['<n/>',' '],['<n/>','/'])
        # output: ['<n/>', ' ']
    """
    word1 = ''.join(wordList1)
    word2 = ''.join(wordList2)
    try:
        freq_word1 = bigram .corpus_dict[word1]
    except:
        freq_word1 = 0
    try:
        freq_word2 = bigram .corpus_dict[word2]
    except:
        freq_word2 = 0
    if freq_word1 >= freq_word2:
        return wordList1
    else:
        return wordList2


def delete_intersect(trigram_choice):
    """
        Choice and delete intersection word between trigram

        Param:
            trigram_choice:  str
                            list of trigram word
                            ex. ["<n/>/จ.","/จ.กรุงเทพมหานคร"]

    """
    # delete intersect word
    sent = []
    for i in range(len(trigram_choice[:-1])):
        cur = word_tokenize(trigram_choice[i])[1:]
        next = word_tokenize(trigram_choice[i+1])[:2]
        # if bigram is not equal we choice one
        if cur != next:
            # compare and select bigram
            intersect = compare_bigram(cur, next)
            # edit frist and second word of next word to list of word that higher frequency
            trigram_choice[i+1] = "".join([*intersect,
                                          *word_tokenize(trigram_choice[i+1])[-1:]])

        # first valuse is space, we not store it.
        if i != 0:
            # store first word
            sent.append(word_tokenize(trigram_choice[i])[0])

    # store last word that we haven't compare
    sent = [*sent, *word_tokenize(trigram_choice[-2: -1][0])]
    return sent


def mapNumber(sent, num):
    """
    Example:
        a = [' ','ที่อยู่',' ','<n/>','/','<n/>',' ','หมู่ที่',' ','<n/>',' ','แขวง','คลองสามประเวศ']
        b = [12,34,66]
        # output: [' ','ที่อยู่',' ',12,'/',34,' ','หมู่ที่',' ',66,' ','แขวง','คลองสามประเวศ']
    """
    if len(num) == 0:
        return sent
    for i in range(len(num)):
        try:
            for j in range(len(sent)):
                if sent[j] == "<n/>":
                    sent[j] = num[i]
                    break
        except:
            break
    return sent


def delete_space(addr: str):
    """
    Remove multiple spaces in a string

    Param:
        addr:   str

    Example:
        addr = 'แขวงคลองสามประเวศ    เขตลาดกระบัง  จ.กรุงเทพมหานคร'
        delete_space(addr)
        # output: 'แขวงคลองสามประเวศ เขตลาดกระบัง จ.กรุงเทพมหานคร'

    """
    return " ".join(addr.split())


def correct(input_addr):
    """ 
    Param:
        input_addr: str

    Return
        sent:   str

    Example:
        addr = "ที่อมยู่ 147/69 หมู่ทฌี่ 1 แขวงคลองสามปรฦเวศ เขตลาดูระบัง จ.กรุง๊เทพมหานครร"
        correct(addr)
        # output: 'ที่อยู่ 147/69 หมู่ที่ 1 แขวงคลองสามประเวศ เขตลาดกระบัง จ.กรุงเทพมหานคร'
    """
    # preprocess input
    words, num = preprocess_input(input_addr)

    # get list of trigram
    trigram_choice = []
    for i in range(len(words[:-2])):
        trigram = [words[i], words[i+1], words[i+2]]
        trigram_correct = word_trigram_choice(trigram)
        trigram_choice.append(trigram_correct)

    # delete interection between trigram
    sent = delete_intersect(trigram_choice)

    # mapping number into address
    sent = mapNumber(sent, num)
    sent = delete_space(''.join(sent))
    return sent
