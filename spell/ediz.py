from Xtokenize import word_tokenize as newmm_tokenize
from Levenshtein import ratio
from corpus import Thai_address

addresses = Thai_address()


def correct(word):
    """
    Most probable spelling correction for word.

    Params: 
        word:   str
                input word.

    Return:
        the word that has leastedit distance from the input word.

    Example:
        spell('ที่อยูล่')
        # "ที่อยู่"
    """
    if word.isnumeric() or word == " " or word == "/":
        return word

    temp = candidates(word, 1)
    # if distance>0.3 and len(word)<=2
    if temp[0][1] > 0.3 and len(temp[0][0]) <= 2:
        return ""
    return temp[0][0]


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
        list of ("word": edit_distance)

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
    def split_address(word, num=3):
        """
        Find words in addresses that word length is between the range of words entered.
        Available to reduce the size of the dictionary.
        """
        n_char = len(word)
        return {k: v[1] for k, v in addresses.items() if v[0] in range(n_char-num, n_char+num)}

    address = split_address(word)

    dist = {key: 1-ratio(word, key) for key in address}
    n_address = len(addresses)
    if show > n_address:
        show = n_address
    return sorted(dist.items(), key=lambda x: x[1], reverse=False)[:show]


def correct_addr(addr: str):
    """
    """
    words = newmm_tokenize(addr)
    temp = []
    for word in words:
        temp.append(correct(word))
    return "".join(temp)
