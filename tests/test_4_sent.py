from pythaiaddr import correct_addr
from pythaiaddr import word_tokenize as newmm_tokenize


addr = "ที่อยูล่ 31/631 หมูี่ที่ 16 แขวงพระบรมถหาราชวัง เขตพระนซคร จ.กรุงเทพมหานค 1113"
token = newmm_tokenize(addr)
print(token)

print(correct_addr(addr,'ediz'))
print(correct_addr(addr,'norvig'))
print(correct_addr(addr,'symspell'))


