import re
from typing import List, Optional
from pythaiaddr.util.trie import Trie
from pythaiaddr.tokenize.newmm import segment


def word_tokenize(
    text: str,
    keep_whitespace: bool = True,
) -> List[str]:

    if not text or not isinstance(text, str):
        return []

    segments = segment(text)

    if not keep_whitespace:
        segments = [token.strip(" ") for token in segments if token.strip(" ")]

    return segments
