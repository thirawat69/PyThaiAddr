from distutils.core import setup


readme = """
123
"""


setup(
    name='pythaiaddr',         # How you named your package folder (MyLib)
    packages=['pythaiaddr','pythaiaddr.corpus','pythaiaddr.spell','pythaiaddr.tokenize','pythaiaddr.util'],   # Chose the same as "name"
    package_data={'pythaiaddr': ['corpus/*.txt']},
    version='0.0.6',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Correct thai address',
    long_description=readme,
    author='Thirawat Phongsathatkit',                   # Type in your name
    author_email='Thirawatp9@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/thirawat69',
    # I explain this later on
    download_url='https://pypi.org/project/pythaiaddr/0.0.6/#files',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
