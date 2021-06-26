from setuptools import setup, Extension
import os

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # How you named your package folder (MyLib)
    name='gitprofile',
    packages=['gitprofile'],   # Chose the same as "name"
    version='0.3',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Extract public repository data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Euan Campbell',                   # Type in your name
    author_email='dev@euan.app',
    # Provide either the link to your github or to your website
    url='https://github.com/euanacampbell/gitprofile',
    # I explain this later on
    download_url='https://github.com/euanacampbell/gitprofile/archive/refs/heads/master.tar.gz',
    # Keywords that define your package best
    keywords=['GitHub', 'scraping', 'requests'],
    install_requires=[
        'requests==2.25.1',
        'beautifulsoup4==4.9.3'      # I get to this in a second
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
