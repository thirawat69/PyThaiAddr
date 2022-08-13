from distutils.core import setup


readme = """
# PyThaiAddr: Thai Address Processing in Python

PyThaiAddr is a Python language library for processing Thai addresses. Currently focusing on word correcting.

PyThaiAddr เป็นไลบารีภาษาไพทอนสำหรับประมวลผลที่อยู่ภาษาไทย โดยปัจจุบันเน้นไปที่การแก้คำผิด


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyThaiAddr.

```bash
pip install pythaiaddr
```


see more on [Github](https://github.com/thirawat69/PyThaiAddr)
"""

setup(
    name='pythaiaddr',         # How you named your package folder (MyLib)
    packages=['pythaiaddr','pythaiaddr.corpus','pythaiaddr.spell','pythaiaddr.tokenize','pythaiaddr.util'],   # Chose the same as "name"
    package_data={'pythaiaddr': ['corpus/*.txt']},
    version='0.0.8',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Correct thai address',
    long_description=readme,
    author='Thirawat Phongsathatkit',                   # Type in your name
    author_email='Thirawatp9@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/thirawat69/PyThaiAddr',
    # I explain this later on
    download_url='https://pypi.org/project/pythaiaddr/0.0.8/#files',
    # Keywords that define your package best
    keywords=['correct', 'correction', 'thai', 'address', 'spell'],
    install_requires=[
        'python-Levenshtein == 0.12.2',
        'numpy'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
