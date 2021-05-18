from io import open
from setuptools import setup
import sys

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='charpy',
    version='0.1.0',
    license='MIT',
    url='https://github.com/shuds13/pyexample',
    description='A game engine that lets you write text/ansii based games, targets 30fps.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nate Brooks',
    author_email='nateonguitar@gmail.com',
    packages=[
        'charpy',
    ],
    install_requires=[
        'pynput',
        'numpy',
    ],
    classifiers=[
        'Intended Audience :: Fun',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='game engine text based charpy',
)
