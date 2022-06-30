# =======================================================================================
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
