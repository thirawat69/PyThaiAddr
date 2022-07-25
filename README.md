<div align="center">
    <h1>PyThaiAddr: Thai Address Processing in Python</h1>
    <a href="https://pypi.python.org/pypi/pythaiaddr"><img alt="pypi" src="https://img.shields.io/pypi/v/pythaiaddr.svg"/></a>
    <a href="https://www.python.org/downloads/release/python-370/"><img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-blue.svg"/></a>
    <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/github/license/thirawat69/PyThaiAddr"/></a>
</div>
PyThaiAddr is a Python language library for processing Thai addresses. Currently focusing on word correcting.

PyThaiAddr เป็นไลบารีภาษาไพทอนสำหรับประมวลผลที่อยู่ภาษาไทย โดยปัจจุบันเน้นไปที่การแก้คำผิด

## Getting Started
- PyThaiAddr requires Python 3.6+
- PyThaiAddr Document v.1 [notebook](https://github.com/thirawat69/PyThaiAddr/blob/main/doc/PyThaiAddr_Document_v_1.ipynb) [colab](https://colab.research.google.com/drive/151UPvQdnrP26MGo25wFkQEhp_0nomgiP) | PyThaiAddr Document v.2 [notebook ](https://github.com/thirawat69/PyThaiAddr/blob/main/doc/PyThaiAddr_Document_v_2.ipynb) [colab](https://colab.research.google.com/drive/1ih_i--tWlI-Aiq172qCKO02F43GDXYhG)
- Note [notebook](https://github.com/thirawat69/PyThaiAddr/blob/main/doc/note.ipynb)[colab](https://colab.research.google.com/drive/1Q7GNv2-8t6c5UAxbGqV0nJw3JJXeRp9k?) - for more information about performance and accuracy.

## Capabilities
<details>
  <summary>List of Features</summary>
  
- Character and words about the address, like Thai address (`Thai_address`), All Thai charactor (`_THAI_LETTERS`).
- Thai address linguistic unit tokenization, including sentence (`word_tokenize`)
- Thai address spelling suggestion and correction (`spell` and `correct` and `correct_addr`)

</details>


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyThaiAddr.

```bash
pip install pythaiaddr
```

## Usage

Tokenize 
```
from pythaiaddr import word_tokenize

addr = 'ที่ชยู่ 125/52 หมู่ทตี่ 10 ต.อดงัะดะ อ.ยแม่ลาว จ.เชียงรเาย'
word_tokenize(addr)
```

Spelling 
```
from pythaiaddr import spell

word = 'c.กรุงเทถมหานค'
spell(word , engine='norvig')
```

Correcting word
```
from pythaiaddr import correct

print(correct('กรุงเทถมหานค', engine='ediz'))
```

Correcting address
```
from pythaiaddr import correct_addr

addr = 'ที่อยูล่ 31/631 หมูี่ที่ 16 แขวงพระบรมถหาราชวัง เขตพระนซคร จ.กรุงเทพมหานค 1113'
correct_addr(addr, engine='symspell')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
