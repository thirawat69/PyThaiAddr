from distutils.core import setup
import os.path


setup(
    name='pythaiaddr',         # How you named your package folder (MyLib)
    packages=['pythaiaddr'],   # Chose the same as "name"
    version='0.0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Correct thai address',
    long_description='plese read in: https://github.com/thirawat69/PyThaiAddr',
    author='Thirawat Phongsathatkit',                   # Type in your name
    author_email='Thirawatp9@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/thirawat69',
    # I explain this later on
    download_url='',
    # Keywords that define your package best
    keywords=['correct', 'correction', 'thai', 'address', 'spell'],
    install_requires=[
        'python-Levenshtein == 0.12.2',
        'numpy == 1.19.5'
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
