from pythaiaddr import word_tokenize as newmm_tokenize

# addr = "ที่อยู่ 31/631 หมู่ที่ 16 แขวงพระบรมมหาราชวัง เขตพระนคร จ.กรุงเทพมหานคร"
# addr = "ที่อfยูล่ 31/631 หมูี่ที่ 16 แขใงพระบรมถหาราชวัง เขตพระนซคร กจ.กรุงเทถมหานคร"
addr = "ที่ชยู่ 125/52 หมู่ทตี่ 10 ต.อดงัะดะ ฮ.ยแม่ลาว จ.เชียงรเาย"
print(newmm_tokenize(addr))
