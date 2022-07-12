# -*- coding: utf-8 -*-
"""
Spell checking functions
"""
from typing import List


def spell(word: str, engine: str = "ediz") -> List[str]:
    """
    Provides a list of possible correct spelling of the given word.

    Param:
        word:   str
                Word to spell check
        engine: str
                "ediz" - apply from edit distance algorithm
                "norvig" - Peter Norvig's algorithm
                default as ediz
    Return: 
        list of possible correct words.
    """
    if engine == "norvig":
        from spell.norvig import candidates as SPELL_CHECKER
        text_correct = SPELL_CHECKER(word)
    else:
        from spell.ediz import candidates as SPELL_CHECKER
        text_correct = SPELL_CHECKER(word)

    return text_correct


def correct(word, engine="ediz"):
    """
    Corrects the spelling of the given word by returning
    the correctly spelled word. 

    Params:
        word:   str
                word to correct spelling
        engine: str
                "ediz" - apply from edit distance algorithm
                "norvig" - Peter Norvig's algorithm
                default as ediz
    """
    if engine == "norvig":
        from spell.norvig import correct as SPELL_CHECKER
        text_correct = SPELL_CHECKER(word)
    else:
        from spell.ediz import correct as SPELL_CHECKER
        text_correct = SPELL_CHECKER(word)

    return text_correct


def correct_addr(addr: str, engine="ediz"):
    """
    Corrects the address.

    Param:
        addr:   str
                address to correct
        engine: str
                "ediz" - apply from edit distance algorithm
                "norvig" - Peter Norvig's algorithm
                "symspell" - symspell algorithm
                default as symspell
    Example:
        correct_addr("ที่อยูล่ 31/631 หมูี่ที่ 16 แขใงพระบรมถหาราชวัง เขตพระนซคร กจ.กรุงเทถมหานค")
        # output: "ที่อยู่ 31/631 หมู่ที่ 16 เมืองนครศรีธรรมราช เขตพระนคร จ.กรุงเทพมหานคร"
    """
    if engine == "ediz":
        from spell.ediz import correct_addr as SPELL_CHECKER
        text_correct = SPELL_CHECKER(addr)
    elif engine == "norvig":
        from spell.norvig import correct_addr as SPELL_CHECKER
        text_correct = SPELL_CHECKER(addr)
    else:
        from spell.symspell import correct as SPELL_CHECKER
        text_correct = SPELL_CHECKER(addr)

    return text_correct
